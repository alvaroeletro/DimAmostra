
print("Bem vindo\n")
print("Calculo do Tamanho de uma amostra necessária\n")
print("V.0.01 versão inicial\n")
print(".....::: Admita as seguintes condições :::.....\n")


contador = 0
erro=float(input("Inserir erro pré-fixado "))
x=0
s=0
espacoamostral = []
somax=0
somaXi=0
n0=int(input("Insira a qntd. da Amostra Piloto "))
gl = (n0-1)
t=input("Verifique na tabela o valor de talpha/2 ")



#NECESSITA SER CONSULTADO EM TABELA
print("Certifique-se de que os valores inseridos correponder a curva T-student")

while contador<n0:
    contador+=1
    x=(int(input("X{}".format(contador))))
    espacoamostral.append(x)

print("Término da inserção de valores")
print("Lista gerada{}".format(espacoamostral))

print("\n Início do calculo\n ")

contador = 0

#CALCULO DO SOMATÓRIO DE X
while contador<n0:
    x=0
    x=espacoamostral[(contador)]
    somax=somax+x
    contador += 1

#CALCULO DA MEDIA
media = somax/n0
print(" A média calculada é de {}".format(media))

#CALCULO DO DESVIO PADRÃO

Xi=0
contador = 0
somaparcelas = 0
#somatório da parcela
while contador<n0:
    Xi=espacoamostral[(contador)]
    Xi= (Xi-media)**2
    somaXi += Xi
    contador+=1


#print("Soma das parcelas {}".format(somaparcelas))
#calculo do desvio padrao com o Somatório pronto

s= (somaXi/(gl))
s= (s**(0.5))


print("Desvio padrão calculado {}".format(s))

#FINALMENTE
#CALCULO DA AMOSTRA MÍNIMA

amostramin=float(t)*float(s)
amostramin=amostramin/erro
amostramin=amostramin**2

print("A amostra minima para esse experimento é de {}".format(amostramin))














