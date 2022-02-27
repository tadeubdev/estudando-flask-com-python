from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


@app.route('/usuarios/<slug>')
def usuarios(slug):
    return render_template('usuarios.html', slug=slug)


if __name__ == '__main__':
    app.run(debug=True)
