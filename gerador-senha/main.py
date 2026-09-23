import random
import string

def gerar_senha (tamanho_senha):
    letras = string.ascii_letters
    numeros = string.digits
    caracter_especial = string.punctuation
    options = letras + numeros + caracter_especial
    
    password_user = ''
    
    for i in range(0,tamanho_senha):
        digits = random.choice(options)
        password_user += digits
    
    return password_user

# len_pass = input('Qual o tamanho da senha? ')

# if len_pass.isdigit():
#     len_pass = int(len_pass)
# else:
#     print('Informação inválida!')
#     quit()

# res = gerar_senha(tamanho_senha=len_pass)
# print(res)