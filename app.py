import os
from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

bucket_name = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files[]')

    # Print filenames for debugging
    print(f"Number of files received: {len(files)}")
    for i, file in enumerate(files):
        print(f"Received file {i + 1}: {file.filename}")

    # Upload each file to Google Cloud Storage
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    for i, file in enumerate(files):
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)

    return 'Files uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
