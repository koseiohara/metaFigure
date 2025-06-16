from PIL import Image, PngImagePlugin

def add_pnginfo(target, key, text):
    png  = Image.open(target)
    meta = PngImagePlugin.PngInfo()

    for key_old, value_old in png.info.items():
        meta.add_text(key_old, value_old)

    meta.add_text(key, text)

    png.save(target, pnginfo=meta)




