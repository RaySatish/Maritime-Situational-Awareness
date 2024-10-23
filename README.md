# Maritime-Situational-Awareness
Scan and analyse textual maritime reports, extract details about potential contacts and plot these identified contacts on a radar/map

Problem Statement: Textual Intelligence for Maritime Situational Awareness

Challenge:

Develop a software solution that uses OCR (Optical Character Recognition) combined with Retrieval-Augmented Generation (RAG) to scan and analyse textual maritime reports (such as surveillance logs, reconnaissance notes or communication messages) and extract details about potential contacts (ships, submarines, aircraft or other entities). The software should then plot these identified contacts on a radar/map interface to provide naval personnel with real-time situational awareness.

Objectives:

Text Extraction.     Use OCR to scan handwritten or printed reports, extracting relevant information about geographical coordinates, headings, speeds and types of vessels or objects detected.

RAG for Information Retrieval.     Implement an API based RAG model that intelligently extracts and structures information such as locations, time of sighting and object descriptions from the scanned text. It should cross-reference the reports with existing databases or contextual information (e.g. previous sightings or known entities).

Contact Mapping.   Use the extracted data to plot contacts (ships, submarines, aircraft or other objects) on a radar-style or map-based interface. The map should update dynamically as new reports are scanned and processed.

User Interface.     Develop a user-friendly interface that displays the radar/map, allowing naval officers to see the plotted contacts with additional metadata (e.g. speed, direction, type of vessel, time of report).

Automated Alerts.     If potential threats are identified (e.g. an unidentified object or a vessel in restricted waters), the system should trigger alerts for naval operators.

Bonus Features

Historical Report Integration.     Allow users to scan historical reports and compare movements of the same contact over time to predict future behavior.

Speech-to-Text.   Extend the software to transcribe spoken reports into text (e.g. from radio communications) and process them in a similar manner.

Deliverables:

Codebase: A working implementation of the solution iro problem statement. The code should be well-documented and capable of running on typical hardware.

Technical Documentation: Detailed documentation explaining the methodology, algorithms used, and the steps taken to achieve the solution.

Performance Metrics: Quantitative analysis showing the accuracy, robustness, and computational efficiency of the solution different test scenarios.

Judging Criteria

Expected features

Text Parsing.     The software should intelligently parse sentences like "At 05.30 UTC, an unidentified vessel was sighted at latitude 12.34 N, longitude 45.67 E, moving at 12 knots towards the northeast."

Real-time Updating.  As new reports are scanned and processed, the system updates the radar/map interface in real-time, showing the latest positions and statuses of the identified contacts. It should update a contact position if previously reported.

Visualization.    The plotted contacts should include details like type (e.g. cargo ship, patrol boat), current location, direction, time of detection, MLA and speed. It should offer options to zoom in/out and filter based on threat level or type of object.

Accuracy

Performance

Documentation: Clarity and thoroughness of the technical documentation.

Tools/Tech Stack

OCR.  Tesseract OCR or equivalent offline toll to convert printed/handwritten reports into digital text.
RAG.     Hugging Face's RAG model (or similar) to retrieve relevant context from the extracted text and generate structured data (such as coordinates, speed, and vessel type).
Map Visualization.     Leaflet.js or equivalent software to create the map interface, D3.js for radar visualization.
Backend.      Python (Flask/Django), FastAPI for API creation.
