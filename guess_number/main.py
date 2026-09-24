import tkinter as tk
import random
from tkinter import messagebox
from tkinter.font import Font

sorteio = 0
tentativas = 0

def iniciar():
    global sorteio,tentativas
    
    valor = answer1.get()
   
    if valor.isdigit():
            valor = int(valor)
            sorteio = random.randint(1,valor)
            tentativas = 0
            
            tit1.pack_forget()
            answer1.pack_forget()
            botao1.pack_forget()
            # trocando a tela
            
            tit2.pack(pady=(20,0))
            answer2.pack(pady=(20,0))
            botao2.pack(pady=(20,0))
            result.pack(pady=(20,0))
            dica.pack(pady=(10,0))
            
    else:
        messagebox.showerror(
            'Valor inválido',
            'Valor informado não é númerico. Tente novamente'
                )
        return

def to_guess():
    global tentativas
    
    palpite = answer2.get()
        
    if palpite.isdigit():
        palpite = int(palpite)
    else:
        messagebox.showerror(
            'Valor inválido',
            'Valor informado não é númerico. Tente novamente'
            )
        
    tentativas += 1
        
    if sorteio == palpite:
        result.config(
            text=f'Parábens!Você acertou. | Tentativas: {tentativas}',fg='green'
            )
        dica.pack_forget() # para remover a dica da tela
        botao2.config(state='disabled') # desativa o botão após a vitória
        
        botao3.pack(pady=(20,0))
    else:
        result.config(
            text='Você errou! Tente novamente',fg='red'
            )
        if palpite > sorteio:
            dica.config(
                text=f'{palpite} é maior',fg='red'
                )
        else:
            dica.config(
                text=f'{palpite} é menor',fg='red'
                )


def reiniciar():
    
    tit2.pack_forget()
    answer2.pack_forget()
    botao2.pack_forget()
    result.pack_forget()
    botao3.pack_forget()
    
    # deletar o que foi digitado 
    answer1.delete(0,tk.END)
    answer2.delete(0,tk.END)
    
    #ativar o botao2
    botao2.config(state='normal')
    
    result.config(text='')
    dica.config(text='')
    
    tit1.pack(pady=(20,0))
    answer1.pack(pady=(20,0))
    botao1.pack(pady=(20,0))
    

janela  = tk.Tk()

janela.title('Advinhe o número secreto')
janela.geometry('500x260')

#  Para o pegar o valor limite que o usuário informar
tit1 = tk.Label(
    janela,text='Até qual número o sorteio vai ser realizado? ',
    font=Font(size=14,weight='bold',family='Georgia')
    )
tit1.pack(pady=(20,0))

answer1 = tk.Entry(
    janela,width=8,
    font=Font(size=14,weight='normal',family='Cascadia Code')
   ) 
answer1.pack(pady=(20,0))

botao1 = tk.Button(
    janela,text='Começar',
    font=Font(size=12,weight='normal',family='Cascadia Code'),
    command=iniciar
    )

botao1.pack(pady=(20,0))

# --------------------------------------------------------------------------

tit2 = tk.Label(
    janela,text='Tente acertar o número secreto',
    font=Font(size=15,weight='bold',family='Georgia')
    )

result = tk.Label(
    janela,text='',
    font=Font(size=13,weight='normal',family='Cascadia Code')
    )
dica = tk.Label(
    janela,text='',
    font=Font(size=13,weight='normal',family='Cascadia Code') 
    )

answer2 = tk.Entry(
    janela,width=8,
    font=Font(size=14,weight='normal',family='Cascadia Code')
   ) 

botao2 = tk.Button(
    janela,text='Palpite',
    font=Font(size=12,weight='normal',family='Cascadia Code'),
    command=to_guess
    )

botao3 = tk.Button(
    text='Jogar novamente',
    font=Font(size=12,weight='normal',family='Cascadia Code'),
    command=reiniciar
    )

janela.mainloop()