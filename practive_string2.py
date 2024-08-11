email= input("Insira seu email: ")
#encontrar se possui @ no email
indice_arroba=email.find('@')

#se True continuar a análise
if indice_arroba != -1:
    indice_ponto = email.find('.',indice_arroba)

    #se False, invalidar email por não conter o ponto
    if indice_ponto != -1:
        print("Email válido")

    else:
        print("EMAIL INVÁLIDO")

else:
    print("Email inválido, pois não possui nenhum @")


