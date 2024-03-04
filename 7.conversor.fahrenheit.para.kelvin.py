# K = (F - 32) / 1.8 + 273.15
print("Conversor de Fahrenheit para Kelvin\n")

temperaturaFahrenheit=float(input("Temperatura em Fahrenheit: "))
temperaturaKelvin=(temperaturaFahrenheit-32)/1.8+273.15

print("\n%.2f graus Fahrenheit equivalem a %.2f graus Kelvin"%(temperaturaFahrenheit,temperaturaKelvin))