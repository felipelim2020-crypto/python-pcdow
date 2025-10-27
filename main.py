class Animal:
    def __init__(self, nome, especie, idade, peso):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
    
    def info(self):
        return f"Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade} anos | Peso: {self.peso} kg"


class PetShop:
    def __init__(self):
        self.animais = []
    
    def adicionar_animal(self, animal):
        self.animais.append(animal)
        print(f"✅ {animal.nome} cadastrado com sucesso!")
    
    def listar_animais(self):
        if not self.animais:
            print("Nenhum animal cadastrado ainda.")
        else:
            print("\n🐾 Lista de Animais Cadastrados:")
            for i, animal in enumerate(self.animais, start=1):
                print(f"{i}. {animal.info()}")
    
    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome.lower() == nome.lower():
                self.animais.remove(animal)
                print(f"❌ {nome} removido com sucesso!")
                return
        print("Animal não encontrado.")


# Menu do Sistema
petshop = PetShop()

while True:
    print("\n===== PETSHOP SYSTEM =====")
    print("1 - Cadastrar Animal")
    print("2 - Listar Animais")
    print("3 - Remover Animal")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do animal: ")
        especie = input("Espécie: ")
        idade = int(input("Idade (anos): "))
        peso = float(input("Peso (kg): "))
        novo_animal = Animal(nome, especie, idade, peso)
        petshop.adicionar_animal(novo_animal)

    elif opcao == "2":
        petshop.listar_animais()

    elif opcao == "3":
        nome = input("Digite o nome do animal a remover: ")
        petshop.remover_animal(nome)

    elif opcao == "4":
        print("Encerrando o sistema... Até logo! 🐕👋")
        break

    else:
        print("Opção inválida! Tente novamente.")
