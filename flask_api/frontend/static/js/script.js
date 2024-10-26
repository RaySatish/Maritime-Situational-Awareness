document.getElementById("selectImageBtn").onclick = function () {
	document.getElementById("imageInput").click();
};

document.getElementById("imageInput").onchange = function () {
	const imageResult = document.getElementById("imageResult");
	const file = this.files[0];
	if (file) {
		imageResult.innerHTML = "Selected image: " + file.name;
		processImage(); // Call image processing function if needed
	} else {
		imageResult.innerHTML = "No image selected.";
	}
};

document.getElementById("selectAudioBtn").onclick = function () {
	document.getElementById("speechInput").click();
};

document.getElementById("speechInput").onchange = function () {
	const speechResult = document.getElementById("speechResult");
	const file = this.files[0];
	if (file) {
		speechResult.innerHTML = "Selected audio: " + file.name;
		processSpeech(); // Call speech processing function if needed
	} else {
		speechResult.innerHTML = "No audio selected.";
	}
};
// Function to display the transcription result for images
function displayImageTranscription(text) {
	const imageTranscription = document.getElementById("imageTranscription");
	imageTranscription.value = text; // Display the transcribed text in the image textarea
}

// Function to display the transcription result for audio
function displayAudioTranscription(text) {
	const audioTranscription = document.getElementById("audioTranscription");
	audioTranscription.value = text; // Display the transcribed text in the audio textarea
}

// Function to process image files and call the backend for OCR
function processImage() {
	const imageResult = document.getElementById("imageResult");
	const file = document.getElementById("imageInput").files[0];

	if (file) {
		const formData = new FormData();
		formData.append("file", file);

		// Call backend to perform OCR
		fetch("/process_image", {
			method: "POST",
			body: formData,
		})
			.then((response) => response.json())
			.then((data) => {
				if (data.text) {
					displayImageTranscription(data.text);
					imageResult.innerHTML = "Image processed successfully.";
				} else {
					imageResult.innerHTML = "Error processing image.";
				}
			})
			.catch((error) => {
				console.error("Error:", error);
				imageResult.innerHTML = "Error processing image.";
			});
	} else {
		imageResult.innerHTML = "No image selected.";
	}
}

// Function to process audio files and call the backend for transcription
function processSpeech() {
	const speechResult = document.getElementById("speechResult");
	const file = document.getElementById("speechInput").files[0];

	if (file) {
		const formData = new FormData();
		formData.append("file", file);

		// Call backend to perform speech-to-text
		fetch("/process_audio", {
			method: "POST",
			body: formData,
		})
			.then((response) => response.json())
			.then((data) => {
				if (data.text) {
					displayAudioTranscription(data.text);
					speechResult.innerHTML = "Audio processed successfully.";
				} else {
					speechResult.innerHTML = "Error processing audio.";
				}
			})
			.catch((error) => {
				console.error("Error:", error);
				speechResult.innerHTML = "Error processing audio.";
			});
	} else {
		speechResult.innerHTML = "No audio selected.";
	}
}

function uploadFile() {
	const imageInput = document.getElementById("imageInput");
	const speechInput = document.getElementById("speechInput");
	const uploadResult = document.getElementById("uploadResult");

	let fileName = "";

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
	window.location.href = "../templates/Map.html";
}
