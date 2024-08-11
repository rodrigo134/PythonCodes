entrada_user= input("insira seu cpf ")
# Formata a entrada removendo espaços, pontos e traços
entrada_formatada=entrada_user.strip() #remove espaços em brancos
entrada_formatada=entrada_formatada.replace('.','') #remove pontos
entrada_formatada= entrada_formatada.replace('-','')#remove o traço

#validação se cpf for formado por 11 numeros e de tamanho igual a 11
if  len(entrada_formatada)==11 and entrada_formatada.isdigit():
   print(f'{entrada_user} CPF VÁLIDO ')
else:
   print(f'{entrada_user} CPF INVÁLIDO')
