import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4  # Fixed typo here
)

qr.add_data("https://chat.openai.com/")

qr.make(fit=True)

image = qr.make_image(fill_color="pink", back_color="white")  # Adjusted color names to lowercase

image.save("Color.png")
