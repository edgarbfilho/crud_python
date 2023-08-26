from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Minha Página em Flask</title>
    </head>
    <body>
        <h1>Olá, mundo!</h1>
        <p>Esta é a minha primeira página web em Flask.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
