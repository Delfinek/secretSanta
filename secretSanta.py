import random
file = open('secretSantaList.txt', 'r')
nameList = []
randomizedNames = []

for line in file:
	line = line.strip()
	nameList.append(line)
	randomizedNames.append(line)


def WhoGiftsWho(list1, list2):
	while (list1[len(list1)-1] == list2[len(list2)-1]):
		random.shuffle(list2)
	while(len(list2)):
		who = list1.pop(0)
		filename = who + ".txt"
		out_file = open(filename, 'w+')
		if (who == list2[0]):
			out_file.write("Jesteś tajemniczym Świętym Mikołajem dla tej osoby:\n" + list2.pop(1))
		else:
			out_file.write("Jesteś tajemniczym Świętym Mikołajem dla tej osoby:\n" + list2.pop(0))
	return

WhoGiftsWho(nameList, randomizedNames)
