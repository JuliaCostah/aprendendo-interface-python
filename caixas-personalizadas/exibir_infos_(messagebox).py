from tkinter import messagebox  

#  Exibindo uma informação
messagebox.showinfo(
    'Download Concluído',
    'Arquivo salvo com sucesso'
)
#  Um aviso
messagebox.showwarning(
    'Atenção: Bateria fraca',
    'A sua bateria está em 10%. Conecte o carregador.'
)
#  Um erro
messagebox.showerror(
    'Erro de conexão',
    'Não foi possível conectar ao servidor. Verifique sua conexão com a internet.'
)