from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ==============================
# CLASSES
# ==============================
class Pet:
    def __init__(self, nome, especie, idade, status):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.status = status

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.pets = []

    def adicionar_pet(self, pet):
        self.pets.append(pet)

# ==============================
# SISTEMA
# ==============================
class SistemaPet:
    def __init__(self):
        self.clientes = []
        self.carregar_dados()

    def salvar_dados(self):
        with open("pets.txt", "w", encoding="utf-8") as arquivo:
            for cliente in self.clientes:
                for pet in cliente.pets:
                    linha = f"{cliente.nome};{cliente.telefone};{pet.nome};{pet.especie};{pet.idade};{pet.status}\n"
                    arquivo.write(linha)

    def carregar_dados(self):
        try:
            with open("pets.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    nome_cli, tel, nome_pet, especie, idade, status = linha.strip().split(";")
                    cliente = next((c for c in self.clientes if c.nome == nome_cli), None)
                    if not cliente:
                        cliente = Cliente(nome_cli, tel)
                        self.clientes.append(cliente)
                    cliente.adicionar_pet(Pet(nome_pet, especie, idade, status))
        except FileNotFoundError:
            pass

    def excluir_cliente(self, nome):
        self.clientes = [c for c in self.clientes if c.nome != nome]
        self.salvar_dados()

    def editar_cliente(self, nome_antigo, novo_nome, novo_tel):
        for cliente in self.clientes:
            if cliente.nome == nome_antigo:
                cliente.nome = novo_nome
                cliente.telefone = novo_tel
                break
        self.salvar_dados()


sistema = SistemaPet()

# ==============================
# ROTAS
# ==============================

@app.route('/')
def index():
    return render_template('index.html', clientes=sistema.clientes)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome_cliente = request.form['nome_cliente']
    telefone = request.form['telefone']
    nome_pet = request.form['nome_pet']
    especie = request.form['especie']
    idade = request.form['idade']
    status = request.form['status']

    cliente = next((c for c in sistema.clientes if c.nome == nome_cliente), None)
    if not cliente:
        cliente = Cliente(nome_cliente, telefone)
        sistema.clientes.append(cliente)

    cliente.adicionar_pet(Pet(nome_pet, especie, idade, status))
    sistema.salvar_dados()

    return redirect('/')

@app.route('/excluir/<nome>')
def excluir(nome):
    sistema.excluir_cliente(nome)
    return redirect('/')

@app.route('/editar/<nome>', methods=['GET', 'POST'])
def editar(nome):
    cliente = next((c for c in sistema.clientes if c.nome == nome), None)
    if not cliente:
        return redirect('/')

    if request.method == 'POST':
        novo_nome = request.form['novo_nome']
        novo_tel = request.form['novo_tel']
        sistema.editar_cliente(nome, novo_nome, novo_tel)
        return redirect('/')

    return render_template('editar.html', cliente=cliente)

if __name__ == '__main__':
    app.run(debug=True)

