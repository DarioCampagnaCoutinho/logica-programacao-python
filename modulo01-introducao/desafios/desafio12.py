print("===== Desafio 12 =====")
preco = float(input('Digite o preço produto = '))
porcentagem = int(input('Digite o desconto ='))

desconto = preco / 100 * porcentagem
resultado = preco - desconto

print('O preço do produto é {} R$ , com desconto de {} % vai custar {:.2f} R$ '.format(preco, porcentagem, resultado))
