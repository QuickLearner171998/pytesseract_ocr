# Text recognition using tesseract and pytesseract
Text recognition using pytesseract

For text detection I simply used clovaai CRAFT-pytorch repository.
Although they also have their text recognition model but their offline model is not trained on alphanumerics.
So I used pytesseract for text recognition.

# Installation
1) Install tesseract from https://github.com/UB-Mannheim/tesseract/wiki

2) Tesseract-OCR directory will be created at the installation location.

3) Go to Tesseract-OCR\tessdata and replace eng.traineddata file with https://github.com/tesseract-ocr/tessdata_best/blob/master/eng.traineddata

4) Add Tesseract-OCR and tessdata directory paths to the Path variables.

## To use tesseract for text recognition:

Open command prompt in the image directory.

tesseract image_name.png out.

This will create out.txt with the detected text.

## To use pytesseract for text recognition:

run demo.py:

python demo.py --imageDir="path/to/imageDir" --preprocess="thresh" --resize=Fasle

#### Note: For good results try resizing the image by different factors. change resize to True for the same. 
