from flask import Flask, request, json


import os
from os.path import splitext
import secrets


storage_folder = 'STORAGE FOLDER'
secret_key = 'SECRET'


app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if request.form.to_dict(flat=False)['secret_key'][0] == secret_key:
            file = request.files['image']
            extension = splitext(file.filename)[1]
            filename = secrets.token_urlsafe(5)
            file.save(os.path.join(storage_folder, filename + extension))
            return json.dumps({"filename": filename, "extension": extension}), 200


if __name__ == '__main__':
    app.run(port=80)
