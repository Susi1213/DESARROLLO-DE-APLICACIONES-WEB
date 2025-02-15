from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenida Personalizado!"

if __name__ == "__main__":
    app.run(debug=True)
