# Project TODO List

- [ ] Create a script or Flask route to generate and save sample characters using the `CharacterBuilder`.
- [ ] Build Marshmallow schemas for serializing/deserializing the `Character` and `Event` models.
- [x] Define the `Relationship` model (SQLAlchemy), incorporate it into `Character`, and update migrations.
- [ ] Adapt `CharacterBuilder` or creation logic to handle `Relationship` instances.
- [x] Implement `generate_name` static method in `app/models.py`.
- [x] Create basic HTML/CSS/JS CRUD page for Characters (Read, Create).
- [x] Add Edit (Update) functionality to the character frontend.
- [x] Add Delete endpoint (`DELETE /api/characters/<id>`) to the backend.
- [x] Add Update endpoint (`PUT /api/characters/<id>`) to the backend.
