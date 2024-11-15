from flask import Flask, request, render_template, jsonify
import os
import pyttsx3
import PyPDF2

app = Flask(__name__)
speaker = pyttsx3.init()

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Global variables to manage text and pages
pdf_text = []
current_page = 0
is_paused = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global pdf_text, current_page
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files['pdf']
    if pdf_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
    pdf_file.save(file_path)

    # Read and extract text from the PDF
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_text = [page.extract_text() for page in pdf_reader.pages]
        current_page = 0

    return jsonify({"text": " ".join(pdf_text)}), 200

@app.route('/play')
def play():
    global is_paused
    if not pdf_text:
        return "No text available to play", 400

    is_paused = False
    # Speak the text from the current page
    speaker.say(pdf_text[current_page])
    speaker.runAndWait()
    return "Playing text!", 200

@app.route('/pause')
def pause():
    global is_paused
    is_paused = True
    speaker.stop()  # Stops the speech
    return "Text paused!", 200

@app.route('/next_page')
def next_page():
    global current_page
    if current_page < len(pdf_text) - 1:
        current_page += 1
    return f"Moved to page {current_page + 1}!", 200

@app.route('/previous_page')
def previous_page():
    global current_page
    if current_page > 0:
        current_page -= 1
    return f"Moved to page {current_page + 1}!", 200

if __name__ == '__main__':
    app.run(debug=True)
