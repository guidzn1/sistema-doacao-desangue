import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Importe o widget de calendário
from datetime import date
import pymysql

class Agendamento:
    def __init__(self, root, tela_anterior):
        self.root = root
        self.root.title("Agendamento de Doação")
        self.tela_anterior = tela_anterior  # Adicione a referência à tela anterior

        tk.Label(root, text="Tipo Sanguíneo:").pack()
        tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Não sei"]
        combo_tipo_sanguineo = ttk.Combobox(root, values=tipos_sanguineos)
        combo_tipo_sanguineo.pack()

        tk.Label(root, text="Data:").pack()
        entry_data = DateEntry(root, date_pattern="dd-mm-yyyy", locale="pt_BR")
        entry_data.pack()

        tk.Label(root, text="Horário:").pack()
        entry_horario = tk.Entry(root)
        entry_horario.pack()

        tk.Label(root, text="Nome:").pack()
        entry_nome = tk.Entry(root)
        entry_nome.pack()

        tk.Label(root, text="CPF:").pack()
        entry_cpf = tk.Entry(root)
        entry_cpf.pack()

        btn_agendar = tk.Button(root, text="Agendar", command=lambda: self.agendar_doacao(
            combo_tipo_sanguineo.get(),
            entry_data.get(),
            entry_horario.get(),
            entry_nome.get(),
            entry_cpf.get()
        ))
        btn_agendar.pack()

        btn_voltar = tk.Button(root, text="Voltar", command=self.voltar_tela_anterior)
        btn_voltar.pack()

        # Conectando ao banco de dados
        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"
        )
        self.cursor = self.conexao.cursor()

    def agendar_doacao(self, tipo_sanguineo, data, horario, nome, cpf):
        try:
            data_formatada = self.converter_data_formato(data)
            sql = "INSERT INTO agendamento (tipo_sanguineo, data, horario, nome, cpf) VALUES (%s, %s, %s, %s, %s)"
            values = (tipo_sanguineo, data_formatada, horario, nome, cpf)
            self.cursor.execute(sql, values)
            self.conexao.commit()
            print("Doação agendada com sucesso!")
        except Exception as e:
            print(f"Erro ao agendar doação: {str(e)}")

    def converter_data_formato(self, data):
        partes_data = data.split("-")
        data_formatada = f"{partes_data[2]}-{partes_data[1]}-{partes_data[0]}"
        return data_formatada

    def voltar_tela_anterior(self):
        self.tela_anterior.deiconify()
        self.root.destroy()
