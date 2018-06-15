import Node

def id3():
	data = [[]]
	f = open('Pokemon1.csv')
	for line in f:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	tree = {'objectType': {'pokemon': {'rarity': {'<7': {'type': {'other': {'catchable': {'y': {'ap': {'<30': {'dp': {'<30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': 'n'}}}}, '>30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}}}, '>30': {'dp': {'<30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}, '>30': 'y'}}}}, 'n': {'ap': {'<30': {'dp': {'<30': {'hpOfPokemon': {'<50': 'n', '>50': {'hpOfPlayer': {'<60': 'n', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}, '>30': 'n'}}, '>30': 'n'}}}}, 'normal': {'catchable': {'y': {'ap': {'<30': {'dp': {'<30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}, '>30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}}}, '>30': {'dp': {'<30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}, '>30': {'hpOfPokemon': {'<50': {'hpOfPlayer': {'<60': {'shiny': {'y': 'y', 'n': 'n'}}, '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}, '>50': {'hpOfPlayer': {'<60': 'y', '>60': {'shiny': {'y': 'y', 'n': 'n'}}}}}}}}}}, 'n': 'n'}}}}, '>7': {'type': {'other': {'catchable': {'y': 'y', 'n': 'n'}}, 'normal': {'catchable': {'y': 'y', 'n': 'n'}}}}}}, 'item': 'y'}}
	attributes = ['objectType', 'rarity', 'type', 'catchable', 'ap', 'dp', 'hpOfPokemon', 'hpOfPlayer', 'shiny', 'catch']
	count = 0
	for entry in data:
		count += 1
		tempDict = tree.copy()
		result = ""
		while(isinstance(tempDict, dict)):
			root = Node.Node(list(tempDict)[0], tempDict[list(tempDict)[0]])
			tempDict = tempDict[list(tempDict)[0]]
			index = attributes.index(root.value)
			value = entry[index]
			if(value in tempDict.keys()):
				child = Node.Node(value, tempDict[value])
				result = tempDict[value]
				tempDict = tempDict[value]
			else:
				print(str("Info from pokedex: %s" % data))
				return str(result)
				break
	print(str("Info from pokedex: %s" % data))
	print("entry%s = %s" % (count, result))
	return str(result)
