#!/usr/bin/python3

# This is a Map of my house

def showInstructions():
  #print a main menu and the commands
  print('''
WELCOME TO MY HOUSE
========
Commands:
  go [direction]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('Current Location = ' + currentRoom)
  print("---------------------------")


#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Front Porch' : {
                  'north' : 'Front Entryway',
                  'east' : 'Porch: Facing Garage',
                  'south' : 'Front Porch',
                  'west' : 'Porch: Facing National Park',
                },

            'Front Entryway' : {
                  'north' : 'Hall',
                  'east' : 'Entryway: facing Office',
                  'south' : 'Front Porch',
                  'west' : 'Entryway: facing Livingroom'
                },

            'Hall' : {
                  'north' : 'Bar area',
                  'east' : 'Half Bathroom',
                  'south' : 'Front Entryway',
                  'West' : 'Pantry'
               },
            'Garage' : {
                  'north' : 'Dining Room',
                  'west' : 'Kitchen',
                  'item' : 'pile of dead babies',
                  'item' : 'red ferrari'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie'
              },
            'Basement' : {
                  'south' : 'Hall',
                  'item' : 'whip and chains.',
                  'east' : 'B1',
                  'west' : 'B1',
                  'north' : 'B1'
                   },
            'Upstairs Hall' : {
                  'south' : 'Playroom',
                  'north' : 'Bedroom',
                  'west' : 'Bathroom',
                  'east' : 'Hall',
                  'item' : 'whip and chains.'
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
                  'item' : 'BIG BLACK DILDO =======D---'
                  },
            'Closet' : {
                  'north' : 'Bathroom',
                  'item' : 'cucumber',
                  'item' : 'tube of vaseline'
                  },
            'Playroom' : {
                    'north' : 'Upstairs Hall',
                    'east' : 'Attic',
                    'item' : 'glitter',
                    'item' : 'bodyoil',
                    'item' : 'LIVE: hamster',
                    'item' : 'plastic tube'
                    },
            'Attic' : {
                    'west' : 'Upstairs Hall',
                    'item' : 'dead thai lady boy'
                    },
            'B1' : {
                    'west' : 'Basement',
                    'east' : 'B3',
                    'north' : 'B2',
                    'south' : 'B2'
                    },
            'B2' : {
                    'west' : 'B4',
                    'east' : 'B4',
                    'north' : 'B1',
                    'south' : 'B1'
                    },
            'B3' : {
                    'west' : 'B1',
                    'east' : 'B3',
                    'north' : 'B3',
                    'south' : 'B4'
                    },
            'B4' : {
                    'west' : 'B2',
                    'east' : 'B2',
                    'north' : 'B3',
                    'south' : 'B3'
            }
         }

#start the player in the Hall
currentRoom = 'Front Porch'

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

  if currentRoom == 'Front Porch' and input() == 'south':
    print('Leaving so soon?')

  if currentRoom == 'Front Porch':
    print('You are standing on the front porch facing The Schrantz Residence.') 
    print('The porch goes across the front of the house.')
    print('If you turn east you are facing the garage if you turn west you will be facing the Cuyahoga Valley National Park')

  if currentRoom == '':
      print('You are a dirty gender neutral pronoun')

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A figure with a rubber phyallic object strapped to its forhead has got you... GAME OVER!')
    break
