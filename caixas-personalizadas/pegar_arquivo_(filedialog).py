from tkinter import filedialog,messagebox

# 1. Escolher uma pasta (askdirectory())
pasta = filedialog.askdirectory(
    title='Selecione uma pasta para salvar os relatórios'
)

if pasta:
    messagebox.showinfo(
        'Pasta escolhida',f'{pasta}'
    )

# 2. Abrir um arquivo (askopenfilename())
arquivo = filedialog.askopenfilename(
    title='Escolha um arquivo de texto',
    filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
)

if arquivo:
    messagebox.showinfo(
        'Arquivo selecionado',f'{arquivo}'
    )

# 3. Onde salvar um arquivo (asksaveasfilename())
salvar_arquivo = filedialog.asksaveasfilename(
    title=('Salvar arquivo como...'),
    defaultextension= '.txt',  # evita que o arquivo seja salvo sem extensão
    filetypes=[('Documento de texto','*.txt')]
)

if salvar_arquivo:
    messagebox.showinfo(
        'Local de salvamento',
        f'O arquivo será salvo em:\n{salvar_arquivo}'
    )