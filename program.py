import Node

def id3():
    data = [[]]
    f = open('Pokemon1.csv')
    for line in f:
	    line = line.strip("\r\n")
	    data.append(line.split(','))
    data.remove([])
    tree = {'objectType': {'pokemon': {'rarity': {'4': {'type': {'fire': {'catchable': {'y': {'ap': {'40': 'y', '10': 'n', '15': {'dp': {'15': {'hpOfPokemon': {'100': 'n', '90': 'y'}}}}}}}}, 'water': {'catchable': {'y': {'ap': {'30': 'y', '10': {'dp': {'20': {'hpOfPokemon': {'80': 'n', '90': 'y'}}}}}}}}, 'grass': {'catchable': {'y': {'ap': {'35': 'y', '15': {'dp': {'15': {'hpOfPokemon': {'90': {'hpOfPlayer': {'40': 'y', '80': 'n'}}, '40': 'y'}}}}}}}}, 'normal': {'catchable': {'y': {'ap': {'30': {'dp': {'30': {'hpOfPokemon': {'90': {'hpOfPlayer': {'20': 'y', '90': 'n'}}}}}}}}}}}}, '6': {'type': {'normal': {'catchable': {'y': {'ap': {'50': {'dp': {'50': {'hpOfPokemon': {'90': 'n', '80': {'hpOfPlayer': {'40': 'y', '70': 'n'}}, '100': {'hpOfPlayer': {'100': {'shiny': {'y': 'y', 'n': 'n'}}}}}}}}}}}}}}, '8': {'type': {'fire': {'catchable': {'n': 'n', 'y': 'y'}}, 'grass': {'catchable': {'n': {'ap': {'50': {'dp': {'50': {'hpOfPokemon': {'90': 'n', '80': 'n', '40': 'n', '70': 'y'}}}}}}, 'y': 'y'}}, 'water': {'catchable': {'n': {'ap': {'50': {'dp': {'50': {'hpOfPokemon': {'80': {'hpOfPlayer': {'100': 'n', '10': 'y', '30': 'n'}}, '90': 'n', '40': 'n'}}}}}}, 'y': 'y'}}}}, '1': {'type': {'grass': {'catchable': {'y': {'ap': {'20': {'dp': {'20': {'hpOfPokemon': {'80': {'hpOfPlayer': {'90': 'n', '20': 'y'}}, '90': 'y'}}}}}}}}}}, '2': {'type': {'fire': {'catchable': {'y': {'ap': {'25': {'dp': {'25': {'hpOfPokemon': {'100': 'y', '50': 'y', '80': 'n'}}, '10': {'hpOfPokemon': {'100': {'hpOfPlayer': {'30': 'y', '100': 'n'}}, '20': 'n'}}}}}}}}, 'water': {'catchable': {'y': {'ap': {'30': 'y', '20': {'dp': {'20': {'hpOfPokemon': {'40': 'n', '100': 'n', '80': {'hpOfPlayer': {'20': 'y', '90': 'n'}}, '90': 'n'}}}}}}}}, 'normal': {'catchable': {'y': {'ap': {'30': {'dp': {'30': {'hpOfPokemon': {'90': 'y', '30': 'n', '10': 'y'}}}}}}}}, 'grass': 'y'}}, '5': {'type': {'fire': 'y', 'grass': {'catchable': {'y': {'ap': {'15': {'dp': {'10': {'hpOfPokemon': {'90': 'n', '100': 'n', '10': 'n', '80': 'y'}}}}}}}}}}, '3': 'n'}}, 'item': 'y'}}
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
			    print( str("Info from pokedex: %s" % data))
			    return str(result)
			    break
    print(str("Info from pokedex: %s" % data))
    print("entry%s = %s" % (count, result))
    return str(result)