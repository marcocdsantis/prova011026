from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():

    if request.method == 'POST':
        nome = request.form.get('nome')
        peso = request.form.get('peso')
        altura = request.form.get('altura')

        nome = nome
        peso = float(peso)  
        altura = float(altura)

        erros = []

        if not nome:
            erros.append('O nome é obrigatório.')
        elif len(nome) < 3:
            erros.append('O nome deve ter pelo menos 3 caracteres.')

        if not peso:
            erros.append('O peso é obrigatório.')
        if peso <= 0:
            erros.append('O peso deve ser maior que 0.')

        if not altura:
            erros.append('A altura é obrigatória.')
        if altura < 0.5 or altura > 2.5:
            erros.append('A altura deve estar entre 0.5 e 2.5.')


        if erros:
            for erro in erros:
                flash(erro, 'danger')

            return render_template('index.html', erros = erros)


        faixa = ''
        cor = ''
        imc = (peso / (altura * altura))

        if imc < 18.5:
            faixa = '🔵 Abaixo do peso'
            cor = 'alert-info'
        elif imc >= 18.5 and imc < 25:
            faixa = '🟢 Peso normal'
            cor = 'alert-success'
        elif imc >= 25 and imc < 30:
            faixa = '🟡 Sobrepeso'
            cor = 'alert-warning'
        else:
            faixa = '🔴 Obesidade'
            cor = 'alert-danger'

            return render_template('index.html', imc = imc, nome = nome, peso = float(peso), altura = float(altura), faixa = faixa, cor= cor)

    if request.method == 'GET':
        return render_template('index.html')

@app.route('/equipe', methods=['GET','POST'])   
def equipe():
    return render_template('equipe.html')





if __name__ == '__main__':
    app.run(debug=True)