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
      className="fixed inset-0 bg-gray-500 bg-opacity-60 dark:bg-gray-900 dark:bg-opacity-70 flex justify-center items-center z-50 p-4 transition-opacity duration-300 ease-in-out"
      onClick={onCancel}
    >
      {/* Modal Card: White background, moderate rounding, padding, shadow, dark mode support */}
      <div
        className="bg-white dark:bg-gray-800 rounded-lg shadow-xl w-full max-w-md p-6 transform transition-all duration-300 ease-in-out scale-95 opacity-0 animate-fade-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Title */}
        <h3 className="text-lg font-semibold mb-4 text-gray-900 dark:text-gray-100">
          {title}
        </h3>
        {/* Message */}
        <p className="text-gray-600 dark:text-gray-300 mb-6 text-sm">
          {message}
        </p>
        {/* Buttons Container */}
        <div className="flex justify-end space-x-3">
          {/* Cancel Button: Similar to App's secondary buttons */}
          <button
            onClick={onCancel}
            disabled={isConfirming}
            className="px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 rounded-md text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 dark:focus:ring-offset-gray-800 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {cancelText}
          </button>
          {/* Confirm Button: Similar to App's primary buttons */}
          <button
            onClick={onConfirm}
            disabled={isConfirming}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center min-w-[80px]" // Added min-width for spinner consistency
          >
            {isConfirming ? (
              <svg
                className="animate-spin h-4 w-4 text-white" // Adjusted size
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
