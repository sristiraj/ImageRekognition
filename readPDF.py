#!/bin/bash


import PyPDF2
import pyocr
import pyocr.builders
from wand.image import Image
import io
from PIL import Image as PI


# tool = pyocr.get_available_tools()[0]
# lang = tool.get_available_languages()[1]
# req_image = []
# final_text = []
image_pdf = Image(filename="C:/Users\Sristi Raj\Desktop/Certificate_AWS_Architected_App.pdf", resolution=300)
image_jpeg = image_pdf.convert('jpeg')

image_jpeg.save(filename="C:/Users\Sristi Raj\Desktop/Certificate_AWS_Architected_App.jpeg")

# for img in image_jpeg.sequence:
#     img_page = Image(image=img)
#     req_image.append(img_page.make_blob('jpeg'))
#
# for img in req_image:
#     txt = tool.image_to_string(
#         PI.open(io.BytesIO(img)),
#         lang=lang,
#         builder=pyocr.builders.TextBuilder()
#     )
# final_text.append(txt)