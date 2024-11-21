import numpy as np
from pyzbar.pyzbar import decode
import qrcode

def decode_image(image:np.ndarray):
    decoded_data = decode(image) 

    return decoded_data[0].data.decode('utf-8')

def encode_image(input:str):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )

    # Add text data to the QR Code
    qr.add_data(input)
    qr.make(fit=True)

    # Create an image of the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to NumPy array
    qr_array = np.array(img, dtype=np.uint8)

    # Ensure it is in RGB format
    if qr_array.ndim == 2:  # Grayscale QR code
        qr_array = np.stack([qr_array] * 3, axis=-1) * 255

    return qr_array
