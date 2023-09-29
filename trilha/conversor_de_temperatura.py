def conversor_temperatura(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F!')

if __name__ == '__main__':
    celsius = float(input('Informe a temperatura em °C: '))
    conversor_temperatura(celsius)