import React from "react";

// Helper to format labels (e.g., family_name -> Family Name)
const formatLabel = (key) => {
  return key
    .replace(/_/g, " ") // Replace underscores with spaces
    .replace(/\b\w/g, (char) => char.toUpperCase()); // Capitalize first letter of each word
};

// Helper to display value or placeholder
const displayValue = (value) => {
  if (value === null || value === undefined || value === "") {
    return <span className="text-gray-400 italic">N/A</span>;
  }
  if (Array.isArray(value)) {
    return value.length > 0 ? (
      value.join(", ")
    ) : (
      <span className="text-gray-400 italic">None</span>
    );
  }
  // Basic date detection (improve if specific format needed)
  if (typeof value === "string" && value.match(/^\d{4}-\d{2}-\d{2}/)) {
    try {
      return new Date(value + "T00:00:00").toLocaleDateString(); // Adjust based on how dates are stored/expected
    } catch (e) {
      return value; // Fallback to string if date parsing fails
    }
  }
  return String(value);
};

function CharacterDetailModal({ isOpen, character, onClose }) {
  if (!isOpen || !character) return null;

  // Define the order and grouping of fields
  const fieldGroups = {
    Identity: ["id", "name", "family_name", "title"],
    Lineage: [
      "birth_date",
      "birth_place" /* 'mother_id', 'father_id' - Exclude for now */,
    ],
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
    "Traits & Hobbies": ["traits", "hobbies"], // Use string literal for key with space
    Other: ["occupation", "primary_address"],
  };

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-60 flex justify-center items-center z-50 p-4 transition-opacity duration-300 ease-in-out"
      onClick={onClose}
    >
      <div
        className="bg-white dark:bg-gray-800 rounded-lg shadow-xl w-full max-w-2xl max-h-[85vh] overflow-y-auto p-6 transform transition-all duration-300 ease-in-out scale-95 opacity-0 animate-fade-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex justify-between items-center mb-4 pb-3 border-b dark:border-gray-600">
          <h2 className="text-2xl font-semibold text-gray-800 dark:text-gray-100">
            Character Details
          </h2>
          <button
            onClick={onClose}
            className="text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 text-2xl"
          >
            &times;
          </button>
        </div>

        <div className="space-y-6">
          {Object.entries(fieldGroups).map(([groupName, fields]) => (
            <div key={groupName}>
              <h3 className="text-lg font-medium text-gray-700 dark:text-gray-300 mb-3">
                {groupName}
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-3 text-sm">
                {fields
                  .filter((field) => character.hasOwnProperty(field)) // Only show fields present in the character object
                  .map((field) => (
                    <div
                      key={field}
                      className="flex justify-between border-b border-gray-200 dark:border-gray-700 py-1.5"
                    >
                      <span className="font-medium text-gray-600 dark:text-gray-400">
                        {formatLabel(field)}:
                      </span>
                      <span className="text-gray-800 dark:text-gray-200 text-right">
                        {displayValue(character[field])}
                      </span>
                    </div>
                  ))}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-6 pt-4 border-t dark:border-gray-600 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200 rounded-md text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50"
          >
            Close
          </button>
        </div>
      </div>
      {/* Animation (same as ConfirmationModal) */}
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

export default CharacterDetailModal;
