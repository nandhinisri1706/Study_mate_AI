import pytesseract
from PIL import Image


def extract_text_from_image(file):

    image = Image.open(file)

    text = pytesseract.image_to_string(image)

    return text
