from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(input_file, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Set the font and size
    c.setFont("Courier", 10)

    with open(input_file, "r") as file:
        lines = file.readlines()

    x_margin = 40
    y_margin = height - 40
    line_height = 12

    for line in lines:
        if y_margin < 40:
            c.showPage()
            c.setFont("Courier", 10)
            y_margin = height - 40

        c.drawString(x_margin, y_margin, line.strip())
        y_margin -= line_height

    c.save()


# Example usage
input_file = "96 Paint app.py"  # Replace with your Python file
output_file = "output.pdf"  # Output PDF file name
create_pdf(input_file, output_file)
