import pyshorteners 

def encurtar_url (url): 
    encurtar = pyshorteners.Shortener()
    return encurtar.tinyurl.short(url)


url_original = input ('Insira a URL que você deseja encurtar: ')
url_encurtada = encurtar_url(url_original)

print ('URL encurtada: ', url_encurtada)