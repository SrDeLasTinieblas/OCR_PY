import cv2
import pytesseract
from translate import Translator
from langdetect import detect

# Cargar la imagen
img = cv2.imread("Hannibal.jpg")

def OCR(img):
    # Ejecutar el OCR
    text = pytesseract.image_to_string(img)
    return text

def detectIdiomaTexto(text):
    # Detectar el idioma del texto
    language = detect(text)
    return language
    
def traducirText(text, lenguaje):
    # Traducir el texto a español
    translator = Translator(to_lang="es")
    translation = translator.translate(text)
    return translation

def main():
    print(OCR(img))
    print(detectIdiomaTexto(OCR(img)))
    print(traducirText(OCR(img), detectIdiomaTexto(OCR(img))))


if __name__ == "__main__":
    main()




