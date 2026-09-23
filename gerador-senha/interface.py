import tkinter as tk
from tkinter.font import Font
from main import gerar_senha
from tkinter import messagebox

def gerar():
    
    tamanho = answer.get()
    
    if tamanho.isdigit():
        tamanho = int(tamanho)
    else:
        messagebox.showerror(
            'Valor inválido',
            'O valor informado não é númerico. Tente novamente.'
        )
        return

    res = gerar_senha(tamanho_senha=tamanho)
    
    if res:
        result.config(
            text=f'Senha gerada: {res}',fg='red'
            )
        

janela = tk.Tk()

janela.title('Gerador de senha')
janela.geometry('400x250')

titulo = tk.Label(
    janela,text='Qual o tamanho da senha?',
    font=Font(size=15,weight='normal',family='Cascadia Code')
    )
titulo.pack(pady=(10,0))

result = tk.Label(
    janela,text='',
    font=Font(size=15,weight='normal',family='Cascadia Code')
    )

answer = tk.Entry(
    janela,width=5,
    font=Font(size=12,weight='bold',family='Cascadia Code')
    )
answer.pack(pady=(30,0))


botao = tk.Button(
    janela,text='Gerar senha',
    font=Font(size=12,weight='normal',family='Cascadia Code'),
    command=gerar
    )

result.pack(pady=(30,0))
botao.pack(pady=(50,0))

janela.mainloop()