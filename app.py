from flask import Flask, app, render_template, request
import pymysql

app = Flask(__name__)
conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="emails"
)
cursor = conexao.cursor()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/enviaremail', methods=['POST'])
def enviaremail():
    
    email = request.form['email']
    try:
        cursor.execute("INSERT INTO email (email) VALUES (%s)", (email,))
        conexao.commit()
        
        return render_template('sucess.html', email=email)
    except pymysql.Error as e:
        conexao.rollback()
        return f"Erro ao inscrever: {str(e)}"

if __name__ == 'main':
    app.run(debug=True)