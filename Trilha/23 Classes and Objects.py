# Classes e Objetos sao usados para criar datatypes personlizado

# DEFINICAO:
    # classes: diagrama/modelo para criacao do objeto
    # objects: aquilo criado pela classe
# dentro de classes temos variaveis que chamamos de (attributes) e funcoes que chamamos de (methods)
    # determinam a propriedade e o comportamento do objeto dentro da classe


# CRIANDO CLASS:
class Movie:         # o nome da class deve ter iniciais das palavras compostas maiúsculas e não há espaços ou underscores
    
# CRIANDO OBJETO:
    # primeira coisa que fazemos é dar attributes para a classe e fazemos isso quando criamos uma funcao
    # Usando Initialization statement:
    def __init__(self,title,year,imdb_score,have_seen):             # self -> keyword | title, year, imdb_score, have_seen -> attributes
        self.title = title                                          # self refe-se ao objeto que estamos criando, pode ter outro nome
        self.year = year                                            # nesse bloco estamos atribuindo valores aos atributos da classe Movie
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    # Depois podemos adicionar mais metodos que formam o comportamento do objeto:
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)

    # Objetos (chamados instancias de classe) estao na forma: Movie()     *nome da class + ()    e podemos atribuir a uma variavel
film_1 = Movie("Life of Brian",1979,8.1,True)                       # aqui estamos entrando com dados que os valores dos atributos vao receber (igual funcao)                         
film_2 = Movie("The Holy Grail",1975,8.2,True)

print(film_1.title, film_1.imdb_score)
    # fica: Life of Brian 8.1
film_2.nice_print()         # Usando os argumentos do film_2 na funcao nice_print       EQUIVALENTE -> Movie.nice_print(film_2)
    # fica: Title:  The Holy Grail
    #       Year of production:  1975
    #       MDB Score:  8.2
    #       I have seen it:  True
    