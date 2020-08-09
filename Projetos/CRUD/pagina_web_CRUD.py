from flask import Flask

app = Flask(__name__)


@app.route("/")  # Define uma rota
def firstapp():
    return "<h1>Minha Primeira Pagina Web Com Flask</h1>" \
           "<br>" \
           "<h2>Eadeaeaeae</h2>"


if __name__ == "__main__":
    app.run()  # Roda a aplicação
