import json

with open ('dados.json', encoding= 'utf-8') as d: 
    dados = json.load(d)

def mapeamento(item, chave):
    return item[chave]

valor = [mapeamento(item,'valor') for item in dados]
dia = [mapeamento(item,'dia') for item in dados]

valor_sem_faturamentos_zerados= set(valor)
valor_sem_faturamentos_zerados.remove(0.0)

menor_valor = min(valor_sem_faturamentos_zerados)
maior_valor= max(valor)

soma=0
for i in range (len(valor)) : 
    soma+= valor[i]

media = soma / 21

numero_de_dias=0
for j in range(len(valor)): 
    if valor[j] > media:
        numero_de_dias+=1

print (f'O menor  faturamento em um dia do mês, desconsiderando feriados e finais de semana foi igual a {menor_valor}')
print(f'\nO maior faturamento ocorrido em um dia do mês foi {maior_valor}')
print(f'\nO número de dias do mês em que o valor do faturamento diário foi maior que à média mensal foi {numero_de_dias}')
