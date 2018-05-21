from flask import Flask, request, json


import os
from os.path import splitext
import secrets


storage_folder = 'STORAGE FOLDER'
secret_key = 'SECRET'
allowed_extension = ['.png', '.jpeg', '.jpg', '.gif']


app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if request.form.to_dict(flat=False)['secret_key'][0] == secret_key:
            file = request.files['image']
            extension = splitext(file.filename)[1]
            file.flush()
            size = os.fstat(file.fileno()).st_size
            if extension not in allowed_extension:
                return 'File type is not supported', 415

            elif size > 6000000:
                return 'File size too large', 400

            else:
                filename = secrets.token_urlsafe(5)
                file.save(os.path.join(storage_folder, filename + extension))
                return json.dumps({"filename": filename, "extension": extension}), 200
        else:
            return 'Unauthorized use', 401


if __name__ == '__main__':
    app.run(port=80)
