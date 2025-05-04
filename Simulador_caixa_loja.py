# cadastro de produtos:

import math
print('-_' * 10)
print(' PAPELARIA DA RÊ ')
print('-_' * 10)

print()
total_compra = [] # precisa desta lista para poder retornar todos os itens cadastrados, caso contrário ele retornará apenas o último

while True:
    produto = {}
    produto['nome'] = input('Digite o nome do produto: ')
    produto['preço'] = float(input('Digite o preço do produto: R$ '))
    total_compra.append(produto)

    continua = input('Deseja continuar? [S/N] ').upper().split()[0]
    if continua in 'N':
        break



#mostrar a lista dos itens com o preço e o total a pagar
print()
print('Total de itens registrados: ')
total = 0
for item in total_compra:
    print(f'{item["nome"]}: R$ {item["preço"]:.2f}')
    total += item["preço"]
print()
print(f'Total da sua compra é: R$ {total:.2f}')
print()



#Pagamento
print('''0 - Dinheiro
1 - Pix
2 - Cartão de Débito
3 - Cartão de crédito à vista
4 - Cartão de crédito parcelado (parcela até 8x, parcela mínima: R$ 50,00)''')

opção = int(input('Como você deseja pagar? '))




print()
#condições:

tot_desconto = total * 5 /100
preço_final = total - tot_desconto

if opção == 0:
    print('Pagamento em dinheiro, possui desconto de 5%')
    print(f'Total ficou {preço_final:.2f}')
    cedula = float(input('Valor recebido: R$ '))
    troco = cedula - preço_final
    print(f'Valor do troco: R$ {troco:.2f}')



elif opção == 1:
    print('Pagamento em Pix, possui desconto de 5%')
    print(f'Total ficou {preço_final:.2f}')
    print('Compra finalizada com sucesso, liberando comprovante de pagamento...')

elif opção == 2:
    print('Compra finalizada com sucesso, liberando comprovante de pagamento...')
elif opção == 3:
        print('Compra finalizada com sucesso, liberando comprovante de pagamento...')

elif opção == 4:
    print(f'Sua compra deu o total de {total:.2f}')
    if total == 100:
        print('Este valor você ser parcelado em até 2 vezes no cartão sem juros')
    elif total == 150:
        print('Este valor você ser parcelado em até 3 vezes no cartão sem juros')

    elif total == 200:
        print('Este valor você ser parcelado em até 4 vezes no cartão sem juros')

    elif total == 250:
        print('Este valor você ser parcelado em até 5 vezes no cartão sem juros')

    elif total == 300:
        print('Este valor você ser parcelado em até 6 vezes no cartão sem juros')

    elif total == 350:
        print('Este valor você ser parcelado em até 7 vezes no cartão sem juros')

    elif total >= 400:
        print('Este valor você ser parcelado em até 8 vezes no cartão sem juros')
    elif total < 100:
        print('Imposivel parcelar! Parcela mínima é de R$ 50.00')


print()
print('*'* 24)
print('Obrigada e volte sempre!')
print('*'* 24)










