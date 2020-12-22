spirit_dict ={
    'rum':.40,
    'gin':.40,
    'genever': .40,
    'vodka': .40,
    'whiskey' : .40,
    'vermouth' : .18,
    'wine': .18,
    'champagne': .18,
    'brandy': .40,
    'cognac': .40,
    'cointreau' : .40,
    'grain': 1.95,
    'tequila': .40,
    'mezcal': .40,
    'liqueur': .25,
    'greenchartreuse': .55,
    'yellowchartreuse': .40,
    'non': 0
    }


def split_ingredients(s):
    text = s.strip('0123456789.')
    text = text.strip('oz ')
    number = s.strip('qwertyuiopasdfghjklzxcvbnm')
    number = number.strip(' oz')
    number = float(number) * 30        #Converts ounces to milliliters
    return text, number

total_proof = 0
total_volume = 0

print("To see the list of spirits, type 'H'")

#loop here
while True:
    ingredient = input('Enter the spirit and volume (Ex. 3 oz Rum): ')

    if ingredient == "Done" or ingredient == "":
            print("Proof is ", (total_proof/total_volume * 100))
            break
    elif ingredient.upper() == "H":
        for key in spirit_dict:
            print(key)
    else:
        si = split_ingredients(ingredient)
        
        text_spirit = si[0]
        volume = int(si[1])

        if text_spirit in spirit_dict:
            proof = (spirit_dict[text_spirit] * volume)
            total_proof += proof
            total_volume += volume

        else:
            total_volume += volume
        print("     Type 'Done' when finished")


