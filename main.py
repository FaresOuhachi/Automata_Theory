import re

class Word_miroir:

    def __init__(self,word: str):
        self.word = word

    def reverse_word(self):
        print(f"Le mot miroir du {self.word} est: {self.word[::-1]}")


# Demander la partie voulue du programme
class Word_puissance:

    def __init__(self,word:str,n:int):
        self.word = word
        self.n = n

    def puissance(self):
        return self.word * self.n

    def show_puissance(self):
        print(f"La puissance {self.n} du mot {self.word} est: {self.puissance()}")


class Generator:

    def __init__(self,n:int ):

        assert n > 0 , "N est inférieur a 0 !!"

        self.longeur = n

        self.P = {

            'S' : ['AB'],
            'A' : ['aA','bA','ab'],
            'B' : ['bC'],
            'C' : ['aC','bC','']
        }

        self.mots = set()



    def possiblities(self,word):

        if (len(word) > self.longeur):
            return

        match = re.search('[ABC]', word)

        if match:

            for i in list(word):

                if i == 'A' or i == 'B' or i == 'C':

                    for j in self.P.get(i):

                        self.possiblities(word.replace(i, j))
        else:

            if word not in self.mots:
                self.mots.add(word)


    def show_possibilities(self):

        for i in self.mots:
            print(i)


print(''' 
    1: Manipulation et opérations sur les mots.
    2: Langage et grammaires.
    3: Analyseur syntaxique.
    ''')


while True:

    choice_partie = int(input("Entrer le numéro de la partie voulue: "))

    if choice_partie-1 in range(3):
        break

# Partie 1

if choice_partie == 1 :

    print(''' 
        * Miroir d'un mot.
        * Puissance d'un mot.
        ''')

    while True:

        choice_sous_partie = str(input("Miroir ou Puissance? (m/p): "))

        if choice_sous_partie.lower() == 'm' or choice_sous_partie.lower() == 'p':

            break


    # if the answer was M "Miroir"
    if choice_sous_partie.lower() == 'm':

        while True:

            mot_in = str(input("Entrer le mot: "))



            match = re.search('[^abc]',mot_in)

            if not match:
                break

        # Déclaration du premier objet " reverse_mot "

        reverse_mot = Word_miroir(mot_in)

        # Appeler la méthode "reverse_word"

        reverse_mot.reverse_word()

    # if the answer was P "Puissance"
    else:

        while True:

            mot_in = str(input("Entrer le mot: "))

            # Déclaration du premier objet " reverse_mot "

            match = re.search('[^abc]',mot_in)

            #Checking if the word contains only {a,b,c}
            if not match:

                while True:

                #Checking if N is greater than 0

                    n = int(input("Entrer la valeur de n: "))

                    if n > 0:
                        break
                break

        # Déclaration du deuxieme objet

        power_mot = Word_puissance(mot_in,n)

        power_mot.show_puissance()

if choice_partie == 2 :

    N = int(input("Entrer la valeur de n: "))

    generated = Generator(N)

    generated.possiblities(generated.P.get('S')[0])

    generated.show_possibilities()

if choice_partie == 3:

    pass

