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
- [x] Implement basic CRUD functionality (Create, Read, Update, Delete) for characters.
- [x] Display a list of characters fetched from the backend.
- [x] Allow creating new characters.
- [x] Allow deleting characters with confirmation.
- [x] Implement viewing character details in a modal.
- [x] Implement editing character details in a modal.
- [x] Add loading states for asynchronous operations.
- [x] Add error handling and display messages to the user.
- [x] Add a copy description button to the character card.
- [x] Unify styling of `ConfirmationModal.jsx` with the rest of the app (`App.jsx` as reference).
- [ ] Add relationships between characters (e.g., family, friends, rivals)
- [ ] Implement a way to generate character backstories or bios
- [ ] Add more attributes to characters (e.g., skills, flaws, goals)
- [x] Add `creation_date` to Character model and create migration `ef0f72190d66`

# Future Ideas

- Create a page that allows you to bulk generate characters with the same occupation. This would be useful if we want to create 50 farmers
  - [x] Add `POST /api/characters/bulk-generate` endpoint to backend.
  - [x] Add bulk generation form (Occupation, Count) to frontend (`App.jsx`).
  - [x] Implement `handleBulkCreate` function in frontend to call API and update state.

# TODO List

- [x] Setup Flask-SQLAlchemy and Flask-Migrate
- [x] Define Character and Event models
- [x] Create initial migration
- [x] Setup API blueprint
- [x] Implement basic CRUD endpoints for Character
- [x] Implement basic CRUD endpoints for Event
- [x] Add relationship between Character and Event
- [x] Update migrations for relationship
- [x] Update API endpoints to handle relationships
- [x] Add frontend structure (basic HTML/JS)
- [x] Fetch and display characters on frontend
- [x] Add form to create characters
- [x] Implement frontend character creation logic
- [x] Ensure DB tables are created on startup if they don't exist
