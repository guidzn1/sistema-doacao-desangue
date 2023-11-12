import tkinter as tk
from tkinter import ttk
from datetime import date
import pymysql

class Agendamento:
    def __init__(self, root):
        self.root = root
        self.root.title("Agendamento de Doação")

        # Interface para agendamento
        tk.Label(root, text="Tipo Sanguíneo:").pack()
        tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Não sei"]
        combo_tipo_sanguineo = ttk.Combobox(root, values=tipos_sanguineos)
        combo_tipo_sanguineo.pack()

        tk.Label(root, text="Data (dd-mm-yyyy):").pack()
        entry_data = tk.Entry(root)
        entry_data.pack()

        # Define a data atual no campo de data
        data_atual = date.today().strftime("%d-%m-%Y")  # Obtém a data no formato dd-mm-yyyy
        entry_data.insert(0, data_atual)  # Insere a data no Entry da interface

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

        # Conectando ao banco de dados
        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"  # Nome do seu banco de dados
        )
        self.cursor = self.conexao.cursor()

    def agendar_doacao(self, tipo_sanguineo, data, horario, nome, cpf):
        try:
            # Converter a data para o formato aceitável pelo banco de dados (yyyy-mm-dd)
            data_formatada = self.converter_data_formato(data)
            
            # Inserir dados na tabela 'agendamento'
            sql = "INSERT INTO agendamento (tipo_sanguineo, data, horario, nome, cpf) VALUES (%s, %s, %s, %s, %s)"
            values = (tipo_sanguineo, data_formatada, horario, nome, cpf)
            self.cursor.execute(sql, values)
            self.conexao.commit()
            print("Doação agendada com sucesso!")
        except Exception as e:
            print(f"Erro ao agendar doação: {str(e)}")
            
    def converter_data_formato(self, data):
        # Converte a data do formato dd-mm-yyyy para yyyy-mm-dd
        partes_data = data.split("/")
        data_formatada = f"{partes_data[2]}-{partes_data[1]}-{partes_data[0]}"
        return data_formatada
