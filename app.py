import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from flask import Flask, render_template, request, flash
import pymysql
import os

app = Flask(__name__)
app.secret_key = "af4e09990e02357d7410f1b683cc127a6fc69ad49eb9da62"

conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="emails"
)
cursor = conexao.cursor()

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
        
        # Caminho da imagem no sistema de arquivos
        caminho_imagem = os.path.join(app.root_path, 'static', 'img', 'anewslerner.webp')

        # Criação do objeto MIMEMultipart
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Impressão que Impressiona: Sua newsletter chegou"
        msg['From'] = login
        msg['To'] = email

        # Corpo do e-mail em HTML com a imagem incorporada
        html = f"""
            <html>
                <body>
                    <div>
                        <p>
                            Uso da impressão 3D aliada à realidade virtual permite o desenvolvimento do primeiro simulador de cirurgia craniana, em São Paulo.
                        </p>
                        <img src='cid:anewslerner' alt='newslerner'>
                        <p>
                            O Hospital das Clínicas da USP desenvolveu o primeiro simulador de cirurgia craniana, que alia o uso de um protótipo produzido por uma impressora 3D com tecnologia da realidade virtual. Inicialmente, um modelo de cérebro 3D foi impresso com resina, silicone e borracha, e em seguida, foi complementado com detalhes anatômicos produzidos a partir da realidade virtual, como pele e veias. A produção do protótipo se mostra um avanço na medicina, visto que permitiu que um estudo pré-cirúrgico fosse realizado pela equipe médica, evitando que erros ocorressem no procedimento feito no paciente humano. Ainda, tal tecnologia permitiu a substituição do uso de cadáveres reais para estudo, sendo uma alternativa promissora para hospitais e clínicas. Para receber mais informações sobre a impressão 3D na medicina, basta acessar o site www.impressaoqueimpressiona.com.br
                        </p>
                    </div>
                </body>
            </html>
        """

        # Adiciona o corpo do e-mail ao objeto MIMEMultipart
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        # Carrega a imagem e a anexa ao corpo do e-mail
        with open(caminho_imagem, 'rb') as imagem:
            imagem_anexada = MIMEImage(imagem.read())
            imagem_anexada.add_header('Content-ID', '<anewslerner>')
            msg.attach(imagem_anexada)

        # Estabelece conexão com o servidor SMTP e envia o e-mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(login, senha)
            server.sendmail(login, email, msg.as_string())

        return render_template('index.html')
    except pymysql.Error as e:
        conexao.rollback()
        flash(f"Erro ao inscrever: {str(e)}", "error")
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
