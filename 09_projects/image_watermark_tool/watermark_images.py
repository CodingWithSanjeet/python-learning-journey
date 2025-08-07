# Import required modules from PIL (Python Imaging Library) for image manipulation
from PIL import Image,ImageDraw,ImageFont
import os

# Define function to add watermark text to all images in a folder
def add_watermark_text_to_folder(input_dir, output_dir, watermark_text, position, font_size):
    # Check if output directory exists, if not create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if file is an image by examining its extension (case-insensitive)
        if filename.lower().endswith((".jpg",".jpeg",".png",".bmp")):
            # Create full path to the image file by joining directory and filename
            img_path = os.path.join(input_dir,filename)
            # Open the image file using PIL
            original_img = Image.open(img_path)
            # Get the width and height dimensions of the image
            width, height = original_img.size
            # Create a drawing context on the image to add text
            draw = ImageDraw.Draw(original_img)
            # Try to load custom font file, fallback to default if not found
            try:
                font = ImageFont.truetype("super_nought.ttf", size=font_size)
                # Print font bounding box and size for debugging
                print(f"Here is the font: {font.getbbox(watermark_text)}{font.size}")
            except OSError:
                # Handle case when custom font file doesn't exist
                print("Font file not found, using default font")
                font = ImageFont.load_default()
            
            # Print the loaded font name for verification
            print(f"Here is the font: {font.getname()}")
            # Get bounding box coordinates of the text using font mask
            # getbbox() returns (x0, y0, x1, y1) - top-left and bottom-right coordinates
            x0,y0,x1,y1 = font.getmask(watermark_text).getbbox()
            # Calculate actual text width by subtracting left from right coordinate
            text_width = x1-x0
            # Calculate actual text height by subtracting top from bottom coordinate
            text_height = y1-y0
            # Print all dimensions for debugging and verification
            print(f"image width: {width}, image height: {height}")
            print(f"text width: {text_width}, text height: {text_height}")
            
            # Set margin distance from image edges (reduced from 100 to 50 pixels)
            margin = 50
            
            # Calculate x position: place text near right edge with margin
            x = width - text_width - margin
            # Calculate y position: place text near bottom edge with margin
            y = height - text_height - margin
            
            print(f"Calculated position: x={x}, y={y}")
            
            # Draw the watermark text on the image at calculated position
            # Using both fill and stroke for better visibility
            draw.text((x,y), text=watermark_text, fill="white", font=font)
            
            # Create output file path with "watermark_" prefix
            output_path = os.path.join(output_dir,f"watermark_{filename}")
            
            # Save the watermarked image to the output directory
            original_img.save(output_path)
            
            # Print confirmation message
            print(f"Watermarked image saved as {output_path}")
            
            
# Define input directory path (relative path to current directory)
input_dir = r".\input_images"
# Define output directory path (relative path to current directory)
output_dir = r".\watermarked_images"
# Set the watermark text to be added to images
watermark_text = "@sanjeet"
# Set the font size for the watermark text (reduced from 200 to 32 for better fit)
font_size = 32
# Define position variable (note: has typo 'postion' and not actually used in function)
postion = 0
# Call the function to process all images, using the font_size variable instead of hardcoded value
add_watermark_text_to_folder(input_dir, output_dir,watermark_text,position=postion,font_size=font_size)
            