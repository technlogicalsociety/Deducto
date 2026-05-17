from pathlib import Path
import pytesseract
from PIL import Image
import cv2
import numpy as np

def extract_text_from_image(image_path: str) -> str:

    """
    Takkes a file path to an images
    Returns extracted text as a string
    """
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    """
    ==PRE - PROCESSING==


    importing NumPy Arrays (via Open CV)

    cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)

    Loads image in grayscale (good for OCR).

    cv2.threshold(..., cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    Turns it into a black‑and‑white binary image with an auto‑calculated threshold (OTSU).

    This is a very common, proven preprocessing step for receipt‑OCR and works well on phone‑photo‑style receipts.

    """
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    _, clean_image = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    """
    ==EXTRACTION==

    External library API's
    Imports from package Pillow API and pytesseract image processing
    """
    pil_image = Image.fromarray(clean_image)
    text = pytesseract.image_to_string(pil_image)

    return text.strip()
