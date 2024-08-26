[temperatura, escala] = input().split(' ')

celsius = ''
kelvin = ''
fahrenheit = ''

if escala == 'C':
    celsius = float(temperatura)

    kelvin = celsius + 273.15
    fahrenheit = (1.8 * celsius) + 32
elif escala == 'K':
    kelvin = float(temperatura)

    celsius = kelvin - 273.15
    fahrenheit = (1.8 * celsius) + 32
elif escala == 'F':
    fahrenheit = float(temperatura)

    celsius = (fahrenheit - 32) / 1.8
    kelvin = celsius + 273.14

print('Temperatura em Celsius: {:.2f} °C'.format(celsius))
print('Temperatura em Fahrenheit: {:.2f} °F'.format(fahrenheit))
print('Temperatura em Kelvin: {:.2f} K'.format(kelvin))