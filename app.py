from flask import Flask, render_template

# Cria a instância da aplicação Flask
# __name__ é uma variável especial do Python que contém o nome do módulo atual
# O Flask usa isso para saber onde procurar os templates e arquivos estáticos
app = Flask(__name__)


# O decorador @app.route define qual URL aciona esta função
# '/' é a rota raiz — o endereço principal do site (ex: http://localhost:5000/)
@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')





if __name__ == '__main__':
    app.run(debug=True)