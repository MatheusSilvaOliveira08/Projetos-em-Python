def calcular (peso,altura): 
    IMC = peso/ (altura**2)
    return IMC

def classificar_IMC (IMC): 
    if IMC < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= IMC <= 24.9: 
        return "Peso normal"
    elif 25 <= IMC <= 29.9: 
        return "Sobrepeso"
    elif 30 <= IMC <= 34.9: 
        return "Obesidade de Grau 1"
    elif 35 <= IMC <= 39.9: 
        return "Obesidade de Grau 2"
    else: 
        return "Obesidade de Grau 3"
    
peso = float (input("Digite a o seu peso: "))
altura = float (input (" Digite a sua altura: "))

IMC  = calcular (peso, altura)
categoria = classificar_IMC (IMC)

print ( f"Seu IMC é: {IMC:.2f}")
print (f"Classificação: {categoria}")
