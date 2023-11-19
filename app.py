import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, flash, redirect
import pymysql

app = Flask(__name__)
app.secret_key = "af4e09990e02357d7410f1b683cc127a6fc69ad49eb9da62"  # Substitua pela sua chave secreta segura

# conexao = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="emails"
# )
# cursor = conexao.cursor()

#variaveis de ambiente para o envio do email
login = "impressaoqueimpressiona@gmail.com"
senha = "fwjmpogccpejwrmp"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/enviaremail', methods=['POST'])
def enviaremail():
    email = request.form['email']
    try:
        cursor.execute("INSERT INTO email (email) VALUES (%s)", (email,))
        conexao.commit()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Impressão que Impressiona: Sua newsletter chegou"
        msg['From'] = login
        msg['To'] = email
        html = f"<html><body><p>SUA NEWSLETTER CHEGOUUU</p></body></html>"
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        #estabelecendo conexão com o servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        #logando na conta google e enviando email
        server.login(login, senha)
        server.sendmail(login, email, msg.as_string())
    
        return render_template('index.html')
    except pymysql.Error as e:
        conexao.rollback()
        flash(f"Erro ao inscrever: {str(e)}", "error")
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
