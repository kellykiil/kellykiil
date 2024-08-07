n1= int(input("Digite o primeiro numero que deseja fazer a operação matematica: "))
n2= int(input("Digite o segundo numero que deseja fazer a operação matematica: "))
operacao= input("Digite a operação matematica que deseja fazer: ")
if operacao == "+":
    print("Resultado", n1+n2)

elif operacao == "-":
    print("Resultado", n1-n2)
    
elif operacao == "*":
    print("Resultado", n1*n2)
    
elif operacao == "/":
    print("Resultado", n1/n2)  
else:
    print("Operação inválida")
