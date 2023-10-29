import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bd_unes',
)

meu_cursor = conexao.cursor()

def fechar_conexao_banco():
    conexao.close()
    meu_cursor.close()


'''
#create database bd_unes;

#use bd_unes;

/*create table faleconosco(
	id integer not null auto_increment,
    email varchar(100), 
    assunto varchar(100),
    descricao varchar(500),
	primary key(id)
);*/

select * from faleconosco;
'''