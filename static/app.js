/**
 * To-Do App - Client-side JavaScript
 * Handles auto-submit for checkboxes and other UI enhancements.
 */

document.addEventListener("DOMContentLoaded", function () {
  // Auto-hide flash messages after 3 seconds
  const flashMessages = document.querySelectorAll(".flash");
  flashMessages.forEach(function (flash) {
    setTimeout(function () {
      flash.style.transition = "opacity 0.5s";
      flash.style.opacity = "0";
      setTimeout(function () {
        flash.remove();
      }, 500);
    }, 3000);
  });

  // Confirm before deleting a task
  const deleteForms = document.querySelectorAll(".delete-form");
  deleteForms.forEach(function (form) {
    form.addEventListener("submit", function (e) {
      if (!confirm("Are you sure you want to delete this task?")) {
        e.preventDefault();
      }
    });
  });
});
