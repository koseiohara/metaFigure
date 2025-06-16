from PyPDF2 import PdfReader, PdfWriter

def add_pdfinfo(target, key, text):
    reader = PdfReader(target)
    meta   = reader.metadata or {}
    meta.update({'/'+key:text})

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(meta)
    pdf = open(target, 'wb')
    writer.write(pdf)


