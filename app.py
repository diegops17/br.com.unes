from flask import Flask, render_template, request
from model import FaleConosco
import bd_dao as bd

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('quem-somos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        try:
            endereco_email = request.form['endereco_email']
            assunto = request.form['assunto']
            descricao = request.form['descricao']

            fale = FaleConosco(endereco_email, assunto, descricao)

        except:
            return f'Não foi possível enviar a mensagem!'
        else:
            sql = f"INSERT INTO faleconosco(email, assunto, descricao) " \
                  f"VALUES('{fale.endereco_email}','{fale.assunto}','{fale.descricao}')"

            bd.meu_cursor.execute(sql)
            bd.conexao.commit()

            return render_template('contato.html')
        finally:
            print(bd.meu_cursor.rowcount, 'linha(s) foram afetadas')
            #bd.fechar_conexao_banco()
    else:
        return render_template('contato.html')

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('erro404.html')

if __name__ == '__main__':
    app.run(debug=True)