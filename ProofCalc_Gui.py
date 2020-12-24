from guizero import App, Text, Picture, PushButton, Combo, TextBox
from random import choice

app = App(title="Proof Calculator", width='350', height='600') #Titles the Window of the app

message =Text(app, text="How boozy is it?", font="Libre Baskerville", size="18") #The first field (app) tells the lcoation of the text to display

app.bg = "#cce6ff"      #BACKGROUND color. can take hex or RGD coordiantes

martini_pic = Picture(app, image="./Coupe256.png")

proof_sum = 0
total_proof = 0
total_volume = 0
display_drink = Text(app, text='',  font="Libre Baskerville")
recipe = Text(app, text='', font="Libre Baskerville", size = '10')

#   Dictionary with common spirits and their alcohol %
spirits = {" ":0, 'Amaretto':28, "Bourbon":40, "Brandy":40, "Campari":24, "Champagne":12, "Chartreuse, Green":55, "Chartreuse, Yellow":40,
               "Cider, n/a":0, "Cointreau":40, "Cognac":40, "Genever":43, "Gin":42, "Ginger Beer":0, "Grain":95, "Liqueuer, generic":20, "Luxardo":32, "Mezcal":40,
               "Juice":0,"Rum":40, "Scotch":45, "Schnapps":18, "Simple syrup":0, "Soda":0, "Tequila":40, "Tonic":0, "Vermouth":18, "Vokda":40,
               "Water":0, "Whiskey":45, "Wine":15
           }

ingredients = [" ", "Amaretto", "Bourbon", "Brandy", "Campari", "Champagne", "Chartreuse, Green", "Chartreuse, Yellow",
               "Cider, n/a", "Cointreau", "Cognac", "Genever", "Gin", "Ginger Beer", "Grain", "Liqueuer, generic", "Luxardo", "Mezcal",
               "Juice","Rum", "Scotch", "Schnapps", "Simple syrup", "Soda", "Tequila", "Tonic", "Vermouth", "Vokda",
               "Water", "Whiskey", "Wine"]


def refresh_drinks():
    display_drink.clear()
    
    proof_check()

    recipe.value += '\n %s oz of %s' %(volume.value,liquor_choice.value) 
    
    display_text = "With %s oz of %s, the drink\n is currently %s%% alcohol." %(volume.value,liquor_choice.value, str(total_proof)[:4])
    display_drink.value = display_text

    
    #print(volume.value, liquor_choice.value, total_proof, proof_sum)

def proof_check():
    global proof, total_volume, proof_sum, total_proof
    if liquor_choice.value in spirits:
        proof = int(spirits[liquor_choice.value])
        
        proof_sum += float(volume.value) * proof #(oz. * proof)
        
        total_volume += float(volume.value)
        #(oz * proof)+...(oz. + proof)/total_volume

        total_proof = float(proof_sum/total_volume)

        #print(proof, proof_sum, total_volume, total_proof)
        return proof_sum, total_volume, total_proof
        

def clear_all():
    global proof, total_volume, proof_sum, total_proof
    proof = 0
    total_volume *= 0
    proof_sum *= 0
    total_proof = 0

    recipe.value = " "
    display_drink.value = 0
    display_drink.value = "Glass emptied"



drink_values = Text(app)


volume = TextBox(app, "1.5", align="left", width='4')
ounces = Text(app, text='oz.', align='left')
liquor_choice = Combo(app, ingredients, align="left")

add_button = PushButton(app, refresh_drinks, text="Add", align="left")  #calls the refresh drinks function
clear_button = PushButton(app, clear_all, text="Clear", align="right")  #calls the clear function




app.display() #must have at the end




#Enter volume & spirit
#[_] oz COMBO
# 'Add' button 
