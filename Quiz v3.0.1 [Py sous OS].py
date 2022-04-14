#################################################
#          ___     _   _   _   _____            #
#         /    \  | | | | | | |___  |           #
#         | [] |  | | | | | |    / /            #
#         \__  |  | |_| | | |   / /__           #
#            \_\  |_____| |_|  |_____|          #
#################################################
#                   By Perrier                  #
#                  Version 3.0.1                #
#################################################

import random
from tkinter import *
from time import *
import os
import csv
import unicodedata


clear = lambda: os.system('cls')

class colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#Couleur pour les logs consol

def quiz():

    print(colors.WARNING+ "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(colors.GREEN + "          ___     _   _   _   _____            ")
    print(colors.GREEN + "         /    \  | | | | | | |___  |           ")
    print(colors.GREEN + "         | [] |  | | | | | |    / /            ")
    print(colors.GREEN + "         \__  |  | |_| | | |   / /__           ")
    print(colors.GREEN + "            \_\  |_____| |_|  |_____|          ")
    print()
    print(colors.GREEN + "                 Version: 3.0.1                 ")
    print(colors.WARNING+ "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    sleep(1.5)
    print(colors.END)
    clear()
    global score
    score=0
    global questionsRight
    questionsRight=0
    print(colors.UNDERLINE)
    fileName = input("Entré le nom du fichier: ") #Sélection du fichier csv (Tout fichier non csv engagera une erreur dans le programme)
    print(colors.END)
    clear()
    print(colors.RED +"/!\ Merci de ne pas toucher à la console, en cas de problème veuillez contacter un administrateur. /!\ " + colors.END)
    quizFile = open(fileName,"r")
    quizData = quizFile.readlines()
    with open(fileName, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(colors.WARNING + "[DEBUG] Lecture des questions en cours.." + colors.END)
            sl = (random.randint(5, 20))/10
            sleep(sl)
        print(colors.WARNING + "[Logs] Nombre de question: " + colors.END + "" + str(reader.line_num))
        sleep(1.5)
        print("")
    random.shuffle(quizData)
    global questionnb
    questionnb=1
    for i in range(reader.line_num):

        x = quizData[i].strip()
        data = x.split(",")
        question = data[0]
        CorrectAnswer = data[1]

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(colors.BLUE + "Question #",questionnb, "" + colors.END)
        print()
        print(colors.CYAN + "" + question + "" + colors.END)
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        def subit():
            global questionnb
            global questionsRight
            global score
            print(colors.WARNING + "[Logs] Réponse : " + colors.END + "" + answer.get()) #Réponse normal
            finalans = unicodedata.normalize('NFKD', answer.get()).encode('ascii', 'ignore') #Écriture de la réponse en code ASCII (sans les accents)
            print(colors.WARNING + "[DEBUG] Réponse ASCII :" + colors.END + "" + str(finalans))
            print(colors.WARNING + "[DEBUG] Réponse LOWER :" + colors.END + "" + str(finalans.lower())) #Écriture de la réponse en minuscule

            name = str(finalans.lower())
            soundex = ""

            soundex += name[0]
            dictionary = {"bfpv": "1", "cgjkqsxz":"2", "dt":"3", "l":"4", "mn":"5", "r":"6", "aeiouhwy":"."}
            for char in name[1:]:
                for key in dictionary.keys():
                    if char in key:
                        code = dictionary[key]
                        if code != soundex[-1]:
                            soundex += code

            soundex = soundex.replace(".", "")
            soundex = soundex[:4].ljust(4, "0")
            print("[DEBUG] Soundex: " + soundex)

            repcsv = str(CorrectAnswer)
            soundexrep = ""

            soundexrep += repcsv[0]
            dictionary = {"bfpv": "1", "cgjkqsxz":"2", "dt":"3", "l":"4", "mn":"5", "r":"6", "aeiouhwy":"."}
            for char in repcsv[1:]:
                for key in dictionary.keys():
                    if char in key:
                        code = dictionary[key]
                        if code != soundexrep[-1]:
                            soundexrep += code

            soundexrep = soundexrep.replace(".", "")
            soundexrep = soundexrep[:4].ljust(4, "0")
            print("[DEBUG] Soundex Réponse: " + soundexrep)

            if str(soundex) == str(soundexrep):
                print( colors.WARNING + "[Logs] " + colors.END + "Réponse:" + colors.GREEN + "Correct!" + colors.END)
                score=score+1
                questionsRight=questionsRight+1
                questionnb = questionnb+1
            else:
                print(colors.WARNING + "[Logs]" + colors.END + "Réponse: " +colors.RED + "Incorrect." + colors.END)
                print(colors.WARNING + "[Logs] Réponse correct: " + colors.END + "" + CorrectAnswer)
                questionnb = questionnb+1
            print()
            sleep(1)
            Quest.destroy()

        Quest = Tk()
        Quest.geometry("800x400")
        Quest.title(string=' ')
        frame = LabelFrame(
            Quest,
            text='Question n°' + str(questionnb),
            bg='#f0f0f0',
            font=(10)
        )
        frame.pack(expand=True, fill=BOTH)
        Label(
            frame,
            text=question
        ).pack()

        answer=StringVar()

        Entry(
            frame,
            textvariable = answer
        ).pack()
        Button(
            frame,
            text='Validé vôtre réponse',
            command=subit
        ).pack()
        #-------------[Ancien script]------------
        #txt=Label(Quest,text="Question #" + str(questionnb)).pack()
        #txtquest=Label(Quest,text=question).pack()
        #answer=StringVar()
        #rep=Entry(Quest, textvariable = answer).pack()
        #button1 = Button(text='Subit', command=subit).pack()
        #----------------------------------------

        Quest.mainloop() #Fenetre de vos question avec l'insertion de votre réponse.

    totalScore = (score / reader.line_num) * 100
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(colors.RED + "                    FIN                        ")
    print("  Tu as ",score," questions correcte soit",totalScore,"%." + colors.END)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    fen = Tk()
    fen.geometry("800x400")
    fen.title(string=' ')
    fen["bg"]= "white"
    fen["relief"] = "raised"

    frame = LabelFrame(
    fen,
    text='Quiz v3.0.1 | Fin',
    bg='#f0f0f0',
    font=(10)
    )
    frame.pack(expand=True, fill=BOTH)

    Label(
    frame,
    text="Votre score final est de : " + str(score),
    bg='#f0f0f0',
    font=("Comic Sans MS", 30)
    ).pack()

    Label(
        frame,
        text='soit → ' + str(totalScore) + "% de réponse juste.",
        bg='#f0f0f0',
        font=("Comic Sans MS", 30)
        ).pack()
    #-------------[Ancien script]------------
    #spc=Label(fen,text="Quiz v1.0.7 \n ",bg='white',font=("Arial", 16)).pack()
    #txt1=Label(fen,text="Votre score est de : " + str(score),bg='white',font=("Comic Sans MS", 30)).pack()
    #txt2=Label(fen,text='soit → ' + str(totalScore) + "% de réponse juste.",bg='white',font=("Comic Sans MS", 30)).pack()
    #----------------------------------------

    if score == 0:
        Label(frame,text="Retente ta chance car là..  :'(",bg='#f0f0f0',font=("Comic Sans MS", 30)).pack()
    if score < (reader.line_num/2):
        if score != 0:
            Label(frame,text="Tu peux faire mieux.. :/",bg='#f0f0f0',font=("Comic Sans MS", 30)).pack()
    if score < reader.line_num:
        if score > (reader.line_num/2):
            Label(frame,text="Pas mal :)",bg='#f0f0f0',font=("Comic Sans MS", 30)).pack()
    if score == reader.line_num:
        Label(frame,text="Perfect ! :D",bg='#f0f0f0',font=("Comic Sans MS", 30)).pack()

    fen.mainloop() #Fenetre de votre score total

quiz()

######################################################################################################
#                                                                                                    #
#   Ceci est un open source, vous avez le droit de modifier le programme si vous le souhaitez.       #
#   Si vous voulez utiliser le programme avec des questions personnels, rédiger un fichier csv       #
#   sous la forme:                                                                                   #
#   Question,b'reponse'                                                                              #
#   Question,b'reponse'                                                                              #
#                                                                                                    #
#   Si le format n'est pas respecté le script ne marchera pas.                                       #
# /!\ Les réponses doivent être écrite en minuscule sans accents entre '' et avec un b devant les '' #
#                                                                                                    #
######################################################################################################

