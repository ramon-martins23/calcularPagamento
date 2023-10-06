#https://www.devmedia.com.br/funcoes-em-python/37340

def calcularPagamento(qtdHoras, valorHora):
      horas = float(qtdHoras) #atribui o valor do param qtdHoras à var horas
      taxa = float(valorHora) #atribui o valor do param valorHora à var taxa
      if horas <= 40: #se o valor de horas for menor ou igual à 40
            salario = horas * taxa 
      else: #se for maior que 40
            horasExced = horas - 40 #calcula quantas horas à mais trabalhou
            salario = 40 * taxa + (horasExced * (1.5 * taxa)) #entre parenteses, calcula o valor por hora extra
      return salario 

userHoras = input('Numero de horas: ')
userTaxa = input('Digite a taxa: ')
totalSalario = calcularPagamento(userHoras, userTaxa)
print(f'O valor de seus rendimentos é : {totalSalario}')