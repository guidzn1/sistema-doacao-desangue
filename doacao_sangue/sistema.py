import tkinter as tk
import pymysql
from tkinter import messagebox
from tkcalendar import DateEntry 



class Doador:
    def __init__(self,cpf, nome, data_nascimento, genero, endereco, contato, tipo_sanguineo):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.endereco = endereco
        self.contato = contato
        self.tipo_sanguineo = tipo_sanguineo

class SistemaDoacaoSangue:
    def __init__(self):
        self.doadores = []

    def cadastrar_doador(self, doador):
        self.doadores.append(doador)

    def atualizar_dados_doador(self, nome, novo_endereco, novo_contato):
        for doador in self.doadores:
            if doador.nome == nome:
                doador.endereco = novo_endereco
                doador.contato = novo_contato

    def consultar_doadores_por_tipo_sanguineo(self, tipo_sanguineo):
        doadores_por_tipo = [doador for doador in self.doadores if doador.tipo_sanguineo == tipo_sanguineo]
        return doadores_por_tipo

    def visualizar_perfil_doador(self, nome):
        for doador in self.doadores:
            if doador.nome == nome:
                return f"Nome: {doador.nome}\nData de Nascimento: {doador.data_nascimento}\nGênero: {doador.genero}\nEndereço: {doador.endereco}\nNúmero de Contato: {doador.contato}\nTipo Sanguíneo: {doador.tipo_sanguineo}"

    def buscar_doadores_por_tipo_sanguineo(self, tipo_sanguineo):
        # Criar uma lista para armazenar os doadores correspondentes
        doadores_encontrados = []

        # Iterar sobre a lista de doadores
        for doador in self.doadores:
            if doador.tipo_sanguineo == tipo_sanguineo:
                # Se o tipo sanguíneo do doador corresponder ao tipo sanguíneo pesquisado,
                # adicione o doador à lista de doadores encontrados
                doadores_encontrados.append(doador)

        # Retornar a lista de doadores encontrados
        return doadores_encontrados



