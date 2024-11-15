
# PDF Reader App

This is a web-based PDF Reader application built using Flask and JavaScript. The app allows users to upload a PDF file, view the extracted text content, and control text-to-speech playback. Users can also navigate through the pages of the PDF using provided controls.

## Features
- **Upload PDF**: Upload a PDF file to extract and display the text content.
- **Text-to-Speech (TTS)**: The app uses `pyttsx3` to read the PDF text aloud.
- **Playback Controls**: Play, pause, and navigate to the previous or next page of the PDF.
- **User-Friendly Interface**: The app has a clean and responsive design with a sidebar to display the extracted text.

## Technologies Used
- **Backend**: Flask, PyPDF2, pyttsx3
- **Frontend**: HTML, CSS, JavaScript
- **Additional Libraries**: 
  - `PyPDF2` for extracting text from PDF files.
  - `pyttsx3` for text-to-speech functionality.

## Setup and Installation
### Prerequisites
- Python (version 3.7 or higher)
- pip (Python package installer)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Chitti333/audiobook
   cd pdf-reader-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install Flask PyPDF2 pyttsx3
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your web browser and visit `http://127.0.0.1:5000` to use the app.

## Usage
1. **Upload a PDF**: Click the "Upload" button to select and upload a PDF file.
2. **View Text Content**: The extracted text will be displayed in the sidebar.
3. **Control Text-to-Speech**:
   - Click "Play" to start reading the text aloud.
   - Click "Pause" to stop the reading.
   - Use "Previous Page" and "Next Page" to navigate through the PDF.

## Project Structure
```
pdf-reader-app/
│
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML file for the frontend
├── static/
│   └── (optional)        # Static files (e.g., CSS, JS)
├── uploads/              # Directory for uploaded PDF files
└── README.md             # This README file
```

## Future Enhancements
- Add more advanced text-to-speech features, such as resuming from the paused point.
- Implement support for other file formats.
- Enhance the user interface with more styling and animations.

## Troubleshooting
- If the text-to-speech feature doesn’t resume correctly after pausing, it's a limitation of `pyttsx3`. Consider using a browser-based speech API for more control.
- Make sure you have installed all the dependencies using `pip install Flask PyPDF2 pyttsx3`.

## License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.

## Acknowledgments
- **Flask**: A micro web framework for Python.
- **PyPDF2**: A library for working with PDF files in Python.
- **pyttsx3**: A text-to-speech conversion library in Python.

