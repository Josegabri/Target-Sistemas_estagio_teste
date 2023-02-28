# mostra se o número informado pertence à senquência de Fibonacci.
numero_informado= int(input('Digite o número: '))
primero_termo= 0
segundo_termo=1
soma=1 
sequencia_Fibonacci = []
for i in range (0,25): 
    soma = segundo_termo + primero_termo
    primero_termo = segundo_termo
    segundo_termo= soma 
    sequencia_Fibonacci.append(primero_termo)
    
if numero_informado in sequencia_Fibonacci: 
    print ('Número informado está presente na sequência de Fibonacci.')
else : 
    print ( 'Número informado não esta presente na sequência de Fibonnaci') 
