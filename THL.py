import sys

from PyQt5.QtWidgets import *


from PyQt5 import QtWidgets


from PyQt5.uic import loadUi


from PyQt5.QtGui import QPixmap

import re


#################################  ALGORITHMS #############################################



################################# Generer  #################################################


class Generator:


    def __init__(self,n:int ):


        if n < 0:

           print("N est inferieur a 0 !!")

           pass

        else:
            
            if n < 3:

                print(f"Cette grammaire ne genere pas des mots d'une longeur de {n} !!")

                pass

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
            if len(i) == self.longeur:
                print(i)

        print("----------------------------------------------------------------------------------------------------------------")



#####################################  Analyser   #############################################


class Verify:


    def __init__(self,word:str):


        self.word = word


    def verifier(self,word_table:list):


        if len(word_table) == 1:


            if word_table[0] == 'a':


                return True


            else:


                return False


        elif len(word_table) == 3:


            if (word_table == ['a', 'a', 'b'] or word_table == ['a','a','a']):


                return True


            else:


                return False



        else:


            if (word_table[-1] == 'b' and word_table[0:2] == ['a','a']):


                return self.verifier(word_table[2:-1])


            elif (word_table[-1] == 'a'):


                return self.verifier(word_table[:-1])


            else:


                return False


#########################################  Miroir   #################################################

class Word_miroir:

    def __init__(self,word: str):
        self.word = word

    def reverse_word(self):
        print(f"Le mot miroir du {self.word} est: {self.word[::-1]}")

##########################################  Puissance  ####################################################


class Word_puissance:

    def __init__(self,word:str,n:int):
        self.word = word
        self.n = n

    def puissance(self):
        return self.word * self.n

    def show_puissance(self):
        print(f"La puissance {self.n} du mot {self.word} est: {self.puissance()}")


############################################################################################################


class Main_frame(QMainWindow):


    def __init__(self):



        super(Main_frame,self).__init__()


        loadUi("test_frame.ui",self)
        

        qpixmap = QPixmap('TP THL\Frame 1.jpg')


        self.label.setPixmap(qpixmap)


        self.mir_puis_button.clicked.connect(self.goto_m_p)


        self.analyse_button.clicked.connect(self.goto_anal)


        self.generate_button.clicked.connect(self.goto_gen)
        
        


    def goto_m_p(self):


        m_p_window = M_P_frame()


        widget.addWidget(m_p_window)


        widget.setCurrentIndex(widget.currentIndex()+1) 
    
   

    def goto_anal(self):


        anal_window = Anal_frame()


        widget.addWidget(anal_window)


        widget.setCurrentIndex(widget.currentIndex()+1) 
    

    def goto_gen(self):


        gen_window = Gen_frame()


        widget.addWidget(gen_window)


        widget.setCurrentIndex(widget.currentIndex()+1) 



class M_P_frame(QMainWindow):


    def __init__(self):



        super(M_P_frame,self).__init__()


        loadUi("secondFrame_firstQ.ui",self)


        qpixmap = QPixmap('TP THL\Frame_mir_puiss.jpg')


        self.label.setPixmap(qpixmap)


        self.mir_button_2.clicked.connect(self.go_back)


        self.mir_button.clicked.connect(self.goto_mir)


        self.puis_button.clicked.connect(self.goto_puis)


    def go_back(self):


        widget.setCurrentIndex(widget.currentIndex()-1) 


        widget.removeWidget(self)


    def goto_mir(self):


        m_window = Mir_frame()

        widget.addWidget(m_window)


        widget.setCurrentIndex(widget.currentIndex()+1) 



    def goto_puis(self):


        p_window = Puis_frame()

        widget.addWidget(p_window)


        widget.setCurrentIndex(widget.currentIndex()+1) 
       


class Anal_frame(QMainWindow):


    def __init__(self):



        super(Anal_frame,self).__init__()


        loadUi("Anal_Frame.ui",self)


        qpixmap = QPixmap('TP THL\Frame_Analyser.jpg')


        self.label.setPixmap(qpixmap)


        self.return_anal.clicked.connect(self.go_back)


        self.verify_anal.clicked.connect(self.go_analyse)


    def go_back(self):


        widget.setCurrentIndex(widget.currentIndex()-1) 


        widget.removeWidget(self)


    def go_analyse(self):
        

        Mot = str(self.analyse_in.text())


        Verify_word = Verify(Mot)


        Mot_table = list(Verify_word.word)


        print(f"Le mot '{Verify_word.word}' appartient au langage L(G)?' -----------> {Verify_word.verifier(Mot_table)}")


        print('----------------------------------------------------------------------------------------------------------------')
        


class Gen_frame(QMainWindow):


    def __init__(self):



        super(Gen_frame,self).__init__()


        loadUi("Framegenerate.ui",self)


        qpixmap = QPixmap('TP THL\Frame_Generer.jpg')


        self.label.setPixmap(qpixmap)


        self.return_generate.clicked.connect(self.go_back)


        self.generate_button.clicked.connect(self.clickedGen)

        #########################################################################################################################################################################

    def clickedGen(self):



        input_num = int(self.N_generate.text())


        generated = Generator(input_num)


        generated.possiblities(generated.P.get('S')[0])


        generated.show_possibilities()




        #########################################################################################################################################################################


    def go_back(self):


        widget.setCurrentIndex(widget.currentIndex()-1) 


        widget.removeWidget(self)



class Mir_frame(QMainWindow):


    def __init__(self):



        super(Mir_frame,self).__init__()


        loadUi("MiroirFrame.ui",self)


        pixmap = QPixmap('TP THL\Frame_mir.jpg')
        

        self.label.setPixmap(pixmap)
        

        self.return_mir.clicked.connect(self.go_back)

        self.mir_button.clicked.connect(self.go_miroir)


    def go_back(self):


        widget.setCurrentIndex(widget.currentIndex()-1) 


        widget.removeWidget(self)

    def go_miroir(self):

        mot_in = str(self.motMiroir.text())

        match = re.search('[^abc]',mot_in)

        if match:
            
            return print("Erreur !! votre mot n'appartient pas a T*")

        # Déclaration du premier objet " reverse_mot "

        reverse_mot = Word_miroir(mot_in)

        # Appeler la méthode "reverse_word"

        reverse_mot.reverse_word()

        print('----------------------------------------------------------------------------------------------------------------')


class Puis_frame(QMainWindow):


    def __init__(self):



        super(Puis_frame,self).__init__()


        loadUi("PuissanceFrame.ui",self)


        qpixmap = QPixmap('TP THL\Frame_puiss.jpg')


        self.label.setPixmap(qpixmap)


        self.return_puiss.clicked.connect(self.go_back)

        self.puiss_button.clicked.connect(self.go_puis)


    def go_back(self):


        widget.setCurrentIndex(widget.currentIndex()-1)  


        widget.removeWidget(self)



    def go_puis(self):

        mot_in = str(self.motMiroir.text())

           

        match = re.search('[^abc]',mot_in)

            #Checking if the word contains only {a,b,c}
        if match:

            return print("Erreur !! votre mot n'appartient pas a T*")

                #Checking if N is greater than 0
        else:

            n = int(self.N_puis.text())

            if n < 0:
                
                return print("Erreur !! votre N est inférieur a 0")

        # Déclaration du deuxieme objet

        power_mot = Word_puissance(mot_in,n)

        power_mot.show_puissance()

        print('----------------------------------------------------------------------------------------------------------------')


app = QApplication(sys.argv)


#Create a stack of windows

widget = QtWidgets.QStackedWidget()


#Create instances of classes

mainwindow = Main_frame()


#Add instances to Stack

widget.addWidget(mainwindow)



#Set height and width of widget

widget.setFixedHeight(590)

widget.setFixedWidth(980)


#show widget

widget.show()

#execute

app.exec_()


