#  Escreva um programa que inverta os caracteres de um string.
string = 'estagio'
string_invertida=''
tamanho_string= len(string)
for i in range ((tamanho_string-1), 0,-1): 
    string_invertida += string[i]

print(string_invertida)
    
