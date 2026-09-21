from tkinter import simpledialog, messagebox

#  Solicitando um texto (askstring())
nome = simpledialog.askstring(
    'Cadastro','Seu Nome:'
).title().strip()

# Solicitando um num inteiro (askinteger())
idade = simpledialog.askinteger(
    'Idade','Sua Idade: ',
    minvalue = 1,maxvalue = 110   # valor minimo e maximo
)

# Solicitando um decimal (askfloat())
altura = simpledialog.askfloat(
    'Altura','Sua Altura em metros (ex:. 1.67)'
)

if nome and idade and altura:
    messagebox.showinfo(
        'Ficha Cadastral',
        f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m'
    )