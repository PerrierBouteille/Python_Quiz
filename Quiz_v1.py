#################################################
#          ___     _   _   _   _____            #
#         /    \  | | | | | | |___  |           #
#         | [] |  | | | | | |    / /            #
#         \__  |  | |_| | | |   / /__           #
#            \_\  |_____| |_|  |_____|          #
#################################################
#                   By Perrier                  #
#                  Version: 1.0                 #
#################################################

import random
from tkinter import *
from time import *
import os
import csv

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
#Celle-ci s'affiche dans le cmd et la console de VisualStudio Code
#si vous utilisé un autres éditeur celle-ci peuvent ne pas fonctionner.

def quiz():
    print(colors.WARNING+ "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(colors.GREEN + "          ___     _   _   _   _____            ")
    print(colors.GREEN + "         /    \  | | | | | | |___  |           ")
    print(colors.GREEN + "         | [] |  | | | | | |    / /            ")
    print(colors.GREEN + "         \__  |  | |_| | | |   / /__           ")
    print(colors.GREEN + "            \_\  |_____| |_|  |_____|          ")
    print()
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
            print(colors.WARNING + "[Logs] Lecture des questions en cours.." + colors.END)
            sleep(1)
        print(colors.WARNING + "[Logs] Nombre de question: " + colors.END + "" + str(reader.line_num))
        sleep(1)
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
            print(colors.WARNING + "[Logs] Réponse donnée:" + colors.END + "" + answer.get())
            if answer.get().lower() == CorrectAnswer:
                print( colors.END + "Réponse:" + colors.GREEN + "Correct!" + colors.END)
                score=score+1
                questionsRight=questionsRight+1
                questionnb = questionnb+1
            else:
                print(colors.END + "Réponse: " +colors.RED + "Incorrect." + colors.END)
                print(colors.WARNING + "[Logs] Réponse correct: " + colors.END + "" + CorrectAnswer)
                questionnb = questionnb+1
            print()
            sleep(1)
            Quest.destroy()

        Quest = Tk()
        Quest.geometry("800x400")
        txt=Label(Quest,text="Question #" + str(questionnb)).pack()
        txtquest=Label(Quest,text=question).pack()
        answer=StringVar()
        rep=Entry(Quest, textvariable = answer).pack()
        button1 = Button(text='Subit', command=subit).pack()
        Quest.mainloop() #Fenetre de vos question avec l'insertion de votre réponse.

    totalScore = (score / reader.line_num) * 100
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(colors.RED + "                    FIN                        ")
    print("  Tu as ",score," questions correcte soit",totalScore,"%." + colors.END)
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    fen = Tk()
    fen.geometry("800x400")
    fen.title("Quiz")
    fen["bg"]= "grey"
    fen["relief"] = "raised"

    txt1=Label(fen,text="Votre score est de : " + str(score),bg='grey',font=("Orkney", 30))
    txt2=Label(fen,text='soit → ' + str(totalScore) + "% de réponse juste.",bg='grey',font=("Orkney", 30))
    txt1.pack()
    txt2.pack()

    fen.mainloop() #Fenetre de votre score total

quiz()

######################################################################################################
#                                                                                                    #
#   Ceci est un open source, vous avez le droit de modifier le programme si vous le souhaitez.       #
#   Si vous voulez utiliser le programme avec des questions personnels, rédiger un fichier csv       #
#   sous la forme:                                                                                   #
#   Question,Reponse                                                                                 #
#   Question,Reponse                                                                                 #
#                                                                                                    #
######################################################################################################

