from flask import Flask 

app = Flask(__name__) #cria aplicação flask

@app.route('/') #define a função que vão responder as requisições feitas para a rota '/'
def home(): #função executada quando alguem apertar '/'
    return "Bom dia, Cris!" #resposta enviada 

if __name__ == '__main__': #roda o codigo so quando appy for iniciado
    app.run(host="0.0.0.0", port=8080) #inicia o servidor flask
