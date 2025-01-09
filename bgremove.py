from rembg import remove
from PIL import Image
import os

input_path = r'C:\Users\TREVOR\Documents\GitHub\Learning-Curve\trevor.JPG'
output_path = r'C:\Users\TREVOR\Documents\Github\Learning-Curve\trevor_no_bg.JPG'

try:
    # Debug paths
    print(f"Input Path: {input_path}")
    print(f"Output Path: {output_path}")
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Open input image and remove background
    with Image.open(input_path) as inp:
        output = remove(inp)

        # Convert to RGB if necessary
        if output.mode == "RGBA":
            output = output.convert("RGB")

        output.save(output_path, format="JPEG")
    print("Background removed successfully")
    
    
    # Display the processed image
    with Image.open(output_path) as result_img:
        result_img.show()
except Exception as e:
    print(f"An error occurred: {e}")
