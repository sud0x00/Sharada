from PIL import Image, ImageDraw, ImageFont

# Open the text file and read each line
with open("sharada.txt", "r" , encoding='utf-8') as f:
    lines = f.readlines()

print(lines)
# Set up image size and font
image_width = 500
image_height = 500

font = ImageFont.truetype('NotoSansSharada.ttf', 120 , layout_engine=ImageFont.LAYOUT_RAQM)

# Loop through each line and create an image for each one
for index, line in enumerate(lines):
    # Create a new image
    image = Image.new('RGB', (image_width, image_height), color = (255, 255, 255))

    # Draw the text on the image
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(line.strip(), font=font)
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2
    draw.text((x, y), line.strip(), fill=(0, 0, 0), font=font)

    # Save the image with a unique name
    image.save(f'images/image_{index}.png')

print(lines)
