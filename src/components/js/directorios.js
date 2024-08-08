const directories = [
    "Directorio 1/",
    "Directorio 2/",
    "Directorio 3/",
    "Directorio 4/"
];

const files = {
    "Directorio 1/": ["Documento 1", "Documento 2"],
    "Directorio 2/": ["Documento 3"],
    "Directorio 3/": ["Documento 4", "Documento 5"],
    "Directorio 4/": ["Documento 6", "Documento 7"]
};

const directoryContainer = document.getElementById('directories');
const fileContainer = document.getElementById('files');
// let selectedDirectory = null;

function loadDirectories() {
    directoryContainer.innerHTML = '';
    directories.forEach(directory => {
        const div = document.createElement('div');
        div.className = 'directory';
        div.textContent = directory;
        div.onclick = () => selectDirectory(directory);
        directoryContainer.appendChild(div);
    });
}

function loadFiles(directory) {
    fileContainer.innerHTML = '';
    if (files[directory]) {
        files[directory].forEach(file => {
            const div = document.createElement('div');
            div.className = 'file';
            div.textContent = file;
            fileContainer.appendChild(div);
        });
    }
}

function selectDirectory(directory) {
    const previousSelection = document.querySelector('.directory.selected');
    if (previousSelection) {
        previousSelection.classList.remove('selected');
    }
    const currentSelection = Array.from(directoryContainer.children).find(
        child => child.textContent === directory
    );
    if (currentSelection) {
        currentSelection.classList.add('selected');
    }
    loadFiles(directory);
}

// function showFileContent() {
//     const filePath = filePathInput.value;
//     if (selectedDirectory && filePath) {
//         const fullPath = selectedDirectory + filePath;
//         fileContentContainer.innerHTML = `Contenido del archivo: ${fullPath}`;
//     } else {
//         fileContentContainer.innerHTML = 'Por favor, seleccione un directorio y ingrese la ruta del archivo.';
//     }
// }

// Cargar directorios al cargar la página
loadDirectories();