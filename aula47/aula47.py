import sqlite3 
from sqlite3 import Error

'''Criar Conexaõ'''
def ConexaoBanco():
    
    path="aula_python\\banco\\agenda.db"
    con=None
    
    try:
        con=sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

'''Criar Tabela'''
vsql="""CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""
def criarTabela(conexao,sql):

    try:
        conTabela=conexao.cursor()
        conTabela.execute(sql)
        print("Tabela criada com sucesso!")
    except Error as ex:
        print(ex)
    return conTabela

criarTabela(vcon, vsql)

vcon.close()