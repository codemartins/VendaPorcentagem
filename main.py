#Algoritmo
# 1º Passo: Peça para o usuário digitar o valor do produto;
# 2º Passo: Peça para  usuário digitar a porcentagem desconto;
# 3º Passo: Calcule o valor do desconto
#           (porcentagem / 100 * valor do produto);
# 4º Passo: Calcule o valor final.




Cliente = input('>>>>> Caro cliente. Qual o seu nome, por favor? ')
Produto = float(input('$$$ Digite qual o valor do produto: ' ))
Porcentagem = int(input('$$$ Digite qual o Desconto que deseja aplicar: '))

Desconto = (Porcentagem/100) * Produto
ValorFinal = Produto - Desconto

print('')
print('----------------------------------------------------')
print('| uhuuu!!! Você Ganhou um desconto de : R$', Desconto, ' reais.')
print('| Valor total a ser pago é de: R$', ValorFinal, 'reais.')
print('----------------------------------------------------')
print('Volte sempre,', Cliente, '!!! ♥')