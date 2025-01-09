from rembg import remove
from PIL import Image
input_path = 'desktop.jpg'
output_path = 'desktop.jpg'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(output_path)
print("Background removed successfully")