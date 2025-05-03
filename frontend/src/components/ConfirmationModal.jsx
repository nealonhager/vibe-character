import React from "react";

// Reusable Confirmation Modal Component styled based on the provided image
function ConfirmationModal({
  isOpen,
  title = "Confirm Action",
  message,
  onConfirm,
  onCancel,
  confirmText = "Confirm",
  cancelText = "Cancel",
  isConfirming,
}) {
  if (!isOpen) return null;

  return (
    // Overlay: Light gray background with opacity
    <div
      className="fixed inset-0 bg-gray-500 bg-opacity-60 dark:bg-opacity-70 flex justify-center items-center z-50 p-4 transition-opacity duration-300 ease-in-out"
      onClick={onCancel}
    >
      {/* Modal Card: White background, large rounding, padding, shadow */}
      <div
        className="bg-white rounded-2xl shadow-xl w-full max-w-md p-8 transform transition-all duration-300 ease-in-out scale-95 opacity-0 animate-fade-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Title */}
        <h3 className="text-xl font-bold mb-3 text-gray-900">{title}</h3>
        {/* Message */}
        <p className="text-gray-600 mb-8 text-base">{message}</p>
        {/* Buttons Container */}
        <div className="flex justify-end space-x-4">
          {/* Cancel Button: Light gray style */}
          <button
            onClick={onCancel}
            disabled={isConfirming}
            className="px-6 py-3 bg-gray-100 text-gray-800 rounded-lg text-sm font-medium hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 disabled:opacity-60 disabled:cursor-not-allowed"
          >
            {cancelText}
          </button>
          {/* Confirm Button: Black style */}
          <button
            onClick={onConfirm}
            disabled={isConfirming}
            className="px-6 py-3 bg-gray-900 text-gray-100 rounded-lg text-sm font-medium" // Adjusted min-width for padding
          >
            {isConfirming ? (
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
              confirmText
            )}
          </button>
        </div>
      </div>
      {/* Animation remains the same */}
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

export default ConfirmationModal;
