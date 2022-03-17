#Conversão de temperatura celsius --> fahrenheit
temp_celsius = float(input('Insira a temperatura, em graus celsius: '))
temp_fahrenheit =  (1.8 * temp_celsius) + 32

print(f'A temperatura correspondente em fahrenheit é {temp_fahrenheit:.1f}°F')