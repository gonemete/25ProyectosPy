#Crear tus propios códigos QR, 
# así como el proceso de codificación/decodificación de la información.
#  Este proyecto emplea la librería qrcode.

import qrcode

img = qrcode.make('Texto del QR. Puede ser cualquier cosa.')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")