# HERANCA DE CLASSES
# Aqui temos uma classe normal
class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")
character1=Person()       
character1.move()                           # fica: Moves 4 paces

# Aqui temos uma classe que herda a classe anterior
class Doctor(Person):                       # (Person) -> possibilita que a classe Doctor herde todos os atributos e metodos da classe base
    def heal(self):                         # possui seus proprios metodos
        print("Heals 10 health points")
character1=Doctor()
character1.heal()                           # fica: Heals 10 health points

# Terceira classe que possui a mesma funcao que a sua classe base
class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Moves 6 paces")
character1=Fighter()
character1.move()                           # fica: Moves 6 paces

# Quarta classe que herda uma classe que ja e herdeira 
class Wizard(Doctor):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heals 15 health points")
character1=Wizard()
character1.move()                           # fica: Moves 4 paces   -> Herdado de Person

# A quarta classe mas com duas herancas
# class Wizard(Doctor,Fighter):
#     def cast_spell(self):
#         print("Turns invisble")
#     def heal(self):
#         print("Heals 15 health points")
# character1=Wizard() 
# character1.move()                           # fica: Moves 6 paces   -> Person e Fighter possuem o metodo move mas como Fighter esta mais proximo na heranca Wizard herda o metodo de Fighter

# Caso Doctor e Fighter tenham o mesmo metodo o escolhido sera o do Doctor pois este esta na frente de Fighter

# COM INIT
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)           # Utilizamos o método super().__init__() para chamar o construtor da classe Pessoa e passar os valores para os atributos nome e idade.
        self.matricula = matricula
        