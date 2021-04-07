# Würfeln mit Armin - GUI Edition
# Author: William Lee Reed
# Last Modified:

import easygui
import time
import random
from random import randint

# Define Game function


def MainGame():
    spieltypinput = easygui.buttonbox(
        'Es gibt mehrere Wege, dieses Spiel zu spielen. \n Möchtest du selber Würfeln und die Zahlen eingeben, dann Wähle die 1. \n Möchtest du lieber den Computer für dich Würfeln lassen? Dann wähle die 2.', choices=['1', '2'])
    spieltyp = int(spieltypinput)
    spieltypoutput = str(spieltyp)
    easygui.msgbox('Dein Spieltyp ist ' + spieltypoutput)

    while spieltyp == 1:
        var1 = int(easygui.buttonbox('Was war deine erste Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var2 = int(easygui.buttonbox(
            'Was war deine zweite Zahl?',
            choices=['1', '2', '3', '4', '5', '6']))
        var3 = int(easygui.buttonbox('Was war deine dritte Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var4 = int(easygui.buttonbox('Was war deine vierte Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var5 = int(easygui.buttonbox('Was war deine fünfte Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var6 = int(easygui.buttonbox('Was war deine sechste Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var7 = int(easygui.buttonbox('Was war deine siebte Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var8 = int(easygui.buttonbox('Was war deine achte Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        var9 = int(easygui.buttonbox('Was war deine neunte Zahl?',
                                     choices=['1', '2', '3', '4', '5', '6']))
        spieltyp = "bereitfuersatz"

    while spieltyp == 2:
        var1 = random.randint(1, 6)
        var2 = random.randint(1, 6)
        var3 = random.randint(1, 6)
        var4 = random.randint(1, 6)
        var5 = random.randint(1, 6)
        var6 = random.randint(1, 6)
        var7 = random.randint(1, 6)
        var8 = random.randint(1, 6)
        var9 = random.randint(1, 6)
        spieltyp = "bereitfuersatz"

    while spieltyp == 'bereitfuersatz':
        easygui.msgbox('Bereite dich auf dein Ergebnis vor!')
        time.sleep(0.25)
        if var1 == 1:
            text1 = 'ein'
        elif var1 == 2:
            text1 = "zwei"
        elif var1 == 3:
            text1 = "drei"
        elif var1 == "4" or 3:
            text1 = "vier"
        elif var1 == 5:
            text1 = "fünf"
        elif var1 == 6:
            text1 = "sechs"
        if var2 == 1:
            text2 = 'tägige/n'
        elif var2 == 2:
            text2 = "wöchige/n"
        elif var2 == 3:
            text2 = "monatige/n"
        elif var2 == 4:
            text2 = "fachige/n"
        elif var2 == 5:
            text2 = "malige/n"
        elif var2 == 6:
            text2 = "hebige/n"
        if var3 == 1:
            text3 = 'harte/n'
        elif var3 == 2:
            text3 = "softe/n"
        elif var3 == 3:
            text3 = "optionale/n"
        elif var3 == 4:
            text3 = "intransparente/n"
        elif var3 == 5:
            text3 = "alternativelose/n"
        elif var3 == 6:
            text3 = "unumkehrbare/n"
        if var4 == 1:
            text4 = 'Wellenbrecher-'
        elif var4 == 2:
            text4 = "Brücken-"
        elif var4 == 3:
            text4 = "Treppen-"
        elif var4 == 4:
            text4 = "Wende-"
        elif var4 == 5:
            text4 = "Impf-"
        elif var4 == 6:
            text4 = "Ehren-"
        if var5 == 1:
            text5 = 'Lockdown'
        elif var5 == 2:
            text5 = "Stopp"
        elif var5 == 3:
            text5 = "Maßnahme"
        elif var5 == 4:
            text5 = "Kampagne"
        elif var5 == 5:
            text5 = "Sprint"
        elif var5 == 6:
            text5 = "Matrix"
        if var6 == 1:
            text6 = 'zum Sommer'
        elif var6 == 2:
            text6 = "auf Weiteres"
        elif var6 == 3:
            text6 = "zur Bundestagswahl"
        elif var6 == 4:
            text6 = "2030"
        elif var6 == 5:
            text6 = "nach den Abiturprüfungen"
        elif var6 == 6:
            text6 = "in die Puppen"
        if var7 == 1:
            text7 = 'sofortigen'
        elif var7 == 2:
            text7 = "nachhaltigen"
        elif var7 == 3:
            text7 = "allmählichen"
        elif var7 == 4:
            text7 = "unausweichlichen"
        elif var7 == 5:
            text7 = "wirtschaftsschonenden"
        elif var7 == 6:
            text7 = "willkürlichen"
        if var8 == 1:
            text8 = 'Senkung'
        elif var8 == 2:
            text8 = "Steigerung"
        elif var8 == 3:
            text8 = "Beendigung"
        elif var8 == 4:
            text8 = "Halbierung"
        elif var8 == 5:
            text8 = "Vernichtung"
        elif var8 == 6:
            text8 = "Beschönigung"
        if var9 == 1:
            text9 = 'Infektionszahlen'
        elif var9 == 2:
            text9 = "privaten Treffen"
        elif var9 == 3:
            text9 = "Wirtschaftsleistung"
        elif var9 == 4:
            text9 = "Wahlprognosen"
        elif var9 == 5:
            text9 = "dritten Welle"
        elif var9 == 6:
            text9 = "Bundeskanzlerin"
        easygui.msgbox('Deine erste Zahl war ' + str(var1) + '\nDeine zweite Zahl war ' +
                       str(var2) + '\nDeine dritte Zahl war ' + str(var3) + '\nDeine vierte Zahl war ' + str(var4) + '\nDeine fünfte Zahl war ' + str(var5) + '\nDeine sechste Zahl war ' + str(var6) + '\nDeine siebente Zahl war ' + str(var7) + '\nDeine achte Zahl war ' + str(var8) + '\nDeine neunte Zahl war ' + str(var9))
        time.sleep(0.5)
        easygui.msgbox('Was wir jetzt brauchen ist eine/n ' + text1 + text2 + ' ' + text3 + ' ' + text4 +
                       text5 + ' bis ' + text6 + ', zur ' + text7 + ' ' + text8 + ' der ' + text9 + '.')
        spieltyp = 'ende'

    while spieltyp == 'ende':
        easygui.msgbox(
            """Das wars auch schon! Du kannst gerne nochmal spielen!""")
        nochmal = easygui.buttonbox(
            'Willst du nochmal spielen?', choices=['Ja', 'Nein'])
        if nochmal == 'Ja':
            MainGame()
        elif nochmal == 'Nein':
            easygui.msgbox('Bis bald!') #built in directly because, why not?
            break

# End defining Game function


# Define GameEnd function


#def GameEnd():
#    easygui.msgbox('Bis bald!')

# End defining GameEnd function


easygui.msgbox("Wir spielen jetzt eine Runde \"Würfeln mit Armin\"!")

var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
var6 = 0
var7 = 0
var8 = 0
var9 = 0

text1 = 'Fehler!'
text2 = 'Fehler!'
text3 = 'Fehler!'
text4 = 'Fehler!'
text5 = 'Fehler!'
text6 = 'Fehler!'
text7 = 'Fehler!'
text8 = 'Fehler!'
text9 = 'Fehler!'

MainGame()
