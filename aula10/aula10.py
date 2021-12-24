'''
Condições Python e instruções If
    Igual a: a == b
    Diferente de: a! = B
    Menor que: a <b
    Menor ou igual a: a <= b
    Maior que: a> b
    Maior ou igual a: a> = b
'''

#a=True
a=10
b=5
op="*"

'''
if a<b:
    print("Curso de Python!")

print("Fim do PROGRAMA!")
'''    

if op=="+":
    res=a+b
    print("Operação " + op + " : res = " +str(res)) #str CASTE

if op=="-":
    res=a-b
    print("Operação " + op + " : res = " +str(res)) #str CASTE

if op=="/":
    res=a/b
    print("Operação " + op + " : res = " +str(res)) #str CASTE

if op=="*":
    res=a*b
    print("Operação " + op + " : res = " +str(res)) #str CASTE
