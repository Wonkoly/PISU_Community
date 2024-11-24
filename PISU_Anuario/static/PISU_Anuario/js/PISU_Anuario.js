function openUploadModal() {
    const modal = new bootstrap.Modal(document.getElementById("imageModal"));
    modal.show();
}

function openImageModal(imageUrl, description, user) {
    // Establecer el contenido del modal
    document.getElementById('modalImage').src = imageUrl;
    document.getElementById('modalUser').innerText = `Subido por: ${user}`;
    document.getElementById('modalDescription').innerText = description;

    // Abrir el modal
    const modal = new bootstrap.Modal(document.getElementById('imageModal'));
    modal.show();
}

function deletePhoto(photoId) {
    // Aquí colocas el código para eliminar la foto.
    console.log("Eliminando foto con ID:", photoId);
}

// Eliminar foto
function deletePhoto() {
    const imageId = document.getElementById("deleteButton").getAttribute("data-id");
    alert(`Eliminar imagen con ID: ${imageId}`);
    // Aquí puedes implementar la lógica de eliminación usando AJAX o redirección.
}
