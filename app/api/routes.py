from flask import jsonify, request
from . import bp
from ..models import Character
from ..schemas import CharacterSchema
from ..services import CharacterBuilder
from ..extensions import db
from marshmallow import ValidationError
from flask import current_app

characters_schema = CharacterSchema(many=True)  # Renamed for clarity
single_character_schema = CharacterSchema()  # Added for single character responses
update_character_schema = CharacterSchema(partial=True)  # Schema for partial updates


@bp.route("/characters", methods=["GET"])
def get_characters():
    """Get a list of all characters."""
    all_characters = Character.query.all()
    result = characters_schema.dump(all_characters)
    print(result)
    return jsonify(result)


@bp.route("/characters", methods=["POST"])
def create_character():
    """Create a new character using the builder."""
    # TODO: Accept configuration from request.json if needed
    # config = request.json or {}

    builder = CharacterBuilder()
    # Example: Apply config if provided
    # if 'min_age' in config and 'max_age' in config:
    #     builder.set_age_range(config['min_age'], config['max_age'])

    new_character = builder.build()

    db.session.add(new_character)
    db.session.commit()

    result = single_character_schema.dump(new_character)

    # Prepare response
    response = jsonify(result)
    response.status_code = 201
    # Add location header if we have a get_character(id) endpoint
    # response.headers['Location'] = url_for('api.get_character', character_id=new_character.id)
    return response


# Placeholder for getting a single character (needed for Location header)
# @bp.route('/characters/<uuid:character_id>', methods=['GET'])
# def get_character(character_id):
#     character = Character.query.get_or_404(character_id)
#     return jsonify(single_character_schema.dump(character))


@bp.route("/characters/<uuid:character_id>", methods=["PUT"])
def update_character(character_id):
    """Update an existing character."""
    character = Character.query.get_or_404(character_id)
    data = request.get_json()

    # Marshmallow's load method handles validation and updates the object
    try:
        # Using partial=True allows updating only provided fields
        # Load data into a dictionary, validating against the schema
        loaded_data = update_character_schema.load(data)
        # Iterate through validated data and update the character object
        for key, value in loaded_data.items():
            # Handle fields with property setters that expect Enums
            if key == "title":
                character.title_str = value  # Set the underlying string column
            elif key == "hair_color":
                character.hair_color_str = value  # Set the underlying string column
            else:
                setattr(character, key, value)  # Use standard setattr for other fields

    except ValidationError as err:  # Catch specific Marshmallow validation errors
        return jsonify({"message": "Validation error", "errors": err.messages}), 400
    except Exception as err:  # Catch other potential errors during update
        db.session.rollback()  # Rollback in case of non-validation errors during update
        return jsonify({"message": "Error updating character", "error": str(err)}), 500

    db.session.commit()

    result = single_character_schema.dump(character)  # Dump the updated character
    return jsonify(result)


# Add DELETE endpoint
@bp.route("/characters/<uuid:character_id>", methods=["DELETE"])
def delete_character(character_id):
    """Delete a character."""
    character = Character.query.get_or_404(character_id)
    db.session.delete(character)
    db.session.commit()
    # Standard practice is to return 204 No Content on successful delete
    return "", 204


@bp.route("/characters/bulk-generate", methods=["POST"])
def bulk_create_characters():
    """Generate multiple characters with a specified occupation."""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Request body must be JSON"}), 400

    occupation = data.get("occupation")
    count = data.get("count")

    if not occupation:
        return jsonify({"message": "Missing 'occupation' in request body"}), 400

    if not isinstance(count, int) or count <= 0:
        return jsonify({"message": "'count' must be a positive integer"}), 400

    if count > 100:  # Add a reasonable limit to prevent abuse
        return jsonify(
            {"message": "Cannot generate more than 100 characters at a time"}
        ), 400

    newly_created_characters = []
    try:
        for _ in range(count):
            builder = CharacterBuilder()
            # Build character with random attributes first
            new_character = builder.build()
            # Override the occupation with the provided one
            new_character.occupation = occupation
            # Add relationships or other default settings if needed
            db.session.add(new_character)
            newly_created_characters.append(new_character)

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        # Log the exception for debugging
        current_app.logger.error(f"Error during bulk character generation: {e}")
        return jsonify(
            {"message": "Failed to generate characters", "error": str(e)}
        ), 500

    # Optionally return the IDs or a summary of the created characters
    # result = characters_schema.dump(newly_created_characters)
    # return jsonify(result), 201
    return jsonify(
        {
            "message": f"{count} characters with occupation '{occupation}' created successfully."
        }
    ), 201
