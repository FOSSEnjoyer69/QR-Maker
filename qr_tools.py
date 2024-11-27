import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

def decode_image(image:np.ndarray):
    decoded_data = decode(image) 

    return decoded_data[0].data.decode('utf-8')

def encode_image(input: str, logo:np.ndarray):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for embedded images
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )

    # Add text data to the QR Code
    qr.add_data(input)
    qr.make(fit=True)

    # Create an image of the QR Code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    
    if logo is not None:
        if isinstance(logo, np.ndarray):
            logo = Image.fromarray(logo)

        center_size = (qr_img.size[0] // 5, qr_img.size[1] // 5)  # Resize center image to 1/5th of the QR code size
        logo = logo.resize(center_size)

        # Calculate the position to paste the center image
        pos = (
            (qr_img.size[0] - logo.size[0]) // 2,
            (qr_img.size[1] - logo.size[1]) // 2,
        )

        # Overlay the center image on the QR Code
        qr_img.paste(logo, pos)

    # Convert to NumPy array
    qr_array = np.array(qr_img, dtype=np.uint8)

    return qr_array