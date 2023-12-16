from PIL import Image, ImageDraw

# Create a blank image with the HyperPixel resolution
width, height = 800, 480
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw something on the image (example: a red rectangle)
draw.rectangle([100, 100, 200, 200], fill="red")

# Display the image on the HyperPixel screen
image.show()
