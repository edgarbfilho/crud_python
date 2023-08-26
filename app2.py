from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '123321'


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)



cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return render_template('index.html', clientes=clientes)

@app.route('/add', methods=['POST'])
def add_cliente():
    nome = request.form['nome']
    email = request.form['email']
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (nome, email))
    db.commit()
    flash('Cliente adicionado com sucesso', 'success')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit_cliente(id):
    if request.method == 'POST':
        novo_nome = request.form['nome']
        novo_email = request.form['email']
        cursor.execute("UPDATE clientes SET nome=%s, email=%s WHERE id=%s", (novo_nome, novo_email, id))
        db.commit()
        flash('Cliente atualizado com sucesso', 'success')
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM clientes WHERE id=%s", (id,))
        cliente = cursor.fetchone()
        cliente_dict = {'id': cliente['id'], 'nome': cliente['nome'], 'email': cliente['email']}
        return render_template('edit.html', cliente=cliente_dict)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_cliente(id):
    cursor.execute("SELECT * FROM clientes WHERE id=%s", (id,))
    cliente = cursor.fetchone()

    if cliente:
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
        db.commit()
        flash('Cliente excluído com sucesso', 'success')
    else:
        flash('Cliente não encontrado', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)