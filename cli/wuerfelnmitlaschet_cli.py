# Title: Würfeln mit Armin
# Author: William Lee Reed
# Last Modified: 2021-04-06, 22:19

import time
import random
from random import randint

print('Wir spielen jetzt eine Runde Würfeln mit Armin')
print('.')
var1 = randint(10, 16)
var2 = randint(10, 16)
var3 = randint(10, 16)
var4 = randint(10, 16)
var5 = randint(10, 16)
var6 = randint(10, 16)
var7 = randint(10, 16)
var8 = randint(10, 16)
var9 = randint(10, 16)

text1 = 'Fehler!'
text2 = 'Fehler!'
text3 = 'Fehler!'
text4 = 'Fehler!'
text5 = 'Fehler!'
text6 = 'Fehler!'
text7 = 'Fehler!'
text8 = 'Fehler!'
text9 = 'Fehler!'


print('Wie möchtest du das Spiel spielen?')
print('Möchtest du Selber würfeln und deine Zahlen eingeben? Dann gib eine 1 ein!')
print('Möchtest du lieber den Computer für dich Würfeln lassen? Dann gib eine 2 ein!')
spieltypinput = input(
    'Gib hier bitte deine gewünschte Spielweise ein (1/2) : ')
spieltyp = int(spieltypinput)
print('Dein Spieltyp ist:')
print(spieltyp)
print(' ')


if spieltyp == 1:
    var1 = int(input('Was war deine erste Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var2 = int(input('Was war deine zweite Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var3 = int(input('Was war deine dritte Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var4 = int(input('Was war deine vierte Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var5 = int(input('Was war deine fünfte Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var6 = int(input('Was war deine sechste Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var7 = int(input('Was war deine siebte Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var8 = int(input('Was war deine achte Zahl? (Nur zahlen von 1-6)'))
    # time.sleep(0.25)
    var9 = int(input('Was war deine neunte Zahl? (Nur zahlen von 1-6)'))
    spieltyp = "bereitfuersatz"
elif spieltyp == 2:
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
time.sleep(0.25)
while spieltyp == 'bereitfuersatz':
    print('So jetzt bereite dich auf der Ergebnis vor!')
    time.sleep(0.25)
    if var1 == 1:
        print('Deine erste Zahl war 1')
        text1 = 'ein'
    elif var1 == 2:
        print('Deine erste Zahl war 2')
        text1 = "zwei"
    elif var1 == 3:
        print('Deine erste Zahl war 3')
        text1 = "drei"
    elif var1 == "4" or 3:
        print('Deine erste Zahl war 4')
        text1 = "vier"
    elif var1 == 5:
        print('Deine erste Zahl war 5')
        text1 = "fünf"
    elif var1 == 6:
        print('Deine erste Zahl war 6')
        text1 = "sechs"
    if var2 == 1:
        print('Deine zweite Zahl war 1')
        text2 = 'tägige/n'
    elif var2 == 2:
        print('Deine zweite Zahl war 2')
        text2 = "wöchige/n"
    elif var2 == 3:
        print('Deine zweite Zahl war 3')
        text2 = "monatige/n"
    elif var2 == 4:
        print('Deine zweite Zahl war 4')
        text2 = "fachige/n"
    elif var2 == 5:
        print('Deine zweite Zahl war 5')
        text2 = "malige/n"
    elif var2 == 6:
        print('Deine zweite Zahl war 6')
        text2 = "hebige/n"
    if var3 == 1:
        print('Deine dritte Zahl war 1')
        text3 = 'harte/n'
    elif var3 == 2:
        print('Deine dritte Zahl war 2')
        text3 = "softe/n"
    elif var3 == 3:
        print('Deine dritte Zahl war 3')
        text3 = "optionale/n"
    elif var3 == 4:
        print('Deine dritte Zahl war 4')
        text3 = "intransparente/n"
    elif var3 == 5:
        print('Deine dritte Zahl war 5')
        text3 = "alternativelose/n"
    elif var3 == 6:
        print('Deine dritte Zahl war 6')
        text3 = "unumkehrbare/n"
    if var4 == 1:
        print('Deine vierte Zahl war 1')
        text4 = 'Wellenbrecher-'
    elif var4 == 2:
        print('Deine vierte Zahl war 2')
        text4 = "Brücken-"
    elif var4 == 3:
        print('Deine vierte Zahl war 3')
        text4 = "Treppen-"
    elif var4 == 4:
        print('Deine vierte Zahl war 4')
        text4 = "Wende-"
    elif var4 == 5:
        print('Deine vierte Zahl war 5')
        text4 = "Impf-"
    elif var4 == 6:
        print('Deine vierte Zahl war 6')
        text4 = "Ehren-"
    if var5 == 1:
        print('Deine fünfte Zahl war 1')
        text5 = 'Lockdown'
    elif var5 == 2:
        print('Deine fünfte Zahl war 2')
        text5 = "Stopp"
    elif var5 == 3:
        print('Deine fünfte Zahl war 3')
        text5 = "Maßnahme"
    elif var5 == 4:
        print('Deine fünfte Zahl war 4')
        text5 = "Kampagne"
    elif var5 == 5:
        print('Deine fünfte Zahl war 5')
        text5 = "Sprint"
    elif var5 == 6:
        print('Deine fünfte Zahl war 6')
        text5 = "Matrix"
    if var6 == 1:
        print('Deine sechste Zahl war 1')
        text6 = 'zum Sommer'
    elif var6 == 2:
        print('Deine sechste Zahl war 2')
        text6 = "auf Weiteres"
    elif var6 == 3:
        print('Deine sechste Zahl war 3')
        text6 = "zur Bundestagswahl"
    elif var6 == 4:
        print('Deine sechste Zahl war 4')
        text6 = "2030"
    elif var6 == 5:
        print('Deine sechste Zahl war 5')
        text6 = "nach den Abiturprüfungen"
    elif var6 == 6:
        print('Deine sechste Zahl war 6')
        text6 = "in die Puppen"
    if var7 == 1:
        print('Deine siebte Zahl war 1')
        text7 = 'sofortigen'
    elif var7 == 2:
        print('Deine siebte Zahl war 2')
        text7 = "nachhaltigen"
    elif var7 == 3:
        print('Deine siebte Zahl war 3')
        text7 = "allmählichen"
    elif var7 == 4:
        print('Deine siebte Zahl war 4')
        text7 = "unausweichlichen"
    elif var7 == 5:
        print('Deine siebte Zahl war 5')
        text7 = "wirtschaftsschonenden"
    elif var7 == 6:
        print('Deine siebte Zahl war 6')
        text7 = "willkürlichen"
    if var8 == 1:
        print('Deine achte Zahl war 1')
        text8 = 'Senkung'
    elif var8 == 2:
        print('Deine achte Zahl war 2')
        text8 = "Steigerung"
    elif var8 == 3:
        print('Deine achte Zahl war 3')
        text8 = "Beendigung"
    elif var8 == 4:
        print('Deine achte Zahl war 4')
        text8 = "Halbierung"
    elif var8 == 5:
        print('Deine achte Zahl war 5')
        text8 = "Vernichtung"
    elif var8 == 6:
        print('Deine achte Zahl war 6')
        text8 = "Beschönigung"
    if var9 == 1:
        print('Deine neunte Zahl war 1')
        text9 = 'Infektionszahlen'
    elif var9 == 2:
        print('Deine neunte Zahl war 2')
        text9 = "privaten Treffen"
    elif var9 == 3:
        print('Deine neunte Zahl war 3')
        text9 = "Wirtschaftsleistung"
    elif var9 == 4:
        print('Deine neunte Zahl war 4')
        text9 = "Wahlprognosen"
    elif var9 == 5:
        print('Deine neunte Zahl war 5')
        text9 = "dritten Welle"
    elif var9 == 6:
        print('Deine neunte Zahl war 6')
        text9 = "Bundeskanzlerin"
    time.sleep(0.75)
    print('Was wir jetzt brauchen ist eine/n ' + text1 + text2 + ' ' + text3 + ' ' + text4 +
          text5 + ' bis ' + text6 + ', zur ' + text7 + ' ' + text8 + ' der ' + text9 + '.')
    spieltyp = 'ende'

print(' ')
print('Und, wie findest du den Satz?')
# break

# while spieltyp != 'bereitfuersatz' or 'z' or 'Z' or 'w' or 'W' or 'ende':
#     print('Es ist ein Fehler aufgetreten: ')
#     print(' ')
#     print('Fehlercode: Variable \"spieltyp\" not equal \"bereitfuersatz\" or \"z\" or \"Z\" or \"w\" or \"W\"')
#     print('spieltyp = ' + spieltyp)


# print('*********************')
# print('*********************')
# print('*********************')
# print('.')
# print('DEBUG!!!')
# print('.')
# print('*********************')
# print('.')
# print('Variable 1= ' + var3)
# print('Variable 2= ' + var2)
# print('Variable 3= ' + var3)
# print('Variable 4= ' + var4)
# print('Variable 5= ' + var5)
# print('Variable 6= ' + var6)
# print('Variable 7= ' + var7)
# print('Variable 8= ' + var8)
# print('Variable 9= ' + var9)
# print('.')
# print('*********************')
# print('.')
# print('Text 1= ' + text1)
# print('Text 2= ' + text2)
# print('Text 3= ' + text3)
# print('Text 4= ' + text4)
# print('Text 5= ' + text5)
# print('Text 6= ' + text6)
# print('Text 7= ' + text7)
# print('Text 8= ' + text8)
# print('Text 9= ' + text9)
# print('.')
# print('*********************')
# print('.')
# print('DEBUG ENDE!!!')
# print('.')
# print('*********************')
# print('*********************')
# print('*********************')
