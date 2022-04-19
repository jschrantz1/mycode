pokedex= {"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

pokedex["Pikachu"] = "Electric"

a = pokedex
a = ",".join(a)
print(a)


b = "Sorry we dont have any record of that Pokemon!"

choice= input("Choose a starter Pokemon from the list:\n>")

print(pokedex.get(choice, b))

        # if the pokemon you chose was not in the available pokemon
if choice not in pokedex:
       print("Please make a different selection")
else:
    print("Great choice!", (pokedex.get(choice)), "is a favorite type of mine! Choose another Pokemon!")

#print(pokedex.get(choice, "Sorry we dont have any record of that Pokemon!"))
        
