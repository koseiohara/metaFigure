from PIL import Image, PngImagePlugin

def add_pnginfo(target, key, text):
    png  = Image.open(target)
    meta = PngImagePlugin.PngInfo()
    meta.add_text(key, text)

    png.save(target, pnginfo=meta)




