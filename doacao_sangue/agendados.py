import tkinter as tk
from tkinter import ttk
import pymysql

class Agendados:
    def __init__(self, root):
        self.root = root
        self.root.title("Agendamentos Registrados")

        self.tree = ttk.Treeview(root, columns=("Tipo Sanguíneo", "Data", "Horário", "Nome", "CPF"), show="headings")
        self.tree.heading("Tipo Sanguíneo", text="Tipo Sanguíneo")
        self.tree.heading("Data", text="Data")
        self.tree.heading("Horário", text="Horário")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("CPF", text="CPF")
        self.tree.pack()

        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"
        )
        self.cursor = self.conexao.cursor()

        self.exibir_agendamentos()

        self.cpf_entry = tk.Entry(root)
        self.cpf_entry.pack()
        retirar_button = tk.Button(root, text="Retirar", command=self.retirar_pessoa)
        retirar_button.pack()

    def exibir_agendamentos(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)

        self.cursor.execute("SELECT tipo_sanguineo, data, horario, nome, cpf FROM agendamento")
        agendamentos = self.cursor.fetchall()

        for agendamento in agendamentos:
            self.tree.insert("", "end", values=agendamento)

    def retirar_pessoa(self):
        cpf = self.cpf_entry.get()
        try:
            sql = "DELETE FROM agendamento WHERE cpf = %s"
            self.cursor.execute(sql, (cpf,))
            self.conexao.commit()
            print("Pessoa removida dos agendados com sucesso!")
            self.exibir_agendamentos()
        except Exception as e:
            print(f"Erro ao retirar pessoa dos agendados: {str(e)}")

