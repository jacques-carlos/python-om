"""

CONSTANTE = "Variáveis" que não vão mudar de valor

Sinais de complexidade (ruim):
- Muitas condições no mesmo if
- Contagem de complexidade (ex.: muitos if dentro de if)
\ -> quebra o código para a próxima linha

"""

# velocidade atual do carro
velocidade_carro = 70
# local em que o carro está na estrada
km_carro = 101

# velocidade máxima do radar 1:
VELOCIDADE_RADAR_1 = 60
# local onde o radar 1 está:
LOCAL_RADAR_1 = 100
# a distância que o radar pega:
RANGE_RADAR_1 = 1
# o início do range do radar:
KM_INICIAL_RADAR_1 = (LOCAL_RADAR_1 - RANGE_RADAR_1)
# o final do range do radar:
KM_FINAL_RADAR_1 = (LOCAL_RADAR_1 + RANGE_RADAR_1)

# True se a velocidade do carro for maior que a permitida no radar 1
velocidade_excedida_no_radar_1 = velocidade_carro > VELOCIDADE_RADAR_1
# True se o km (local) do carro estiver entre o início e  o fim do radar 1
carro_no_radar_1 = km_carro >= KM_INICIAL_RADAR_1 \
    and km_carro <= KM_FINAL_RADAR_1

if velocidade_excedida_no_radar_1:
    print('A velocidade do carro está acima do permitido para o radar 1.')
else:
    print('A velocidade do carro está dentro do permitido para o radar 1.')

if carro_no_radar_1:
    print('O carro está no radar 1.')
else:
    print('O carro não está no radar 1.')

if carro_no_radar_1 and velocidade_excedida_no_radar_1:
    print('O carro foi multado.')
else:
    print('O carro não foi multado.')
