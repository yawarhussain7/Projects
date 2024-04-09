import qrcode as qr

url = "https://www.youtube.com/watch?v=OKuiyX5k6zg&t=3666s"

image = qr.make(url)

image.save("Wscode.png")