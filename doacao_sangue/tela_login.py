import tkinter as tk
from tkinter import messagebox
import pymysql
from datetime import datetime
from tkinter import ttk
from PIL import Image, ImageTk
from consulta import TelaConsulta
from agendamento import Agendamento
from agendados import Agendados
from relatorios import Relatorios
from atualiza import AtualizaDados


class TelaLogin:
    def __init__(self, root, sistema):
        self.sistema = sistema
        self.root = root
        self.root.title("Tela de Login")

        # Carregue o ícone a partir do arquivo "imagem_sangue.png"
        icon_image = Image.open("imagem_sangue.png")
        tamanho_desejado = (50, 50)
        icon_image.thumbnail(tamanho_desejado)
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Adicione o Label com o ícone
        icon_label = tk.Label(root, image=icon_photo)
        icon_label.photo = icon_photo
        icon_label.pack(anchor='nw', padx=150, pady=10)

        # Conecte-se ao banco de dados MySQL
        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"
        )
        self.cursor = self.conexao.cursor()

        # Labels e Entry para nome de usuário e senha
        tk.Label(root, text="Sistema De Doação de Sangue - HemoLife", font=("Helvetica", 12)).pack()

        tk.Label(root, text="Nome de Usuário:", font=("Helvetica", 8)).pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Senha:", font=("Helvetica", 8)).pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Botões para selecionar o tipo de usuário
        tk.Button(root, text="Login", command=self.login_funcionario).pack()
        tk.Button(root, text="Agendamento", command=self.login_agendamento).pack()

    def login_funcionario(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "admin":
            self.abrir_tela_cadastro()
            self.root.withdraw()  # Esconder a janela de login
        else:
            messagebox.showerror("Erro de Login", "Credenciais de funcionário inválidas")

    def login_agendamento(self):
        self.abrir_tela_agendamento()
        self.root.withdraw()  # Esconder a janela de login

    def abrir_tela_agendamento(self):
        root_agendamento = tk.Toplevel(self.root)
        app_agendamento = Agendamento(root_agendamento, self.root)  # Passar a referência da tela atual

    
    def abrir_tela_agendados(self):
        root_agendados = tk.Toplevel(self.root)
        app_agendados = Agendados(root_agendados, self.root)  # Passe a referência da tela atual
        self.root.withdraw()


    def abrir_tela_cadastro(self):
        janela_cadastro = tk.Toplevel(self.root)
        janela_cadastro.title("Tela de Cadastro")

        tk.Label(janela_cadastro, text="CPF do Doador:").pack()
        entry_cpf = tk.Entry(janela_cadastro)
        entry_cpf.pack()

        tk.Label(janela_cadastro, text="Nome do Doador:").pack()
        entry_nome = tk.Entry(janela_cadastro)
        entry_nome.pack()

        tk.Label(janela_cadastro, text="Data de Nascimento (DD/MM/YY):").pack()
        entry_data_nascimento = tk.Entry(janela_cadastro)
        entry_data_nascimento.pack()

        tk.Label(janela_cadastro, text="Gênero:").pack()
        generos = ["Masculino", "Feminino", "Outro"]
        combo_genero = ttk.Combobox(janela_cadastro, values=generos)
        combo_genero.pack()

        tk.Label(janela_cadastro, text="Endereço:").pack()
        entry_endereco = tk.Entry(janela_cadastro)
        entry_endereco.pack()

        tk.Label(janela_cadastro, text="Número de Contato:").pack()
        entry_contato = tk.Entry(janela_cadastro)
        entry_contato.pack()

        tk.Label(janela_cadastro, text="Tipo Sanguíneo:").pack()
        tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        combo_tipo_sanguineo = ttk.Combobox(janela_cadastro, values=tipos_sanguineos)
        combo_tipo_sanguineo.pack()

        btn_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", command=lambda: self.cadastrar_doador(
            entry_cpf.get(),
            entry_nome.get(),
            entry_data_nascimento.get(),
            combo_genero.get(),
            entry_endereco.get(),
            entry_contato.get(),
            combo_tipo_sanguineo.get()
        ))
        btn_cadastrar.pack()

        btn_consultar = tk.Button(janela_cadastro, text="Consultar", command=self.abrir_tela_consulta)
        btn_consultar.pack()

        btn_agendados = tk.Button(janela_cadastro, text="Agendados", command=self.abrir_tela_agendados)
        btn_agendados.pack()

        btn_relatorios = tk.Button(janela_cadastro, text="Relatórios", command=self.abrir_tela_relatorios)
        btn_relatorios.pack()

        btn_atualiza = tk.Button(janela_cadastro, text="Atualizar Cadastro", command=self.abrir_tela_atualiza)
        btn_atualiza.pack()


    def cadastrar_doador(self, entry_cpf, nome, data_nascimento, genero, endereco, contato, tipo_sanguineo):
        try:
            if data_nascimento:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            else:
                data_nascimento = None

            sql = "INSERT INTO doacaosangue (cpf, nome, data_nascimento, genero, endereco, contato, tipo_sanguineo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (entry_cpf, nome, data_nascimento, genero, endereco, contato, tipo_sanguineo)
            self.cursor.execute(sql, values)
            self.conexao.commit()

            messagebox.showinfo("Cadastro", f"Doador {nome} cadastrado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar doador: {str(e)}")

    def abrir_tela_consulta(self):
        root_consulta = tk.Toplevel(self.root)
        app_consulta = TelaConsulta(root_consulta)  # Crie a instância da tela de consulta
        # Você também pode chamar métodos específicos ou adicionar lógica à tela de consulta se necessário
        self.root.withdraw()  # Esconder a janela de login

    def abrir_tela_relatorios(self):
        root_relatorios = tk.Toplevel(self.root)
        app_relatorios = Relatorios(root_relatorios, self.root)  # Abre a tela de relatórios
        self.root.withdraw()  # Esconde a janela de login

    def abrir_tela_atualiza(self):
        root_atualiza = tk.Toplevel(self.root)
        app_atualiza = AtualizaDados(root_atualiza)  # Cria a instância para atualizar dados
        self.root.withdraw()  

