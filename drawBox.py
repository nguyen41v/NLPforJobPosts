from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import matplotlib.pyplot as plt

# width = 100
# height = 50
#
# font = ImageFont.truetype("Arial")
#
# text = "very loooooooooooooooooong text"
#
# # get text size
# text_size = font.getsize(text)
#
# # set button size + 10px margins
# # button_size = (text_size[0]+20, text_size[1]+20)
# button_size = (width, height)
#
# # create image with correct size and black background
# button_img = Image.new('RGBA', button_size, "black")
#
# # put text on button with 10px margins
# button_draw = ImageDraw.Draw(button_img)
# button_draw.text((10, 10), text, font=font)
#
# # put button on source image in position (0, 0)
# source_img.paste(button_img, (50, 50))

from PIL import Image, ImageDraw

W, H = (60,20)
msg = "hello"

im = Image.new("RGBA", (W,H), (18, 85, 204, 100))
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2), msg, fill="white")

im.save("helloLight.png", "PNG")
#
# # save in new file
# source_img.save("output.jpg", "JPEG")
