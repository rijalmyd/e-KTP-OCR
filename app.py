import cv2
import json
import numpy as np
import ocr
import timeit
import yolo_detect
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ocr', methods = ['POST'])
def upload_file():
    start_time = time.time()

    if 'image' not in request.files:
        finish_time = time.time() - start_time

        json_content = {
            'message': "image is empty",
            'time_elapsed': str(round(finish_time, 3))
        }
    else:
        imagefile = request.files['image'].read()
        npimg = np.frombuffer(imagefile, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # Note: Uncomment for YOLO feature
        image = yolo_detect.main(image)
        # print(image)

        try:
            (nik, nama, tempat_lahir, tgl_lahir, jenis_kelamin, agama,
            status_perkawinan, provinsi, kabupaten, alamat, rt_rw, 
            kel_desa, kecamatan, pekerjaan, kewarganegaraan) = ocr.main(image)

            finish_time = time.time() - start_time

            json_content = {
                'nik': str(nik),
                'nama': str(nama),
                'tempat_lahir': str(tempat_lahir),
                'tgl_lahir': str(tgl_lahir),
                'jenis_kelamin': str(jenis_kelamin),
                'agama': str(agama),
                'status_perkawinan': str(status_perkawinan),
                'pekerjaan': str(pekerjaan),
                'kewarganegaraan': str(kewarganegaraan),
                'alamat': {
                    'name': str(alamat),
                    'rt_rw': str(rt_rw),
                    'kel_desa': str(kel_desa),
                    'kecamatan': str(kecamatan),
                    'kabupaten': str(kabupaten),
                    'provinsi': str(provinsi)
                },
                'time_elapsed': str(round(finish_time, 3))
            }
        except:
            json_content = {
                'error': True,
                'message': 'Maaf, KTP tidak terdeteksi'
            }
    python2json = json.dumps(json_content)
    return app.response_class(python2json, content_type = 'application/json')

if __name__ == "__main__":
    app.run(debug = True)
