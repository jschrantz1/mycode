#!/usr/bin/env python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Fannypack : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "item2" in rooms[currentRoom]:
    print('You also see a ' + rooms[currentRoom]['item2'])
  if "item3" in rooms[currentRoom]:
      print('and a ' + rooms[currentRoom]['item3'])
  if "item4" in rooms[currentRoom]:
      print('and a ' + rooms[currentRoom]['item4'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'covid-mask',
                  'north' : 'Basement',
                  'west' : 'Upstairs Hall',
                  'item2' : 'buschs baked beans'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east' : 'Garage',
                  'west' : 'Upstairs Hall',
                  'item' : 'Angry Red Headed Python Instructor'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Garage',
                  'item' : 'vaccine card',
                  'north' : 'Pantry'
               },
            'Garage' : {
                  'north' : 'Dining Room',
                  'west' : 'Kitchen',
                  'item' : 'pile of baby dolls',
                  'item2' : 'red ferrari'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie'
              },
            'Basement' : {
                  'south' : 'Hall',
                  'item' : 'GITHUB Code'
                   },
            'Upstairs Hall' : {
                  'south' : 'Office',
                  'north' : 'Bedroom',
                  'west' : 'Bathroom',
                  'east' : 'Hall',
                  'item' : 'jar of peanut butter'
                  },
            'Bedroom' : {
                  'east' : 'Attic',
                  'south' : 'Upstairs Hall',
                  'west' : 'Bathroom'
                  },
            'Bathroom' : {
                  'east' : 'Upstairs Hall',
                  'west' : 'Bedroom',
                  'south' : 'Closet',
                  'item' : 'dog collar'
                  },
            'Closet' : {
                  'north' : 'Bathroom',
                  'item' : 'cucumber',
                  },
            'Office' : {
                    'north' : 'Upstairs Hall',
                    'east' : 'Attic',
                    'item' : 'glitter',
                    'item2' : 'bodyoil',
                    'item3' : 'lemmewinks',
                    },
            'Attic' : {
                    'west' : 'Upstairs Hall',
                    'item' : 'creepy mannequin'
            }
         }

#start the player in the Hall
currentRoom = 'Attic'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get':
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')

#    elif "item2" in rooms[currentRoom] and move[2] in rooms[currentRoom]['item2']:
      inventory += [2]
      print(move[2] + 'got!')

      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
  else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == 'take':
     #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
         #add the item to their inventory
       inventory += [move[1]]
       #display a helpful message
       print(move[1] + ' got!')
       #delete the item from the room
    del rooms[currentRoom]['item']
     #otherwise, if the item isn't there to get
    #else:
       #tell them they can't get it
       #print('Can\'t take ' + move[1] + '!')

  ## Define how a player can win
  if currentRoom == 'Garage' and 'Covid-Mask' in inventory and 'Vaccine Papers' in inventory:
    print('You escaped the house with the appropriate PPE ... YOURE SAFE FROM ALL DANGER. YOU  WIN!')
    break

  if currentRoom == 'Basement' and 'Vaccine Papers' not in inventory:
      print('SHOW ME YOUR PAPERS')

  if currentRoom == 'Kitchen' and 'GITHUB Code' not in inventory:
      print('An Angry Red Headed Python Instructor has got you... GAME OVER!')
      break

  if currentRoom == 'Kitchen' and 'GITHUB Code' in inventory:
      print('\nAn Angry Red Headed Python Instructor approaches you and runs away after seeing your GITHUB Code')
 # ASK CHAD FOR HELP TO NOT BREAK GAME - MOVING BACK INTO ROOM AFTER FIRST ENTRANCE
  if currentRoom == 'Kitchen' and 'GITHIB Code' in inventory:
      del rooms[currentRoom]['item':'Angry Red Headed Python Instructor']

  #elif rooms[currentRoom]

  ## If a player enters a room with a monster
#        elif 'item' in rooms : 'Kitchen', and 'monster' in rooms[currentRoom]['GITHUB Code']:
#        print('A an angry Red Headed Python Instructor has got you... GAME OVER!')
