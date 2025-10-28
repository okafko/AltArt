from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'eg',
    'port': '3306'
}

# Rota raiz redireciona para login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Rota de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        username = request.form['username']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuario WHERE username_usuario = %s OR email_usuario = %s", (username, email))
        if cursor.fetchone():
            flash("Nome de usuário ou email já cadastrado.", "erro")
            cursor.close()
            conn.close()
            return redirect(url_for('cadastro'))

        cursor.execute("""
            INSERT INTO usuario (nome_usuario, username_usuario, password_usuario, email_usuario)
            VALUES (%s, %s, %s, %s)
        """, (nome, username, senha, email))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Cadastro realizado com sucesso! Você já pode fazer login.", "sucesso")
        return redirect(url_for('login'))

    return render_template('cadastro.html')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        senha = request.form['senha'].strip()

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE username_usuario = %s", (username,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        if usuario and check_password_hash(usuario['password_usuario'], senha):
            if not usuario['conta_ativa']:
                flash("Esta conta está desativada.", "erro")
                return redirect(url_for('login'))

            session['usuario_id'] = usuario['cod_usuario']
            session['usuario_nome'] = usuario['nome_usuario']
            return redirect(url_for('index'))  # Redireciona para index.html
        else:
            flash("Usuário ou senha inválidos.", "erro")
            return redirect(url_for('login'))

    return render_template('login.html')

# Página principal após login
@app.route('/index')
def index():
    if 'usuario_id' not in session:
        flash("Você precisa fazer login.", "erro")
        return redirect(url_for('login'))
    return render_template('index.html', nome=session['usuario_nome'])

# Logout
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    flash("Você saiu da sua conta.", "sucesso")
    return redirect(url_for('login'))

@app.route('/paises')
def paises():
    return render_template('paises.html')

@app.route('/comidas')
def comidas():
    return render_template('comidas.html')

@app.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')




if __name__ == '__main__':
    app.run(debug=True)

