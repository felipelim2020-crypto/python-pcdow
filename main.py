class Pet:
    def __init__(self, nome, especie, idade, status):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.status = status
    
    def info(self):
        return f"Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade} anos | Status: {self.status}"


class SistemaPet:
    def __init__(self):
        self.pets = []
    
    def adicionar_pet(self, pet):
        self.pets.append(pet)
        print(f"✅ {pet.nome} cadastrado com sucesso!")
    
    def listar_pets(self):
        if not self.pets:
            print("Nenhum PET cadastrado ainda.")
        else:
            print("\n🐾 Lista de PETs:")
            for i, pet in enumerate(self.pets, start=1):
                print(f"{i}. {pet.info()}")


# Menu
sistema = SistemaPet()

while True:
    print("\n===== SISTEMA DE CONTROLE DE PETS =====")
    print("1 - Cadastrar PET")
    print("2 - Listar PETs")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do PET: ")
        especie = input("Espécie: ")
        idade = int(input("Idade: "))
        status = input("Status do PET (Aguardando, Em consulta, Atendido): ")
        novo_pet = Pet(nome, especie, idade, status)
        sistema.adicionar_pet(novo_pet)

    elif opcao == "2":
        sistema.listar_pets()

    elif opcao == "3":
        print("Saindo... 🐕👋")
        break

    else:
        print("Opção inválida!")

