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
        self.pets = []  # Lista com os pets desse cliente
    
    def adicionar_pet(self, pet):
        self.pets.append(pet)


class SistemaPet:
    def __init__(self):
        self.clientes = []  # Agora vai armazenar os Clientes
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

    def cadastrar_cliente(self):
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        novo_cliente = Cliente(nome, telefone)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        print(f"✅ Cliente {nome} cadastrado!")

    def cadastrar_pet(self):
        if not self.clientes:
            print("⚠ Nenhum cliente cadastrado!")
            return
        
        print("\nSelecione o dono do PET:")
        for i, c in enumerate(self.clientes, start=1):
            print(f"{i}. {c.nome}")
        escolha = int(input("Escolha: ")) - 1

        cliente_escolhido = self.clientes[escolha]

        nome = input("Nome do PET: ")
        especie = input("Espécie: ")
        idade = int(input("Idade: "))
        status = input("Status do PET: ")

        novo_pet = Pet(nome, especie, idade, status)
        cliente_escolhido.adicionar_pet(novo_pet)
        self.salvar_dados()
        print(f"🐾 PET {nome} cadastrado para {cliente_escolhido.nome}!")

    def listar_pets(self):
        for cliente in self.clientes:
            print(f"\n📌 Cliente: {cliente.nome} ({cliente.telefone})")
            if not cliente.pets:
                print("Nenhum PET cadastrado.")
            else:
                for pet in cliente.pets:
                    print("  - " + pet.exibir())


sistema = SistemaPet()

while True:
    print("\n===== SISTEMA PET - ITERAÇÃO 3 =====")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar PET para um Cliente")
    print("3 - Listar Clientes e PETs")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        sistema.cadastrar_cliente()
    elif opcao == "2":
        sistema.cadastrar_pet()
    elif opcao == "3":
        sistema.listar_pets()
    elif opcao == "4":
        print("Encerrando o sistema! 🐕👋")
        break
    else:
        print("⚠ Opção inválida!")
