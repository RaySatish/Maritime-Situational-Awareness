# Maritime-Situational-Awareness

A web-based application that analyzes maritime reports using Optical Character Recognition (OCR) and Natural Language Processing (NLP) techniques to extract relevant information.

Table of Contents

1. About
2. Features
3. Requirements
4. Installation
5. Usage
6. Authors

About  
The Maritime Situational Awareness is designed to analyse maritime reports using OCR and NLP techniques. The system consists of four main components:

- Frontend : A user-friendly interface that allows users to upload maritime reports, view Google Maps with vessel locations, and receive alerts.
- OCR Service : Responsible for converting uploaded image, files (e.g., maritime reports) to text.
- RAG Model API : Implements a Recognising Active Graphs model to extract information from scanned text and cross-reference it with existing databases or contextual information.
- Backend: Flask is a lightweight, customizable Python web framework that serves as the backend foundation, enabling rapid development and easy integration with services like OCR and RAG Model APIs. Its modular structure organizes routes and services, supporting scalable and maintainable applications.

Features

- Upload and analyse maritime reports using OCR and NLP techniques
- View Google Maps with vessel locations and receive alerts
- Extract relevant information from uploaded reports, including location, time of sighting, and object descriptions
- Cross-reference extracted information with existing databases or contextual information
- Provide an intuitive web interface for data interaction and alerts

Installation

- Clone the repository

  - git clone https://github.com/RaySatish/Maritime-Situational-Awareness.git
  - cd Maritime-Situational-Awareness

- Set Up Virtual Environment (Recommended)

  - Create a virtual environment
    - python3 -m venv venv
  - Activate the virtual environment
    - On macOS:
      - source venv/bin/activate
    - On Windows:
      - venv\Scripts\activate

- Install PostgreSQL

  - On macOS
    - brew install postgresql (with Homebrew package manager)
  - On Windows
    - Download the installer from the official website

- Install necessary python librarires
  - pip install -r requirements.txt

Requirements

- Python 3.8+
- Flask for backend development
- PostgreSQL for database management
- Tesseract-OCR for OCR functionality
- Natural Language Processing libraries (e.g., pydub, speech_recongnition)
- Retrieval Augmented Generation with Hugging Face
- Check "requirements.txt" for installing necessary python libraries

Usage  
To use the system, follow these steps:

1. Upload a maritime report using the frontend interface
2. Click on the "Upload" button to view the vessel location with a pin and receive alerts
3. Click on the pin to view additional information about the vessel

Authors

1. Satish Prem Anand (ray.satish10090@gmail.com)
2. N Hari Sai Vignesh (comradev73@gmail.com)
3. Parth Ranjan Mishra (parthranjanmishra4@gmail.com)
4. Ankit Pandey (pandeyankit7178@gmail.com)
5. Shshank Singh (shshanksingh2003@gmail.com)
