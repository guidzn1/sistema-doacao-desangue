import tkinter as tk
from tkinter import ttk
import pymysql

class Relatorios:
    def __init__(self, root, tela_anterior):
        self.root = root
        self.root.title("Relatório de Tipos Sanguíneos")
        self.tela_anterior = tela_anterior  # Referência à tela anterior

        self.tree = ttk.Treeview(root, columns=("Tipo Sanguíneo", "Quantidade"), show="headings")
        self.tree.heading("Tipo Sanguíneo", text="Tipo Sanguíneo")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.pack()

        btn_gerar_relatorio = tk.Button(root, text="Gerar Relatório", command=self.gerar_relatorio)
        btn_gerar_relatorio.pack()

        btn_voltar = tk.Button(root, text="Voltar", command=self.voltar_tela_anterior)
        btn_voltar.pack()

        # Conexão com o banco de dados
        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"
        )
        self.cursor = self.conexao.cursor()

    def gerar_relatorio(self):
        self.tree.delete(*self.tree.get_children())  # Limpa as entradas da Treeview

        sql = "SELECT tipo_sanguineo, COUNT(*) AS quantidade FROM doacaosangue GROUP BY tipo_sanguineo"
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()

        for tipo, quantidade in resultados:
            self.tree.insert("", "end", values=(tipo, quantidade))

    def voltar_tela_anterior(self):
        self.tela_anterior.deiconify()  # Reexibir a tela anterior
        self.root.destroy()  # Fechar a tela de relatórios
