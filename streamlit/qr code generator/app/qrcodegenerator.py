import qrcode

ip = input("Enter link :").strip()
fn = input("Enter filename : ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(ip)  # <-- fixed this line
qr.make(fit=True)  # optional but recommended for proper sizing
img = qr.make_image(fill_color="black", back_color="white")
img.save(fn)

print(f"QR CODE saved as {fn}")
