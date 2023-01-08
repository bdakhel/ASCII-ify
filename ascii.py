import math
import sys
from PIL import Image, ImageDraw, ImageFont
import os
# List of characters to use for image representation
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Create list of characters in reverse order
char_array = list(chars[::-1])

# Calculate interval for mapping image pixel values to characters
char_length = len(char_array)
interval = char_length / 256

# Dimensions of each character in the output image
one_char_width = 10
one_char_height = 18

# Map input pixel value to a character
def get_char(input_int):
    return char_array[math.floor(input_int * interval)]

# Read image file name from argument list
image = sys.argv[1]

# Open text file for writing
text_file = open("ASCII-ified.txt", "w")

# Open image file and convert to RGB
im = Image.open(image).convert('RGB')

# Load font
fnt = ImageFont.truetype("/home/runner/ASCII-ify/Lucon.ttf", 15)

# Get original image dimensions
width, height = im.size

# Scale factor for resizing image

scale_factor = 0.25
# Resize image
im = im.resize(
    (int(scale_factor * width), int(scale_factor * height * (one_char_width / one_char_height))),
    Image.NEAREST,
)
# Update dimensions after resizing
width, height = im.size

# Load image pixels
pix = im.load()

# Create new image with the same size as the original image
output_image = Image.new("RGB", (one_char_width * width, one_char_height * height), color=(0, 0, 0))

# Create image draw object
d = ImageDraw.Draw(output_image)

# Iterate over all pixels in the image
for i in range(height):
    for j in range(width):
        # Get pixel values
        r, g, b = pix[j, i]

        # Calculate pixel brightness
        h = int(r / 3 + g / 3 + b / 3)

        # Update pixel value with brightness
        pix[j, i] = (h, h, h)

        # Write character corresponding to pixel value to text file
        text_file.write(get_char(h))

        # Draw character on output image
        d.text((j * one_char_width, i * one_char_height), get_char(h), font=fnt, fill=(r, g, b))

    # Add newline character to text file after each row of pixels
    text_file.write("\n")

# Save output image
output_image.save(f"/home/runner/ASCII-ify/ASCII-ified.png")
