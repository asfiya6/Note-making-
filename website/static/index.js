// delete function of a note
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }), 
    }).then((_res) => {
      window.location.href = "/"; // reloading the window after deleting a note (refreshing the page)
    });
  }