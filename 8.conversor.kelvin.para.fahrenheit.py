# F = 1.8(K - 273.15) + 32

print("Conversor de Kelvin para Fahrenheit\n")

temperaturaKelvin=float(input("Temperatura em Kelvin: "))
temperaturaFahrenheit=1.8*(temperaturaKelvin-273.15)+32

print("\n%.2f graus Kelvin equivalem a %.2f graus Fahrenheit"%(temperaturaKelvin,temperaturaFahrenheit))