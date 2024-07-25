import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
import arabic_reshaper
import os

img = cv2.imread("like.png")

# Load a font that supports Arabic characters
fontpath = "arial.ttf"  # Make sure to download an Arabic font and specify the correct path
font = ImageFont.truetype(fontpath, 32)

# Convert the image to a PIL image
img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Create a drawing context
draw = ImageDraw.Draw(img_pil)

# Arabic text
text = "اللغة العربية"

# Reshape and bidi the text
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)

# Position and font color
x, y = 100, 80
font_color = (255, 255, 255)  # White

# Draw the text on the image
draw.text((x, y), bidi_text, font=font, fill=font_color)

# Convert back to a NumPy array
img = np.array(img_pil)

# Display the image with Arabic text
cv2.imshow("Image with Arabic", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()