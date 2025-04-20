# ----- required imports -----

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import cv2
import numpy as np
import os
import uuid

# ----- intialization code -----

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'panels'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ----- helper functions -----

def detect_panels(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    panels = []
    for cnt in contours:
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)
            panels.append((x, y, x+w, y+h))
    panels.sort(key=lambda rect: (rect[2]-rect[0])*(rect[3]-rect[1]), reverse=True)
    return image, panels

# ----- endpoints -----

@app.route('/api/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    filename = str(uuid.uuid4()) + '.png'
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(upload_path)
    original, panels = detect_panels(upload_path)
    output_files = []
    for i, (x1, y1, x2, y2) in enumerate(panels[:15]):  
        panel = original[y1:y2, x1:x2]
        panel_filename = f'panel_{i+1}_{filename}'
        output_path = os.path.join(OUTPUT_FOLDER, panel_filename)
        cv2.imwrite(output_path, panel)
        output_files.append(panel_filename)
    return jsonify({'panels': output_files})

@app.route('/panels/<filename>')
def get_panel(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

# ----- execution code -----

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)