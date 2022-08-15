import os

from PIL import Image
import img2pdf


def convert_png_to_pdf(png_path, replace=True, resize=True):
    image_item = Image.open(png_path)
    converted_image = image_item.convert('RGB')
    if resize:
        basewidth = 300
        wpercent = (basewidth / float(image_item.size[0]))
        hsize = int((float(image_item.size[1]) * float(wpercent)))
        image_item = image_item.resize((basewidth, hsize), Image.ANTIALIAS)
    out_path = png_path.replace('.png', '.pdf')
    converted_image.save(out_path)
    if replace:
        os.remove(png_path)
    return out_path


def convert_png_to_pdf_2(png_path, replace=True):
    out_path = png_path.replace('.png', '.pdf')
    with open(out_path, "wb") as f:
        f.write(img2pdf.convert(png_path))
    if replace:
        os.remove(png_path)
    return out_path