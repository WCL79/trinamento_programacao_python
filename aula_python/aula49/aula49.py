import sqlite3 
from sqlite3 import Error

'''Criar Conexão'''
def ConexaoBanco():
    
    path="aula_python\\banco\\agenda.db"
    con=None
    
    try:
        con=sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

'''Inserir dados na Tabela'''
def inserir(conexao, sql):

    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados inseridos na tabela contato!")
    except Error as ex:
        print(ex)

#vsql="""INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)VALUES('Nome_Teste', 'Fone_de_Teste', 'teste@stefanini.com');"""
nome=input("Infome seu nome:")
telefone=input("Informe telefone para contato:")
email=input("Informe email:")

#vsql="INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES ('"+nome+"', '"+telefone+"', '"+email+"')"

#inserir(vcon, vsql)

'''Excluir dados na Tabela'''
def excluir(conexao, sql):

    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido!")
vsql="DELETE"
excluir(vcon, vsql)
        