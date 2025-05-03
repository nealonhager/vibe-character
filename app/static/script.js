document.addEventListener("DOMContentLoaded", function () {
  const charactersTableBody = document
    .getElementById("characters-table")
    .querySelector("tbody");
  const createCharacterForm = document.getElementById("create-character-form");
  const messageArea = document.getElementById("message-area");
  const apiUrl = "/api/characters"; // Adjust if your API prefix is different

  // --- Edit Form elements ---
  const editFormContainer = document.getElementById("edit-form-container");
  const editCharacterForm = document.getElementById("edit-character-form");
  const editCharacterIdInput = document.getElementById("edit-character-id");
  // Identity
  const editNameInput = document.getElementById("edit-name");
  const editFamilyNameInput = document.getElementById("edit-family-name");
  const editTitleInput = document.getElementById("edit-title");
  // Lineage
  const editBirthDateInput = document.getElementById("edit-birth-date");
  const editBirthPlaceInput = document.getElementById("edit-birth-place");
  // Physical
  const editGenderSelect = document.getElementById("edit-gender");
  const editHeightInput = document.getElementById("edit-height");
  const editWeightInput = document.getElementById("edit-weight");
  const editBloodTypeSelect = document.getElementById("edit-blood-type");
  const editEyeColorSelect = document.getElementById("edit-eye-color");
  const editHairColorInput = document.getElementById("edit-hair-color");
  const editRaceSelect = document.getElementById("edit-race");
  const editBuildSelect = document.getElementById("edit-build");
  // Abilities
  const editStrengthInput = document.getElementById("edit-strength");
  const editEnduranceInput = document.getElementById("edit-endurance");
  const editDexterityInput = document.getElementById("edit-dexterity");
  const editConstitutionInput = document.getElementById("edit-constitution");
  const editIntelligenceInput = document.getElementById("edit-intelligence");
  const editWisdomInput = document.getElementById("edit-wisdom");
  const editCharismaInput = document.getElementById("edit-charisma");
  // Traits & Hobbies
  const editTraitsTextarea = document.getElementById("edit-traits");
  const editHobbiesTextarea = document.getElementById("edit-hobbies");
  // Other
  const editOccupationInput = document.getElementById("edit-occupation");
  const editPrimaryAddressTextarea = document.getElementById(
    "edit-primary-address",
  );

  const cancelEditBtn = document.getElementById("cancel-edit-btn");

  let currentCharacters = []; // Store fetched characters for easy lookup

  // --- Function to fetch and display characters ---
  async function fetchCharacters() {
    try {
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      currentCharacters = await response.json(); // Store characters

      charactersTableBody.innerHTML = ""; // Clear existing rows
      currentCharacters.forEach((character) => {
        const row = charactersTableBody.insertRow();
        // Display only a few key fields in the table
        row.innerHTML = `
                    <td>${character.id ? character.id.substring(0, 8) + "..." : "N/A"}</td>
                    <td>${character.name || "N/A"}</td>
                    <td>${character.family_name || "N/A"}</td>
                    <td>${character.gender || "N/A"}</td>
                    <td>
                        <button class="edit-btn" data-id="${character.id}">Edit</button>
                        <button class="delete-btn" data-id="${character.id}">Delete</button>
                    </td>
                `;
        // Add event listeners
        const deleteBtn = row.querySelector(".delete-btn");
        if (deleteBtn) {
          deleteBtn.addEventListener("click", () =>
            deleteCharacter(character.id),
          );
        }
        const editBtn = row.querySelector(".edit-btn");
        if (editBtn) {
          editBtn.addEventListener("click", () => showEditForm(character.id));
        }
      });
    } catch (error) {
      console.error("Error fetching characters:", error);
      messageArea.textContent = "Error fetching characters.";
      messageArea.style.color = "red";
    }
  }

  // Helper to safely set input value
  function safeSetValue(input, value) {
    if (input) {
      input.value = value !== null && value !== undefined ? value : "";
    }
  }

  // --- Function to show and populate the edit form ---
  function showEditForm(characterId) {
    const character = currentCharacters.find((c) => c.id === characterId);
    if (!character) {
      console.error("Character not found for editing:", characterId);
      messageArea.textContent = "Cannot edit: Character not found.";
      messageArea.style.color = "red";
      return;
    }

    // Populate the form
    safeSetValue(editCharacterIdInput, character.id);
    // Identity
    safeSetValue(editNameInput, character.name);
    safeSetValue(editFamilyNameInput, character.family_name);
    safeSetValue(editTitleInput, character.title); // Assumes schema returns title property
    // Lineage
    safeSetValue(editBirthDateInput, character.birth_date); // Assumes YYYY-MM-DD format
    safeSetValue(editBirthPlaceInput, character.birth_place);
    // Physical
    safeSetValue(editGenderSelect, character.gender);
    safeSetValue(editHeightInput, character.height);
    safeSetValue(editWeightInput, character.weight);
    safeSetValue(editBloodTypeSelect, character.blood_type);
    safeSetValue(editEyeColorSelect, character.eye_color);
    safeSetValue(editHairColorInput, character.hair_color); // Assumes schema returns hair_color property
    safeSetValue(editRaceSelect, character.race);
    safeSetValue(editBuildSelect, character.build);
    // Abilities
    safeSetValue(editStrengthInput, character.strength);
    safeSetValue(editEnduranceInput, character.endurance);
    safeSetValue(editDexterityInput, character.dexterity);
    safeSetValue(editConstitutionInput, character.constitution);
    safeSetValue(editIntelligenceInput, character.intelligence);
    safeSetValue(editWisdomInput, character.wisdom);
    safeSetValue(editCharismaInput, character.charisma);
    // Traits & Hobbies (convert array to comma-separated string)
    safeSetValue(
      editTraitsTextarea,
      Array.isArray(character.traits) ? character.traits.join(", ") : "",
    );
    safeSetValue(
      editHobbiesTextarea,
      Array.isArray(character.hobbies) ? character.hobbies.join(", ") : "",
    );
    // Other
    safeSetValue(editOccupationInput, character.occupation);
    safeSetValue(editPrimaryAddressTextarea, character.primary_address);

    // Show the form
    editFormContainer.style.display = "block";
    messageArea.textContent = "";
  }

  // --- Function to hide the edit form ---
  function hideEditForm() {
    editFormContainer.style.display = "none";
    editCharacterForm.reset();
  }

  // --- Event listener for canceling edit ---
  cancelEditBtn.addEventListener("click", hideEditForm);

  // --- Function to handle character creation ---
  createCharacterForm.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission
    messageArea.textContent = "Creating character...";
    messageArea.style.color = "black";

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({}), // Sending empty JSON body
      });

      if (!response.ok) {
        const errorData = await response
          .json()
          .catch(() => ({ detail: "Unknown error" }));
        throw new Error(
          `HTTP error! status: ${response.status}, message: ${errorData.detail || response.statusText}`,
        );
      }

      const newCharacter = await response.json();
      messageArea.textContent = `Character created successfully (ID: ${newCharacter.id})!`;
      messageArea.style.color = "green";
      fetchCharacters(); // Refresh the table
    } catch (error) {
      console.error("Error creating character:", error);
      messageArea.textContent = `Error creating character: ${error.message}`;
      messageArea.style.color = "red";
    }
  });

  // Helper to safely get value or null
  function getValueOrNull(input) {
    if (!input || input.value.trim() === "") {
      return null;
    }
    if (input.type === "number") {
      const num = parseFloat(input.value);
      return isNaN(num) ? null : num;
    }
    return input.value;
  }

  // Helper to get array from comma-separated string
  function getArrayFromCsv(input) {
    if (!input || input.value.trim() === "") {
      return []; // Return empty array instead of null for JSON fields
    }
    return input.value
      .split(",")
      .map((s) => s.trim())
      .filter((s) => s !== "");
  }

  // --- Function to handle character update (Edit form submission) ---
  editCharacterForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    const characterId = editCharacterIdInput.value;
    messageArea.textContent = `Updating character ${characterId}...`;
    messageArea.style.color = "black";

    // Collect data from all fields
    const updatedData = {
      // Identity
      name: getValueOrNull(editNameInput),
      family_name: getValueOrNull(editFamilyNameInput),
      title: getValueOrNull(editTitleInput),
      // Lineage
      birth_date: getValueOrNull(editBirthDateInput),
      birth_place: getValueOrNull(editBirthPlaceInput),
      // Physical
      gender: getValueOrNull(editGenderSelect),
      height: getValueOrNull(editHeightInput),
      weight: getValueOrNull(editWeightInput),
      blood_type: getValueOrNull(editBloodTypeSelect),
      eye_color: getValueOrNull(editEyeColorSelect),
      hair_color: getValueOrNull(editHairColorInput), // Send the string value
      race: getValueOrNull(editRaceSelect),
      build: getValueOrNull(editBuildSelect),
      // Abilities
      strength: getValueOrNull(editStrengthInput),
      endurance: getValueOrNull(editEnduranceInput),
      dexterity: getValueOrNull(editDexterityInput),
      constitution: getValueOrNull(editConstitutionInput),
      intelligence: getValueOrNull(editIntelligenceInput),
      wisdom: getValueOrNull(editWisdomInput),
      charisma: getValueOrNull(editCharismaInput),
      // Traits & Hobbies (convert CSV back to array)
      traits: getArrayFromCsv(editTraitsTextarea),
      hobbies: getArrayFromCsv(editHobbiesTextarea),
      // Other
      occupation: getValueOrNull(editOccupationInput),
      primary_address: getValueOrNull(editPrimaryAddressTextarea),
    };

    // Filter out null values if the backend expects only provided fields
    // Or keep nulls if the backend handles setting fields to null
    // For simplicity, let's send all fields, including nulls

    try {
      const response = await fetch(`${apiUrl}/${characterId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedData),
      });

      if (!response.ok) {
        const errorData = await response
          .json()
          .catch(() => ({ detail: "Unknown error during update" }));
        throw new Error(
          `HTTP error! status: ${response.status}, message: ${errorData.detail || response.statusText}`,
        );
      }

      const updatedCharacter = await response.json();
      messageArea.textContent = `Character ${updatedCharacter.id} updated successfully!`;
      messageArea.style.color = "green";
      hideEditForm();
      fetchCharacters(); // Refresh the table
    } catch (error) {
      console.error("Error updating character:", error);
      messageArea.textContent = `Error updating character: ${error.message}`;
      messageArea.style.color = "red";
    }
  });

  // --- Function to handle character deletion ---
  async function deleteCharacter(characterId) {
    if (!confirm(`Are you sure you want to delete character ${characterId}?`)) {
      return;
    }
    messageArea.textContent = `Deleting character ${characterId}...`;
    messageArea.style.color = "black";

    try {
      // IMPORTANT: Assumes a DELETE endpoint exists at /api/characters/<uuid:character_id>
      const response = await fetch(`${apiUrl}/${characterId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        const errorData = await response
          .json()
          .catch(() => ({ detail: "Unknown error during deletion" }));
        throw new Error(
          `HTTP error! status: ${response.status}, message: ${errorData.detail || response.statusText}`,
        );
      }

      const contentType = response.headers.get("content-type");
      if (contentType && contentType.indexOf("application/json") !== -1) {
        const result = await response.json();
        messageArea.textContent =
          result.message || `Character ${characterId} deleted successfully.`;
      } else {
        if (response.status === 204) {
          messageArea.textContent = `Character ${characterId} deleted successfully.`;
        } else {
          messageArea.textContent = `Character ${characterId} deleted, but received unexpected response format.`;
        }
      }
      messageArea.style.color = "green";
      fetchCharacters(); // Refresh the table
    } catch (error) {
      console.error("Error deleting character:", error);
      messageArea.textContent = `Error deleting character: ${error.message}`;
      messageArea.style.color = "red";
    }
  }

  // --- Initial fetch when the page loads ---
  fetchCharacters();
});
