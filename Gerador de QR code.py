import qrcode

imagem = qrcode.make("https://www.google.com.br/")

imagem.save("QrCode.png")

print ("Seu Qr Code foi gerado com sucesso!")
