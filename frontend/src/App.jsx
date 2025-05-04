import { useState, useEffect } from "react";
import ConfirmationModal from "./components/ConfirmationModal";
import CharacterDetailModal from "./components/CharacterDetailModal";
import CharacterEditModal from "./components/CharacterEditModal";

function App() {
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isCreating, setIsCreating] = useState(false);
  const [createError, setCreateError] = useState(null);
  const [deletingId, setDeletingId] = useState(null);
  const [deleteError, setDeleteError] = useState(null);

  const [isConfirmModalOpen, setIsConfirmModalOpen] = useState(false);
  const [characterToDelete, setCharacterToDelete] = useState(null);
  const [isConfirmingDelete, setIsConfirmingDelete] = useState(false);

  const [isViewModalOpen, setIsViewModalOpen] = useState(false);
  const [viewingCharacter, setViewingCharacter] = useState(null);

  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [editingCharacter, setEditingCharacter] = useState(null);
  const [isSaving, setIsSaving] = useState(false);
  const [editError, setEditError] = useState(null);
  const [copiedId, setCopiedId] = useState(null);

  const apiUrl = "/api/characters";

  useEffect(() => {
    async function fetchCharacters() {
      try {
        setLoading(true);
        setError(null);
        setDeleteError(null);
        setEditError(null);
        const response = await fetch(apiUrl);
        if (!response.ok) {
          let errorMsg = `HTTP error! status: ${response.status}`;
          try {
            const errData = await response.json();
            errorMsg =
              errData.message || errData.error || JSON.stringify(errData);
          } catch (parseErr) {
            // Ignore if response is not JSON
          }
          throw new Error(errorMsg);
        }
        const data = await response.json();
        setCharacters(data);
      } catch (err) {
        console.error("Error fetching characters:", err);
        setError(err.message);
        setCharacters([]);
      } finally {
        setLoading(false);
      }
    }

    fetchCharacters();
  }, [apiUrl]);

  const handleCreateCharacter = async () => {
    setIsCreating(true);
    setCreateError(null);
    setDeleteError(null);
    setEditError(null);
    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({}),
      });
      if (!response.ok) {
        let errorMsg = `HTTP error! status: ${response.status}`;
        try {
          const errData = await response.json();
          errorMsg =
            errData.message || errData.error || JSON.stringify(errData);
        } catch (parseErr) {
          // Ignore if response is not JSON
        }
        throw new Error(errorMsg);
      }
      const newCharacter = await response.json();
      setCharacters((prevChars) => [newCharacter, ...prevChars]);
    } catch (err) {
      console.error("Error creating character:", err);
      setCreateError(err.message);
    } finally {
      setIsCreating(false);
    }
  };

  const initiateDeleteCharacter = (characterId) => {
    setCharacterToDelete(characterId);
    setIsConfirmModalOpen(true);
    setDeleteError(null);
  };

  const confirmDeleteCharacter = async () => {
    if (!characterToDelete) return;

    setIsConfirmingDelete(true);
    setDeletingId(characterToDelete);
    setDeleteError(null);
    setEditError(null);

    try {
      const response = await fetch(`${apiUrl}/${characterToDelete}`, {
        method: "DELETE",
      });

      if (!response.ok && response.status !== 204) {
        let errorMsg = `HTTP error! status: ${response.status}`;
        try {
          const errData = await response.json();
          errorMsg =
            errData.message || errData.error || JSON.stringify(errData);
        } catch (parseErr) {
          errorMsg = response.statusText || errorMsg;
        }
        throw new Error(errorMsg);
      }

      setCharacters((prevChars) =>
        prevChars.filter((char) => char.id !== characterToDelete),
      );
      closeConfirmModal();
    } catch (err) {
      console.error("Error deleting character:", err);
      setDeleteError(
        `Failed to delete character ${characterToDelete.substring(0, 8)}...: ${err.message}`,
      );
      closeConfirmModal();
    } finally {
      setDeletingId(null);
      setIsConfirmingDelete(false);
    }
  };

  const closeConfirmModal = () => {
    setIsConfirmModalOpen(false);
    setCharacterToDelete(null);
    setIsConfirmingDelete(false);
  };

  const openViewModal = (characterId) => {
    const characterToView = characters.find((char) => char.id === characterId);
    if (characterToView) {
      setViewingCharacter(characterToView);
      setIsViewModalOpen(true);
    }
  };

  const closeViewModal = () => {
    setIsViewModalOpen(false);
    setViewingCharacter(null);
  };

  const openEditModal = (characterId) => {
    const characterToEdit = characters.find((char) => char.id === characterId);
    if (characterToEdit) {
      setEditingCharacter(characterToEdit);
      setEditError(null);
      setIsEditModalOpen(true);
    }
  };

  const closeEditModal = () => {
    setIsEditModalOpen(false);
    setEditingCharacter(null);
    setEditError(null);
  };

  const handleUpdateCharacter = async (characterId, updatedData) => {
    setIsSaving(true);
    setEditError(null);
    console.log("Saving data:", updatedData);
    try {
      const response = await fetch(`${apiUrl}/${characterId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedData),
      });

      if (!response.ok) {
        let errorMsg = `HTTP error! status: ${response.status}`;
        try {
          const errData = await response.json();
          errorMsg =
            errData.message ||
            errData.error ||
            JSON.stringify(errData.errors || errData);
        } catch (parseErr) {
          // Ignore if response is not JSON
        }
        throw new Error(errorMsg);
      }

      const savedCharacter = await response.json();
      setCharacters((prevChars) =>
        prevChars.map((char) =>
          char.id === characterId ? savedCharacter : char,
        ),
      );
      closeEditModal();
    } catch (err) {
      console.error("Error updating character:", err);
      setEditError(err.message);
    } finally {
      setIsSaving(false);
    }
  };

  const handleCopyDescription = async (character) => {
    if (!character || !character.physical_description) return;

    try {
      await navigator.clipboard.writeText(character.physical_description);
      setCopiedId(character.id);
      setTimeout(() => {
        setCopiedId(null);
      }, 2000);
    } catch (err) {
      console.error("Failed to copy text: ", err);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6 text-center">
        Character Manager (React)
      </h1>

      {error && (
        <p className="p-4 text-red-600 bg-red-100 border border-red-400 rounded mb-4">
          Error loading characters: {error}
        </p>
      )}
      {deleteError && (
        <p className="p-4 text-red-600 bg-red-100 border border-red-400 rounded mb-4">
          {deleteError}
        </p>
      )}
      {editError && (
        <p className="p-4 text-red-600 bg-red-100 border border-red-400 rounded mb-4">
          Error updating character: {editError}
        </p>
      )}

      <div className="mb-6 p-4 border rounded shadow bg-white">
        <h2 className="text-xl font-semibold mb-2">Create New Character</h2>
        <p className="text-sm text-gray-600 mb-3">
          Click the button to generate a new character with random attributes
          using the backend builder.
        </p>
        <button
          onClick={handleCreateCharacter}
          disabled={isCreating}
          className="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:bg-blue-300 disabled:cursor-not-allowed flex items-center"
        >
          {isCreating ? (
            <>
              <svg
                className="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
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
              Creating...
            </>
          ) : (
            "Create Random Character"
          )}
        </button>
        {createError && (
          <p className="text-red-500 mt-2">
            Error creating character: {createError}
          </p>
        )}
      </div>

      <div className="overflow-x-auto shadow border rounded">
        <h2 className="text-xl font-semibold mb-0 p-4 bg-gray-100 border-b">
          Characters
        </h2>
        {loading && (
          <p className="p-4 text-center text-gray-500">Loading characters...</p>
        )}
        {!loading && !error && (
          <table className="min-w-full bg-white">
            <thead className="bg-gray-100">
              <tr>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  ID
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Name
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Family Name
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Gender
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Age
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Race
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Birth Place
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Occupation
                </th>
                <th className="py-2 px-4 border-b text-left text-sm font-medium text-gray-600 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {characters.length > 0 ? (
                characters.map((char) => (
                  <tr
                    key={char.id}
                    className={`hover:bg-gray-50 ${deletingId === char.id || editingCharacter?.id === char.id ? "opacity-50" : ""}`}
                  >
                    <td
                      className="py-2 px-4 border-b text-xs text-gray-700 font-mono"
                      title={char.id}
                    >
                      {char.id?.substring(0, 8)}...
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.name || "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.family_name || "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.gender || "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.birth_date
                        ? (() => {
                            try {
                              const birthDate = new Date(char.birth_date);
                              const today = new Date();
                              let age =
                                today.getFullYear() - birthDate.getFullYear();
                              const m = today.getMonth() - birthDate.getMonth();
                              if (
                                m < 0 ||
                                (m === 0 &&
                                  today.getDate() < birthDate.getDate())
                              ) {
                                age--;
                              }
                              return age;
                            } catch (e) {
                              return "N/A"; // Handle invalid date format
                            }
                          })()
                        : "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.race || "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.birth_place || "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm text-gray-900">
                      {char.occupation || "N/A"}
                    </td>
                    <td className="py-2 px-4 border-b text-sm whitespace-nowrap">
                      <button
                        onClick={() => openViewModal(char.id)}
                        disabled={
                          deletingId === char.id ||
                          editingCharacter?.id === char.id
                        }
                        className="px-2 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 mr-1 text-xs font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                      >
                        View
                      </button>
                      <button
                        onClick={() => openEditModal(char.id)}
                        disabled={
                          deletingId === char.id ||
                          editingCharacter?.id === char.id ||
                          viewingCharacter?.id === char.id
                        }
                        className="px-2 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600 mr-1 text-xs font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => handleCopyDescription(char)}
                        disabled={
                          deletingId === char.id ||
                          editingCharacter?.id === char.id ||
                          viewingCharacter?.id === char.id ||
                          copiedId === char.id
                        }
                        className={`px-2 py-1 rounded mr-1 text-xs font-medium disabled:opacity-50 disabled:cursor-not-allowed ${copiedId === char.id ? "bg-green-500 text-white" : "bg-gray-500 text-white hover:bg-gray-600"}`}
                      >
                        {copiedId === char.id ? "Copied!" : "Copy Desc"}
                      </button>
                      <button
                        onClick={() => initiateDeleteCharacter(char.id)}
                        disabled={
                          deletingId === char.id ||
                          editingCharacter?.id === char.id ||
                          viewingCharacter?.id === char.id
                        }
                        className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600 text-xs font-medium disabled:bg-red-300 disabled:cursor-not-allowed flex items-center justify-center min-w-[60px]"
                      >
                        {deletingId === char.id ? (
                          <svg
                            className="animate-spin h-4 w-4 text-white"
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
                          "Delete"
                        )}
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  {!error && (
                    <td
                      colSpan="9"
                      className="py-4 px-4 text-center text-gray-500"
                    >
                      No characters found. Create one above!
                    </td>
                  )}
                </tr>
              )}
            </tbody>
          </table>
        )}
      </div>

      <ConfirmationModal
        isOpen={isConfirmModalOpen}
        message={`Are you sure you want to delete character ${characterToDelete?.substring(0, 8)}...? This action cannot be undone.`}
        onConfirm={confirmDeleteCharacter}
        onCancel={closeConfirmModal}
        isConfirming={isConfirmingDelete}
        confirmText="Delete"
        title="Confirm Deletion"
      />

      <CharacterDetailModal
        isOpen={isViewModalOpen}
        character={viewingCharacter}
        onClose={closeViewModal}
      />

      <CharacterEditModal
        isOpen={isEditModalOpen}
        character={editingCharacter}
        onClose={closeEditModal}
        onSave={handleUpdateCharacter}
        isSaving={isSaving}
      />
    </div>
  );
}

export default App;
