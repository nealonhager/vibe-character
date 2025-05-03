from flask import jsonify
from . import bp
from ..models import Character
from ..schemas import CharacterSchema
from ..services import CharacterBuilder
from ..extensions import db

characters_schema = CharacterSchema(many=True)  # Renamed for clarity
single_character_schema = CharacterSchema()  # Added for single character responses


@bp.route("/characters", methods=["GET"])
def get_characters():
    """Get a list of all characters."""
    all_characters = Character.query.all()
    result = characters_schema.dump(all_characters)
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
