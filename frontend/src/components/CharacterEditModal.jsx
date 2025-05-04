import React, { useState, useEffect, useCallback } from "react";

// Helper to format labels (same as Detail Modal)
const formatLabel = (key) => {
  return key.replace(/_/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());
};

// Helper to get value or empty string for controlled inputs
const getValue = (value) =>
  value === null || value === undefined ? "" : value;

function CharacterEditModal({ isOpen, character, onClose, onSave, isSaving }) {
  const [formData, setFormData] = useState({});

  // Initialize form data when the character prop changes or modal opens
  useEffect(() => {
    if (character) {
      // Initialize form with character data, handling potential null/undefined
      const initialData = {};
      for (const key in character) {
        initialData[key] = getValue(character[key]);
      }
      // Convert arrays to CSV for textareas
      initialData.traits = Array.isArray(initialData.traits)
        ? initialData.traits.join(", ")
        : "";
      initialData.hobbies = Array.isArray(initialData.hobbies)
        ? initialData.hobbies.join(", ")
        : "";
      setFormData(initialData);
    } else {
      setFormData({}); // Clear form if no character
    }
  }, [character, isOpen]); // Depend on character and isOpen

  const handleChange = useCallback((e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === "checkbox" ? checked : value,
    }));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Convert CSV strings back to arrays for traits/hobbies
    const dataToSave = {
      ...formData,
      traits: formData.traits
        ? formData.traits
            .split(",")
            .map((s) => s.trim())
            .filter((s) => s)
        : [],
      hobbies: formData.hobbies
        ? formData.hobbies
            .split(",")
            .map((s) => s.trim())
            .filter((s) => s)
        : [],
      // Convert numerical fields back to numbers, handle potential NaN
      height: formData.height !== "" ? Number(formData.height) || null : null,
      weight: formData.weight !== "" ? Number(formData.weight) || null : null,
      strength:
        formData.strength !== "" ? Number(formData.strength) || null : null,
      endurance:
        formData.endurance !== "" ? Number(formData.endurance) || null : null,
      dexterity:
        formData.dexterity !== "" ? Number(formData.dexterity) || null : null,
      constitution:
        formData.constitution !== ""
          ? Number(formData.constitution) || null
          : null,
      intelligence:
        formData.intelligence !== ""
          ? Number(formData.intelligence) || null
          : null,
      wisdom: formData.wisdom !== "" ? Number(formData.wisdom) || null : null,
      charisma:
        formData.charisma !== "" ? Number(formData.charisma) || null : null,
    };
    // Remove fields that shouldn't be updated or aren't handled by this form
    delete dataToSave.id;
    delete dataToSave.mother_id; // Exclude mother_id
    delete dataToSave.father_id; // Exclude father_id

    onSave(character.id, dataToSave); // Pass ID and processed data
  };

  if (!isOpen || !character) return null;

  // Define field groups and input types (similar to HTML form)
  // TODO: Refine input types (selects for enums, number constraints etc.)
  const fieldGroups = {
    Identity: ["name", "family_name", "title"],
    Lineage: ["birth_date", "birth_place"],
    Physical: [
      "gender",
      "height",
      "weight",
      "blood_type",
      "eye_color",
      "hair_color",
      "race",
      "build",
    ],
    Abilities: [
      "strength",
      "endurance",
      "dexterity",
      "constitution",
      "intelligence",
      "wisdom",
      "charisma",
    ],
    "Traits & Hobbies": ["traits", "hobbies"],
    Other: ["occupation", "primary_address"],
  };

  // Basic input type mapping (can be expanded)
  const getInputType = (field) => {
    if (field === "birth_date") return "date";
    if (
      [
        "height",
        "weight",
        "strength",
        "endurance",
        "dexterity",
        "constitution",
        "intelligence",
        "wisdom",
        "charisma",
      ].includes(field)
    )
      return "number";
    if (["traits", "hobbies", "primary_address"].includes(field))
      return "textarea";
    // TODO: Add select for gender, blood_type, eye_color, race, build based on enums/options
    return "text";
  };

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-60 flex justify-center items-center z-50 p-4 transition-opacity duration-300 ease-in-out"
      onClick={onClose} // Allow closing by clicking overlay
    >
      <div
        className="bg-white dark:bg-gray-800 rounded-lg shadow-xl w-full max-w-3xl max-h-[90vh] overflow-y-auto p-6 transform transition-all duration-300 ease-in-out scale-95 opacity-0 animate-fade-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        <form onSubmit={handleSubmit}>
          <div className="flex justify-between items-center mb-5 pb-3 border-b dark:border-gray-600">
            <h2 className="text-2xl font-semibold text-gray-800 dark:text-gray-100">
              Edit Character: {character.name} {character.family_name}
            </h2>
            <button
              type="button"
              onClick={onClose}
              className="text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 text-2xl"
            >
              &times;
            </button>
          </div>

          {/* Form Fields */}
          <div className="space-y-6">
            {Object.entries(fieldGroups).map(([groupName, fields]) => (
              <div key={groupName}>
                <h3 className="text-lg font-medium text-gray-700 dark:text-gray-300 mb-3 capitalize">
                  {groupName}
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-4 text-sm">
                  {fields
                    .filter((field) => formData.hasOwnProperty(field)) // Only show fields present in form data
                    .map((field) => {
                      const inputType = getInputType(field);
                      const label = formatLabel(field);
                      const commonInputClass =
                        "mt-1 block w-full px-3 py-2 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-sm shadow-sm placeholder-gray-400 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 disabled:bg-gray-50 disabled:text-gray-500 disabled:border-gray-200 disabled:shadow-none dark:text-gray-100";

                      return (
                        <div key={field}>
                          <label
                            htmlFor={field}
                            className="block text-sm font-medium text-gray-700 dark:text-gray-300"
                          >
                            {label}
                          </label>
                          {inputType === "textarea" ? (
                            <textarea
                              id={field}
                              name={field}
                              value={formData[field]}
                              onChange={handleChange}
                              rows="3"
                              className={commonInputClass}
                            />
                          ) : (
                            <input
                              type={inputType}
                              id={field}
                              name={field}
                              value={formData[field]}
                              onChange={handleChange}
                              min={inputType === "number" ? "0" : undefined} // Basic min for numbers
                              className={commonInputClass}
                            />
                          )}
                          {/* TODO: Add dropdowns (select) here based on field name */}
                        </div>
                      );
                    })}
                </div>
              </div>
            ))}
          </div>

          {/* Action Buttons */}
          <div className="mt-8 pt-5 border-t dark:border-gray-600 flex justify-end space-x-3">
            <button
              type="button" // Important: type="button" to prevent form submission
              onClick={onClose}
              disabled={isSaving}
              className="px-5 py-2 bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200 rounded-md text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50 disabled:opacity-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isSaving}
              className="px-5 py-2 bg-green-600 text-white rounded-md text-sm font-medium hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 disabled:bg-green-400 disabled:cursor-wait flex items-center justify-center min-w-[120px]"
            >
              {isSaving ? (
                <svg
                  className="animate-spin h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  ></circle>
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                  ></path>
                </svg>
              ) : (
                "Save Changes"
              )}
            </button>
          </div>
        </form>
      </div>
      {/* Animation */}
      <style jsx global>{`
        @keyframes fade-scale-in {
          from {
            opacity: 0;
            transform: scale(0.95);
          }
          to {
            opacity: 1;
            transform: scale(1);
          }
        }
        .animate-fade-scale-in {
          animation: fade-scale-in 0.2s ease-out forwards;
        }
      `}</style>
    </div>
  );
}

export default CharacterEditModal;
