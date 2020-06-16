
print("Bem vindo\n")
print("Calculo do Tamanho de uma amostra necessária\n")
print("V.0.01 versão inicial\n")
print(".....::: Admita as seguintes condições :::.....\n")
print("Utilização de valores da curva T-student\n")
print("Nível de significância alpha 5%")
print("o ível de confiabilidade é de 95%")
print("n0-1 para grau de liberdade | 9 |\n")

contador = 0
x=0
espacoamostral = []
somax=0
n0=10
gl = n0-1

#n0 SERÁ FIXADO EM 10 PELO FATO DE QUE SE ESSE VALOR FOR ALTERADO
#NECESSITA SER CONSULTADO EM TABELA
#ESSA FUNCIONALIDADE NÃO ESTÁ DISPONÍVEL NESSA VERSÃO DO PROGRAMA
#gl = grau de liberdade


while contador<10:
    contador+=1
    x=(int(input("X{}".format(contador))))
    espacoamostral.append(x)

print("Término da inserção de valores")
print("Lista gerada{}".format(espacoamostral))

print("\n Início do calculo\n ")

contador = 0

#CALCULO DO SOMATÓRIO DE X
while contador<10:
    x=0
    x=espacoamostral[(contador)]
    somax=somax+x
    contador += 1

#CALCULO DA MEDIA
media = somax/n0

#CALCULO DO DESVIO PADRÃO

Xi=0
contador = 0
somaparcelas = 0
#somatório da parcela
while contador<10:
    Xi=espacoamostral[(contador)]
    parcela=((Xi-somax)**2)
    contador+=1
    somaparcelas += parcela

#calculo do desvio padrao com o Somatório pronto
print(somaparcelas)

s= somaparcelas/gl
s = s ** 0.5




print(" A média calculada é de {}".format(media))
print("Desvio padrão calculado {}".format(s))


#FINALMENTE
#CALCULO DA AMOSTRA MÍNIMA

amostramin= (2.26*(s))
amostramin=amostramin/3
amostramin=amostramin**2

print("A amostra minima para esse experimento é de {}".format(amostramin))














