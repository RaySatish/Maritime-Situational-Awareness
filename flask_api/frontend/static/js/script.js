document.getElementById('selectImageBtn').onclick = function() {
    document.getElementById('imageInput').click();
};

document.getElementById('imageInput').onchange = function() {
    const imageResult = document.getElementById('imageResult');
    const file = this.files[0];
    if (file) {
        imageResult.innerHTML = "Selected image: " + file.name;
        processImage(); // Call image processing function if needed
    } else {
        imageResult.innerHTML = "No image selected.";
    }
};

document.getElementById('selectAudioBtn').onclick = function() {
    document.getElementById('speechInput').click();
};

document.getElementById('speechInput').onchange = function() {
    const speechResult = document.getElementById('speechResult');
    const file = this.files[0];
    if (file) {
        speechResult.innerHTML = "Selected audio: " + file.name;
        processSpeech(); // Call speech processing function if needed
    } else {
        speechResult.innerHTML = "No audio selected.";
    }
};

function processImage() {
    const imageResult = document.getElementById('imageResult');
    // Placeholder for image processing logic
    imageResult.innerHTML += "<br>Image processed. Text extracted: [Placeholder text]";
}

function processSpeech() {
    const speechResult = document.getElementById('speechResult');
    // Placeholder for speech processing logic
    speechResult.innerHTML += "<br>Speech processed. Text extracted: [Placeholder text]";
}

function uploadFile() {
    const imageInput = document.getElementById('imageInput');
    const speechInput = document.getElementById('speechInput');
    const uploadResult = document.getElementById('uploadResult');

    let fileName = '';

    // Check which input is visible and process the corresponding file
    if (imageInput.files.length > 0) {
        fileName = imageInput.files[0].name;
        uploadResult.innerHTML = "File uploaded: " + fileName + " (Image)";
    } else if (speechInput.files.length > 0) {
        fileName = speechInput.files[0].name;
        uploadResult.innerHTML = "File uploaded: " + fileName + " (Speech)";
    } else {
        uploadResult.innerHTML = "No file selected.";
    }

    // Redirect to a new page after processing/upload
    window.location.href = "/map"; // Replace with the actual URL of the new page
}