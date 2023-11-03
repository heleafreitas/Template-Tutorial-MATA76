from flask import Flask, redirect, render_template, request, url_for
import bd_tutorial as db

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    pass

@app.route('/filtrar', methods=['POST'])
def filtrar():
    pass

@app.route('/iniciar_tarefa/<string:id>', methods=['POST','GET'])
def iniciar_tarefa(id):
    pass

@app.route('/finalizar_tarefa/<string:id>', methods=['POST','GET'])
def finalizar_tarefa(id):
    pass

@app.route('/deletar_tarefa/<string:id>', methods=['POST','GET'])
def deletar_tarefa(id):
    pass

@app.route('/editar_tarefa/<string:id>', methods=['POST','GET'])
def editar_tarefa(id):
    pass

@app.route('/atualizar/<string:id>', methods=['POST','GET'])
def atualizar(id):
    pass

@app.route('/irParaAdicionar', methods=['POST'])
def irParaAdicionar():
    pass

@app.route('/register')
def registrar_atividade():
   pass

@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    pass
    
    return redirect(url_for('home'))

def listarTarefas(select):
    pass

app.run(debug=True)

    