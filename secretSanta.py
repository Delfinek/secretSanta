# -*- coding: cp1252 -*-
import random
file = open('secretSantaListTest.txt', 'r')
SantasList = []
ChildrenList = []
NameGiftDictionary = {}

for line in file:
	(name, gift) = line.split(";")
	NameGiftDictionary[name] = gift
	SantasList.append(name)
	ChildrenList.append(name)

def WhoGiftsWho(RandomSantasList, ChildrenList):
	while (RandomSantasList[len(RandomSantasList)-1] == ChildrenList[len(ChildrenList)-1]):
		random.shuffle(ChildrenList)
	while(len(ChildrenList)):
		who = RandomSantasList.pop(0)
		filename = who.split(',')[0] + ".txt"
		out_file = open(filename, 'w+')
		if (who == ChildrenList[0]):
			out_file.write(SantaTextFile(ChildrenList.pop(1)))
		else:
			out_file.write(SantaTextFile(ChildrenList.pop(0)))
	return


def SantaTextFile(KidName):
	return ("Jesteś tajemniczym Świętym Mikołajem dla tej osoby: " 
				+ KidName 
				+ ". Wybierając prezent możesz inspirować się tym listem do Świętego Mikołaja: " 
				+ NameGiftDictionary[KidName])


# def validate(ShuffledNameList, NameGiftDictionary):
#	for i = len(ShuffledNameList)

WhoGiftsWho(SantasList, ChildrenList)
