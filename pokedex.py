pokedex= {"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

choice= input("Name a Generation 1 starter Pokemon:\n>")
#print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )
print(pokedex.get(choice, "Sorry we dont have any record of that Pokemon!"))
