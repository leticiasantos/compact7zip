import py7zr
import os
import tkinter as tk
from tkinter import filedialog

def compactar_7zip(arquivos_selecionados, diretorio_destino):
    for arquivo in arquivos_selecionados:
        nome_arquivo = os.path.basename(arquivo)
        arquivo_destino = os.path.join(diretorio_destino, nome_arquivo + ".7z")
        
        print(f"Compactando {nome_arquivo}...")
        
        with py7zr.SevenZipFile(arquivo_destino, 'w') as archive:
            archive.write(arquivo, os.path.basename(arquivo))
        
        print(f"{nome_arquivo} compactado com sucesso!")

def selecionar_arquivos():
    arquivos_selecionados = filedialog.askopenfilenames()
    if arquivos_selecionados:
        diretorio_destino = filedialog.askdirectory()
        if diretorio_destino:
            compactar_7zip(arquivos_selecionados, diretorio_destino)
            print(f"Arquivos compactados em {diretorio_destino}")

# Crie uma janela de tkinter apenas para exibir o diálogo de seleção de arquivos
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

selecionar_arquivos()
