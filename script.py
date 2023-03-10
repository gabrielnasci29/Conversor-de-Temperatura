temperatura = float(input('Digite a temperatura em Celsius: '))

print('''Escolha uma opção para conversão:
Fahrenheit [1]
Kelvin [2]
''')

escolher_conversao = int(input('Escolha uma opção: '))

if escolher_conversao == 1:

    print(f'{temperatura:.2f}º Graus Celsius em Fahrenheit equivale a {(temperatura * 9 / 5) + 32}')

elif escolher_conversao == 2:

    print(f'{temperatura:.2f}° Graus Celsius em Kelvin equivale a {(temperatura + 273.15)}')

else:
    print('Clicou a tecla errada!')
