from flask import Flask, request, json
from PIL import Image


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
            '''Get file object from POST request, extract and define needed variables for future use.'''
            file = request.files['image']
            extension = splitext(file.filename)[1]
            file.flush()
            size = os.fstat(file.fileno()).st_size
            '''Check for file extension and file size.'''
            if extension not in allowed_extension:
                return 'File type is not supported', 415

            elif size > 6000000:
                return 'File size too large', 400

            else:
                '''Remove metadata of the file.'''
                image = Image.open(file)
                data = list(image.getdata())
                file_without_exif = Image.new(image.mode, image.size)
                file_without_exif.putdata(data)

                '''Save the image with a new randomly generated filename in the desired path, and return URL info.'''
                filename = secrets.token_urlsafe(5)
                file_without_exif.save(os.path.join(storage_folder, filename + extension))
                return json.dumps({"filename": filename, "extension": extension}), 200
        else:
            return 'Unauthorized use', 401


if __name__ == '__main__':
    app.run(port=80)
