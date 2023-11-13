import tkinter as tk
import pymysql

class AtualizaDados:
    def __init__(self, root):
        self.root = root
        self.root.title("Atualizar Dados do Doador")

        # Frame para organizar visualmente os widgets
        self.form_frame = tk.Frame(root)
        self.form_frame.pack()

        # Widgets para receber o CPF e buscar o doador
        tk.Label(self.form_frame, text="Digite o CPF do doador:").grid(row=0, column=0, pady=5)
        self.cpf_entry = tk.Entry(self.form_frame)
        self.cpf_entry.grid(row=0, column=1, pady=5)
        tk.Button(self.form_frame, text="Buscar", command=self.buscar_doador).grid(row=0, column=2, pady=5)

        # Frame para exibir as informações do doador
        self.info_frame = tk.Frame(root)
        self.info_frame.pack()

        # Labels para exibir informações do doador
        tk.Label(self.info_frame, text="Nome:").grid(row=0, column=0, pady=5)
        self.info_nome = tk.Label(self.info_frame, text="")
        self.info_nome.grid(row=0, column=1, pady=5)

        tk.Label(self.info_frame, text="Endereço atual:").grid(row=1, column=0, pady=5)
        self.info_endereco = tk.Label(self.info_frame, text="")
        self.info_endereco.grid(row=1, column=1, pady=5)

        tk.Label(self.info_frame, text="Contato atual:").grid(row=2, column=0, pady=5)
        self.info_contato = tk.Label(self.info_frame, text="")
        self.info_contato.grid(row=2, column=1, pady=5)

        # Widgets para inserir os novos dados
        tk.Label(root, text="Novos dados:", font=("Helvetica", 15)).pack()

        tk.Label(root, text="_____________________________________", font=("Helvetica", 10)).pack()

        tk.Label(root, text="Novo Endereço:", font=("Helvetica", 10)).pack()

        self.novo_endereco = tk.Entry(root)
        self.novo_endereco.pack()

        tk.Label(root, text="Novo Contato:", font=("Helvetica", 10)).pack()

        self.novo_contato = tk.Entry(root)
        self.novo_contato.pack()

        # Botão para atualizar os dados
        tk.Button(root, text="Atualizar", command=self.atualizar_dados, bg="lightblue").pack()

        # Conexão ao banco de dados MySQL
        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"
        )
        self.cursor = self.conexao.cursor()

    def buscar_doador(self):
        cpf = self.cpf_entry.get()

        sql = "SELECT nome, endereco, contato FROM doacaosangue WHERE cpf = %s"
        self.cursor.execute(sql, (cpf,))
        doador = self.cursor.fetchone()

        if doador:
            self.info_nome.config(text=doador[0])
            self.info_endereco.config(text=doador[1])
            self.info_contato.config(text=doador[2])
        else:
            self.info_nome.config(text="Não encontrado")
            self.info_endereco.config(text="Não encontrado")
            self.info_contato.config(text="Não encontrado")

    def atualizar_dados(self):
        cpf = self.cpf_entry.get()
        novo_endereco = self.novo_endereco.get()
        novo_contato = self.novo_contato.get()

        sql = "UPDATE doacaosangue SET endereco = %s, contato = %s WHERE cpf = %s"
        values = (novo_endereco, novo_contato, cpf)
        self.cursor.execute(sql, values)
        self.conexao.commit()
