import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

class TelaPrincipal:
    def __init__(self, root, sistema):
        self.sistema = sistema
        self.root = root
        self.root.title("Tela Principal")

        # Adicione widgets para a tela principal, como botões e outras funcionalidades
        tk.Button(root, text="Pesquisar Doadores", command=self.pesquisar_doadores).pack()
        tk.Button(root, text="Cadastrar Doador", command=self.abrir_tela_cadastro).pack()

        # Botão para pesquisa de doadores por tipo sanguíneo
        tk.Label(root, text="Pesquisar por Tipo Sanguíneo:", font=("Helvetica", 8)).pack()
        self.tipo_sanguineo_entry = tk.Entry(root)
        self.tipo_sanguineo_entry.pack()
        tk.Button(root, text="Pesquisar", command=self.pesquisar_doadores).pack()

    def pesquisar_doadores(self):
        tipo_sanguineo = self.tipo_sanguineo_entry.get()
        doadores_encontrados = self.sistema.consultar_doadores_por_tipo_sanguineo(tipo_sanguineo)

        # Exibir os doadores encontrados em uma janela ou caixa de diálogo
        # Você pode implementar essa parte para mostrar os resultados na interface gráfica
        # por meio de uma nova janela, caixa de diálogo ou outra forma que preferir.
        # Por exemplo:
        resultado = "Doadores Encontrados:\n\n"
        for doador in doadores_encontrados:
            resultado += f"Nome: {doador.nome}\nEndereço: {doador.endereco}\nContato: {doador.contato}\n\n"

        messagebox.showinfo("Resultados da Pesquisa", resultado)

    def abrir_tela_cadastro(self):
        # Implemente a lógica para abrir a tela de cadastro de doadores aqui
