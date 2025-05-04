# Project TODO List

- [x] Define the `Relationship` model (SQLAlchemy), incorporate it into `Character`, and update migrations.
- [x] Implement `generate_name` static method in `app/models.py`.
- [x] Create basic HTML/CSS/JS CRUD page for Characters (Read, Create).
- [x] Add Edit (Update) functionality to the character frontend.
- [x] Add Delete endpoint (`DELETE /api/characters/<id>`) to the backend.
- [x] Add Update endpoint (`PUT /api/characters/<id>`) to the backend.
- [x] Fix enum dropdowns in edit form (HTML option values don't match enum values)
- [x] Implement PUT /api/characters/<uuid:character_id> endpoint in `app/api/routes.py` for updating characters.
- [x] Refactor frontend from vanilla HTML/CSS/JS to React + Tailwind CSS
  - [x] Set up basic React + Tailwind project structure (Done)
  - [x] Create main `App.jsx` component
  - [x] Fetch and display characters in a table (`CharacterTable.jsx`)
  - [x] Implement character editing (`CharacterEditForm.jsx`)
  - [x] Implement character deletion
    - [x] Add delete button and API call (Done)
    - [x] Add custom confirmation modal
  - [x] Implement character details view
    - [x] Add View button to table
    - [x] Create `CharacterDetailModal` component
    - [x] Add state and logic to `App.jsx` to show modal with character data
  - [x] Add more columns to the main character table (Race, Occupation, Birth Place)
  - [x] Replace default Vite styling with Tailwind utility classes
  - [x] Add 'Copy Description' button to character table actions
- [x] Add Relationship model and link to Character.
- [x] Add `age` property and refine `physical_description` method in `Character` model (`app/models.py`).

# Future Ideas
