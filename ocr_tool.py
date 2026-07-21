import cv2
import pytesseract
import numpy as np
from PIL import Image
import os

# Update this path if Tesseract is not in your system PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_corrected_orientation(image):
    """
    Detects the orientation of the image using Tesseract OSD 
    and rotates it to be upright.
    """
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    try:
        osd = pytesseract.image_to_osd(rgb, output_type=pytesseract.Output.DICT)
        rotate_angle = osd['rotate']
        print(f"[INFO] Detected rotation needed: {rotate_angle} degrees")
        
        if rotate_angle == 90:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif rotate_angle == 180:
            image = cv2.rotate(image, cv2.ROTATE_180)
        elif rotate_angle == 270:
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            
        return image
    except Exception as e:
        print(f"[WARNING] OSD failed (likely not enough text): {e}")
        return image

def deskew_image(image):
    """
    Corrects small skews/tilts in the image text.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]
    
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    return rotated

def process_image_to_markdown(image_path, output_name="output.md"):
    """
    Full pipeline: Load -> Rotate -> Deskew -> OCR -> Save to MD.
    """
    img = cv2.imread(image_path)
    if img is None:
        print("[ERROR] Could not read image.")
        return

    img = get_corrected_orientation(img)
    img = deskew_image(img)
    text = pytesseract.image_to_string(img, config='--psm 3')
    
    with open(output_name, "w", encoding="utf-8") as f:
        f.write(f"# OCR Result: {os.path.basename(image_path)}\n\n")
        f.write(text)
        
    print(f"[SUCCESS] Content saved to {output_name}")

if __name__ == "__main__":
    # Ensure Tesseract and pip dependencies are installed, then swap 'scanned_doc.jpg' for your image.
    process_image_to_markdown("scanned_doc.jpg")
    
