import pyautogui,time
import webbrowser



time.sleep(4)
pyautogui.leftClick(1300,200,duration=1.2)
time.sleep(2)

webbrowser.open_new_tab('https://instagram.com')
time.sleep(3)
#Solicita usuario 
user = pyautogui.prompt("Digite seu nome de usuário:")
pyautogui.click(1330,352,duration=1) #click user
time.sleep(1)
pyautogui.write(user,interval=0.3)


# Solicita a senha
password = pyautogui.password("Digite sua senha:")
time.sleep(1)
pyautogui.click(1330,402 ,duration=1)#click password
pyautogui.write(password,interval=0.3)
time.sleep(3)

pyautogui.click(1432,469,duration=2) # login
time.sleep(6)

#clicar em NAO SALVAR A SENHA
pyautogui.click(1591,308,duration=1) #nao salvar navegador
time.sleep(2)
pyautogui.click(1437,603,duration=2)#nao salvar, instagram
time.sleep(3)

#clicar em buscar
pyautogui.click(1011,330,duration=2)
time.sleep(1)
pyautogui.click(1201,241,duration=2)
pyautogui.write('nike') #escreve nike
time.sleep(3)
pyautogui.click(1228,321,duration=1) #entrar na pagina nike
time.sleep(3)
pyautogui.scroll(-500)
pyautogui.click()
time.sleep(3)
try:
    like=pyautogui.locateCenterOnScreen('like.png')
    time.sleep(3)
    # Se o ícone 'like' for encontrado (significa que a foto NÃO foi curtida)
    if like is not None:
        print(f'Posição do Like: {like}')  # Exibir as coordenadas de 'like'
        pyautogui.click(like[0], like[1], duration=1)  # Clicar no ícone de like
        time.sleep(1)
        pyautogui.click(1865, 132, duration=1)  # Sair da foto
        time.sleep(2)
        pyautogui.click(1002, 953, duration=2)  # Clicar em algum lugar (ajuste conforme necessário)
        pyautogui.click(1094, 951, duration=2)  # Sair do Instagram
        time.sleep(3)
        pyautogui.alert(text='Você saiu', title='AVISO!')
    
    else:
        # Se o ícone 'like' não for encontrado (significa que a foto JÁ foi curtida)
        print("A foto já foi curtida, realizando outras ações.")
        pyautogui.alert(text='  FOTO CURTIDA', title='AVISO!')
except pyautogui.ImageNotFoundException:
    # Caso a imagem não seja encontrada, o PyAutoGUI lança a exceção `ImageNotFoundException`
    print("A imagem 'like.png' não foi encontrada, a foto já foi curtida.")
    # Ações alternativas caso a foto já tenha sido curtida
    pyautogui.click(1865, 132, duration=1)  # Sair da foto
    time.sleep(2)
    pyautogui.click(1002, 953, duration=2)  # Clicar em algum lugar
    pyautogui.click(1094, 951, duration=2)  # Sair do Instagram
    time.sleep(3)
    pyautogui.alert(text='Você saiu', title='AVISO!')