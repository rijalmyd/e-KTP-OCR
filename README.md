# KTP-Indonesian_ID_Card-OCR
This project aims to create an API to scan and convert personal data which covers identity number, name, address, etc. from the image format of an indonesian identification card (*KTP*) into text using PyTesseract Optical Character Recognition (OCR). This includes a deep learning YOLO (You Only Look Once method) based detector that can automatically crop the image to improve OCR's ability to read text from images (this feature requires further development). Big thanks to the developers who have developed most of the contents of this system before.

## Prerequisites
* Flask
```
pip install flask
```
* Numpy
```
pip install numpy
```
* OpenCV
```
pip install opencv-contrib-python
```
* Pandas
```
pip install pandas
```
* PIL
```
pip install pillow
```
* PyTesseract
```
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-ind
pip install pytesseract
```
* TextDistance
```
pip install textdistance
```

## Running the Program
To run the program, use the command below:
```
export FLASK_APP=api.py
flask run
```
or alternatively using this command:
```
python api.py
```

### Request Parameter
Parameter | Data Type | Mandatory | Notes
--- | --- | :---: | ---
image | Image Files | M | Foto KTP

### Response Parameter

Parameter | Description
--- | ---
nik | NIK dari hasil OCR
nama | Nama dari hasil OCR
tempat_lahir | Nama tempat lahir dari hasil OCR
tgl_lahir | Tanggal lahir dari hasil OCR (DD-MM-YYYY)
time_elapsed | Waktu yang pemrosesan yang dibutuhkan (detik)

### Success Response Example
```
{
  "nik": "1203040101900001"
  "nama" : "JOHN DOE"
  "tempat_lahir" : "JAKARTA"
  "tgl_lahir" : "01-01-1990"
  "time_elapsed" : "0.675"
}
```

### Notes for KTP Detection using YOLO
1. Uncomment on line 7 and 29 in ```api.py```
2. Download trained weights [here](https://drive.google.com/open?id=1acjcOcTCHUjBg-1CVvoFD59nUp9vfeDL) and put in data/yolo/ folder
3. Change file name on line 13 in ```yolo_detect.py```
4. Run the program

## Acknowledgments
* https://github.com/enningxie/KTP-OCR
* https://github.com/jeffreyevan/OCR
