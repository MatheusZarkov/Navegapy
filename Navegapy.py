# api currency: 43346c22de0b4dd8b78d4d6767622676
# bibliotecas necessárias
# import requests
# import json

import requests
import json

def cotacao():
 #  cotacao não precisa de API key
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = json.loads(requisicao.text)
    print('#######################')
    print('#### cotação dolar ####')
    print('#######################')
    print('  ')
    print('Moeda: ' + cotacao['USD']['name'])
    print('Data: ' + cotacao['USD']['create_date'])
    print('Valor atual: R$'  + cotacao['USD']['bid'])
    print('  ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#--------------------------------------------------------------------------------------------------
def previsao():
    # APÍ Key = 7acaa0e12112d032d5be6b59464a3e4c
    cidade = input ('escreva o nome da sua cidade: ')
    requisicao_previsao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=7acaa0e12112d032d5be6b59464a3e4c')
    previsao = json.loads(requisicao_previsao.text)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('temperatura atual:')
    temperatura = (float(previsao['main'] ['temp']) - 273.15)
    print('% 0.2f' % temperatura, 'Cº')

    print('Sensação térmica:')
    sensação_termica = (float(previsao['main'] ['feels_like']) - 273.15)
    print('% 0.2f' % sensação_termica, 'Cº')

    print('Mínima:')
    temperatura_minima = (float(previsao['main']['temp_min']) - 273.15)
    print('% 0.2f' % temperatura_minima, 'Cº')

    print('Máxima:')
    temperatura_maxima = (float(previsao['main']['temp_max']) - 273.15)
    print('% 0.2f' % temperatura_maxima, 'Cº')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#--------------------------------------------------------------------------------------------------
def valordiarias():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print('Quarto Luxo (frente para a praia):\nSingle: R$300,00\nDuplo: R$350,00\nTriplo: R$400,00\nQuadruplo: R$450,00')
    print('--')
    print('Quarto Superior (frente para o estacionamento):\nSingle: R$250,00\nDuplo: R$300,00\nTriplo: R$350,00\nQuadruplo: R$400,00')
    print('Todas as nossas reservas incluem café da manhã, academia gratuita para uso de hóspedes, internet, estacionamento  já inclusos na tarifa.')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#--------------------------------------------------------------------------------------------------
def procedimento_checkin():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print('O nosso check in inicia-se apartir das 14:00, é necessário documento com foto de todas as pessoas que irão se hospedar. O pagamento deverá ser feito no ato do check in. Qualquer dúvida estamos à disposição.')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def principal():
    with open('logo.txt','r') as f:
        f_contents = f.read()
        print(f_contents)
    while True:
        print(' ')

        print(' ')
        print(' ##### Navega beach utilitário ###### ')
        print(' ')
        print('Escolha uma opção a seguir:')
        print(' 1 - Valor do dólar hoje.')
        print(' 2 - Temperatura atual.')
        print(' 3 - Valores de diárias')
        print(' 4 - Procedimento de check in.')
        print(' 5 - Sair')
        opção = int(input('> '))

        if opção == 1:
            cotacao()
        elif opção == 2:
            previsao()
        elif opção == 3:
            valordiarias()
        elif opção == 4:
            procedimento_checkin()
        elif opção == 5:
            print ('Saindo do programa...')
            break
        else:
            print('A opção escolhida é inválida, tente novamente.')


#### invocation ####

principal()