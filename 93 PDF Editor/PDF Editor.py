import pikepdf
from pdf2docx import Converter
from docx2pdf import convert
from pdf2image import convert_from_path
from pikepdf import Pdf, PdfImage, Page, Rectangle
from glob import glob

def main():
    print("Please select an option for PDF operation:")
    options = [
        "PDF to WORD", "WORD to PDF", "PDF to IMAGE", "Extract Image from PDF",
        "Add watermarks/Overlays on PDF", "Merge PDF", "Reverse PDF",
        "Delete page from PDF", "Move Page in PDF", "Split PDF (Convert into single page pdf)",
        "Encrypt PDF (Set password)", "Rotate PDF file"
    ]
    for i, opt in enumerate(options, 1):
        print(f"{i} :- {opt}")

    choice = int(input("Select option: "))

    if choice == 1:
        convert_pdf_to_word()
    elif choice == 2:
        convert_word_to_pdf()
    elif choice == 3:
        convert_pdf_to_image()
    elif choice == 4:
        extract_image_from_pdf()
    elif choice == 5:
        add_watermark()
    elif choice == 6:
        merge_pdfs()
    elif choice == 7:
        reverse_pdf()
    elif choice == 8:
        delete_page_from_pdf()
    elif choice == 9:
        move_page_in_pdf()
    elif choice == 10:
        split_pdf()
    elif choice == 11:
        encrypt_pdf()
    elif choice == 12:
        rotate_pdf()
    else:
        print("Invalid choice, please try again.")

def convert_pdf_to_word():
    obj = Converter(input("Enter PDF path: "))
    obj.convert(input("Enter name for DOCX: "))
    obj.close()
    print("Conversion successful!")

def convert_word_to_pdf():
    convert(input("Enter DOCX name: "), input("Enter name for PDF: "))
    print("Conversion successful!")

def convert_pdf_to_image():
    doc = input("Enter PDF Path: ")
    sv = input("Enter name for JPEG image: ")
    old_pdf = convert_from_path(doc, poppler_path=r"D:\project\Python Projects\100 Days challenge\94 PDF Editor\poppler-23.07.0\Library\bin")
    for i, page in enumerate(old_pdf):
        page.save(f"{sv}{i}.jpg", "JPEG")
    print("Conversion successful!")

def extract_image_from_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    a = int(input("Enter page number: "))
    page = old_pdf.pages[a]
    print("Code of images:", list(page.images.keys()))
    raw_image = page.images['/X8']
    pdf_image = PdfImage(raw_image)
    pdf_image.extract_to(fileprefix="extracted_image")
    print("Image extraction successful!")

def add_watermark():
    old_pdf1 = Pdf.open(input("Enter PDF 1 name: "))
    old_pdf2 = Pdf.open(input("Enter PDF 2 name: "))
    a = int(input("Enter PDF 1 page index: "))
    b = int(input("Enter PDF 2 page index: "))
    des_page = Page(old_pdf1.pages[a])
    sur_page = Page(old_pdf2.pages[b])
    d, e, f, g = map(int, input("Enter position (x, y) and size (width, height): ").split())
    des_page.add_overlay(sur_page, Rectangle(d, e, f, g))
    old_pdf1.save(input("Enter name to save PDF: "))
    print("Watermark added successfully!")

def merge_pdfs():
    new_pdf = Pdf.new()
    for file in glob("*.pdf"):
        old_pdf = Pdf.open(file)
        new_pdf.pages.extend(old_pdf.pages)
    new_pdf.save(input("Enter name to save merged PDF: "))
    print("Merge successful!")

def reverse_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    old_pdf.pages.reverse()
    old_pdf.save(input("Enter name to save PDF: "))
    print("PDF reversed successfully!")

def delete_page_from_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    a, b = map(int, input("Enter start and end page numbers: ").split())
    del old_pdf.pages[a:b]
    old_pdf.save(input("Enter name to save PDF: "))
    print("Pages deleted successfully!")

def move_page_in_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    a, b = map(int, input("Enter page index to move and destination index: ").split())
    old_pdf.pages.insert(b, old_pdf.pages.pop(a))
    old_pdf.save(input("Enter name to save PDF: "))
    print("Page moved successfully!")

def split_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    for n, page in enumerate(old_pdf.pages):
        new_pdf = Pdf.new()
        new_pdf.pages.append(page)
        new_pdf.save(f"new{n}.pdf")
    print("PDF split successfully!")

def encrypt_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    no_ext = pikepdf.Permissions(extract=False)
    old_pdf.save(input("Enter name to save PDF: "), encryption=pikepdf.Encryption(user=input("Password: "), owner=input("Owner name: "), allow=no_ext))
    print("PDF encrypted successfully!")

def rotate_pdf():
    old_pdf = Pdf.open(input("Enter PDF name: "))
    a = int(input("Enter rotation degree: "))
    st, ed = map(int, input("Enter start and end page numbers: ").split())
    for page in old_pdf.pages[st:ed]:
        page.Rotate = a
    old_pdf.save(input("Enter name to save PDF: "))
    print("PDF rotated successfully!")

if __name__ == "__main__":
    main()
