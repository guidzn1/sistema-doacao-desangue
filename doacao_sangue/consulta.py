import tkinter as tk
import pymysql

class TelaConsulta:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Doadores")

        tk.Label(root, text="Digite o tipo sanguíneo:").pack()
        self.tipo_sanguineo_entry = tk.Entry(root)
        self.tipo_sanguineo_entry.pack()

        tk.Button(root, text="Buscar", command=self.buscar_doadores).pack()

        self.lista_doadores = tk.Listbox(root, width=50)
        self.lista_doadores.pack()

        # Conecção ao banco de dados MySQL
        self.conexao = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="doacaosangue4"
        )
        self.cursor = self.conexao.cursor()

    def buscar_doadores(self):
        tipo_sanguineo = self.tipo_sanguineo_entry.get()

        sql = "SELECT nome, endereco, contato FROM doacaosangue WHERE tipo_sanguineo = %s"
        self.cursor.execute(sql, (tipo_sanguineo,))

        doadores = self.cursor.fetchall()
        self.lista_doadores.delete(0, tk.END)  # Limpa a listbox antes de exibir os novos resultados

        if doadores:
            for doador in doadores:
                nome, endereco, contato = doador
                info = f"Nome: {nome} | Endereço: {endereco} | Contato: {contato}"
                self.lista_doadores.insert(tk.END, info)
        else:
            self.lista_doadores.insert(tk.END, "Nenhum doador encontrado com esse tipo sanguíneo.")


