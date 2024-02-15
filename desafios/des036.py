
#perguntar o valor da casa
vcasa = int(input('Digite o valor da casa: '))
#valor do salário
vsalario = int(input('Digite o quantos você recebe de salário: '))
#quantos anos ele vai pagar
mensalidade = int(input('Em quantos meses você irá pagar: '))
#calcular o valor das prestações mensais sabendo que o valor não pode execer 30% do
vmensal = vcasa/mensalidade
mpagar= vsalario * 0.3

#se ultrapassar o empréstimo será negado
if vmensal >= mpagar:
    print('Seu empréstimo foi aprovado e você irá pagar R${:.2f} por mês'.format(vmensal))
else:
    print('Desculpa mas seu impréstimo não foi aprovado, tente novamente daqui alguns meses!')
