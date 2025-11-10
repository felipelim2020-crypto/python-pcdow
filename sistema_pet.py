class Pet:
    def __init__(self, nome, especie, idade, status):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.status = status
    
    def info(self):
        return f"{self.nome};{self.especie};{self.idade};{self.status}"

    def exibir(self):
        return f"Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade} anos | Status: {self.status}"


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.pets = []
    
    def adicionar_pet(self, pet):
        self.pets.append(pet)


class SistemaPet:
    def __init__(self):
        self.clientes = []
        self.carregar_dados()

    def salvar_dados(self):
        with open("pets.txt", "w") as arquivo:
            for cliente in self.clientes:
                for pet in cliente.pets:
                    linha = f"{cliente.nome};{cliente.telefone};{pet.info()}"
                    arquivo.write(linha + "\n")

    def carregar_dados(self):
        try:
            with open("pets.txt", "r") as arquivo:
                for linha in arquivo:
                    nome_cli, tel, nome_pet, especie, idade, status = linha.strip().split(";")
                    cliente_encontrado = None
                    
                    for c in self.clientes:
                        if c.nome == nome_cli:
                            cliente_encontrado = c
                            break
                    
                    if not cliente_encontrado:
                        cliente_encontrado = Cliente(nome_cli, tel)
                        self.clientes.append(cliente_encontrado)
                    
                    cliente_encontrado.adicionar_pet(Pet(nome_pet, especie, int(idade), status))

        except FileNotFoundError:
            pass
