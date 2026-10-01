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
        if altura < 0.5 and altura > 2.5:
            erros.append('A altura deve estar entre 0.5 e 2.5.')


        if erros:
            for erro in erros:
                flash(erro, 'danger')

            # return redirect(url_for('pagina_inicial', erros = erros))
            return render_template('index.html', erros = erros)


        faixa = ''
        imc = (peso / (altura * altura))

        if imc < 18.5:
            faixa = 'Abaixo do peso'
        elif imc >= 18.5 and imc < 25:
            faixa = 'Peso normal'
        elif imc >= 25 and imc < 30:
            faixa = 'Sobrepeso'
        else:
            faixa = 'Obesidade'

            return render_template('index.html', imc = imc, nome = nome, peso = peso, altura = altura, faixa = faixa)
            # return redirect(url_for('pagina_inicial', imc = imc, nome = nome, peso = peso, altura = altura, faixa = faixa))

    if request.method == 'GET':
        return render_template('index.html')

@app.route('/equipe', methods=['GET','POST'])
def equipe():
    return render_template('equipe.html')





if __name__ == '__main__':
    app.run(debug=True)