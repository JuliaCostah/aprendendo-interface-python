import tkinter as tk
from tkinter.font import Font
from sistema import is_palindrome_recursive

def verify():    # função ponte
    palavra = word.get()
    res = is_palindrome_recursive(palavra)
    
    if res:
        resultado.config(text=f'{palavra} é um palíndromo',fg='green')
    else:
        resultado.config(text=f'{palavra} não é um palíndromo',fg='red')

    
janela = tk.Tk()

janela.title('É Palíndromo?')
janela.geometry("400x250")

titulo = tk.Label(
    text='Informe a palavra: ',
    font=Font(size=15,weight='normal',family='Cascadia Code')
    )

titulo.pack()

resultado = tk.Label(
    text="",font=Font(size=14,weight='bold',family='Cascadia Code')
    )

# Adicionando o botão

word = tk.Entry(
    janela,width=12,
    font=Font(size=14,weight='normal',family='Cascadia Code')
)

word.pack(pady=(30,30))

#  Adicionando o botão

verify = tk.Button(
    janela,text='Verificar',
    font=Font(size=12,weight='normal',family='Cascadia Code'),
    command=verify
    )

resultado.pack(pady=(0,20))
verify.pack(pady=(10,10))


janela.mainloop()