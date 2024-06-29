import qrcode
from qrcode.exceptions import DataOverflowError
from PIL import Image

def main():
    try:
        input_URL = input("Enter URL: ").strip()
        if not input_URL:
            raise ValueError("URL cannot be empty")

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )

        qr.add_data(input_URL)
        qr.make(fit=True)

        fcolor = input("Enter fill color (e.g., 'black'): ").strip()
        back_color = input("Enter back color (e.g., 'white'): ").strip()

        if not fcolor:
            fcolor = "black"  # default fill color
        if not back_color:
            back_color = "white"  # default back color

        try:
            Image.new("RGB", (1, 1), fcolor)
            Image.new("RGB", (1, 1), back_color)
        except ValueError as ve:
            raise ValueError(f"Invalid color value: {ve}")

        img = qr.make_image(fill_color=fcolor, back_color=back_color)
        img.save("url_qrcode.png")
        print("QR code generated successfully and saved as 'url_qrcode.png'.")
        print("Data added to QR code:", qr.data_list)

    except ValueError as ve:
        print(f"Input error: {ve}")

    except DataOverflowError as doe:
        print(f"Data overflow error: {doe}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
