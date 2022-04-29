#!/usr/bin/python3

import os

# This is a Map of my house
os.system('clear')

def showInstructions():
  #print a main menu and the commands
    print('''
WELCOME TO MY HOUSE
========
Commands:
  go [direction]
''')
    print('You are standing on the front porch facing The Schrantz Residence.')
    print('The porch goes across the front of the house.')
    print('If you turn east you are facing the garage if you turn west you will be facing the Cuyahoga Valley National Park')  

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
                  'east' : 'Garage',
                  'south' : 'Front Yard',
                  'west' : 'Left Side of House',
                },

            'Front Entryway' : {
                  'north' : 'Hall',
                  'east' : 'Office',
                  'south' : 'Front Porch',
                  'west' : 'Living Room',
                  'upstairs' : 'Top of Stairs'
                },

            'Hall' : {
                  'north' : 'Bar Area',
                  'east' : 'Half Bathroom',
                  'south' : 'Front Entryway',
                  'west' : 'Just a Wall'
               },

            'Office' : {
                  'north' : 'Kitchen',
                  'east' : 'Just a Wall',
                  'south' : 'Just a Window',
                  'west' : 'Front Entryway'
               },

            'Bar Area' : {
                  'north' : 'Back Deck',
                  'east' : 'Kitchen',
                  'south' : 'Hall',
                  'west' : 'Dining Room',
                  'downstairs' : 'Bottom of Basement Steps'
              },

            'Living Room' : {
                  'north' : 'Dining Room',
                  'east' : 'Front Entryway',
                  'south' : 'Just a Window',
                  'west' : 'Just a Wall'
                   },

            'Dining Room' : {
                  'north' : 'Screened-in Back Porch',
                  'east' : 'Just a Window',
                  'south' : 'Living Room',
                  'west' : 'Bar Area'
                  },

            'Kitchen' : {
                  'north' : 'Just a Window',
                  'east' : 'Mud Room',
                  'south' : 'Office',
                  'west' : 'Bar Area'
                  },

            'Half Bathroom' : {
                  'north' : 'Just a Toilet',
                  'east' : 'Just a Wall',
                  'south' : 'Just a Sink',
                  'west' : 'Hall'
                  },

            'Mud Room' : {
                  'north' : 'Back Deck',
                  'east' : 'Laundry Room',
                  'south' : 'Garage',
                  'west' : 'Kitchen'
                  },

            'Laundry Room' : {
                    'north' : 'Just a Window',
                    'east' : 'Just a Wall',
                    'south' : 'Just a Wall',
                    'west' : 'Mud Room'
                    },

            'Back Deck' : {
                    'north' : 'Just a Ravine',
                    'east' : 'Just a Ravine',
                    'southwest' : 'Bar Area',
                    'southeast' : 'Mud Room',
                    'west' : 'Screened-in Back Porch'
                    },

            'Screened-in Back Porch' : {
                    'north' : 'Ravine',
                    'east' : 'Back Deck',
                    'south' : 'Dining Room',
                    'west' : 'Back Yard'
                    },

            'Back Yard' : {
                    'north' : 'Ravine',
                    'east' : 'Screened-in Back Porch',
                    'south' : 'Left Side of House',
                    'west' : 'Just the Neighbors House'
                    },

            'Left Side of House' : {
                    'north' : 'Back Yard',
                    'east' : 'Just the outside of House',
                    'south' : 'Front Yard',
                    'west' : 'Just the Neighbors House'
                    },

            'Front Yard' : {
                    'northwest' : 'Left Side of House',
                    'north' : 'Front Porch',
                    'east' : 'Driveway',
                    'south' : 'Just the Street',
                    'west' : 'Just the Neighbors House'
                    },

            'Driveway' : {
                    'north' : 'Garage',
                    'northeast' : 'Right Side of House',
                    'east' : 'Just the Neighbors House',
                    'south' : 'Just the Street',
                    'west' : 'Front Yard'
                    },

            'Garage' : {
                    'north' : 'Mud Room',
                    'east' : 'Just a Wall',
                    'south' : 'Driveway',
                    'west' : 'Just a Wall'
                    },

            'Right Side of House' : {
                    'north' : 'Back of House',
                    'east' : 'Just the Neighbors House',
                    'south' : 'Driveway',
                    'west' : 'Just the outside wall of the house'
                    },

            'Back of House' : {
                    'north' : 'Just the Ravine',
                    'east' : 'Just the Neighbors House',
                    'south' : 'Right Side of House',
                    'west' : 'Back Deck'
                    },

            'Bottom of Basement Steps' : {
                    'upstairs' : 'Bar Area',
                    'east' : 'Finished Basement Area',
                    'south' : 'Just a Wall',
                    'west' : 'Unfinished Basement Area'
                    },

            'Finished Basement Area' : {
                    'north' : 'Just a Wall',
                    'east' : 'Just a Wall',
                    'south' : 'Just a Wall',
                    'southwest' : 'Bottom of Basement Steps',
                    'northwest' : 'Unfinished Basement Area',
                    'west' : 'Wall'
                    },

            'Unfinished Basement Area' : {
                    'north' : 'Just a Wall',
                    'northeast' : 'Finished Basement Area',
                    'east' : 'Just a Wall',
                    'south' : 'Just a Wall',
                    'southeast' : 'Bottom of Basement Steps',
                    'west' : 'Just a Wall'
                    },

            'Top of Stairs' : {
                    'north' : 'Guest Bathroom',
                    'east' : 'Master Bedroom',
                    'south' : 'Front Entry Way',
                    'west' : 'Upstairs Hall',
                    'downstairs' : 'Front Entry Way'
                    },

            'Guest Bathroom' : {
                    'north' : 'Just a Toilet',
                    'east' : 'Just a Sink',
                    'south' : 'Top of Stairs',
                    'west' : 'Just a Shower'
                    },

            'Master Bedroom' : {
                    'north' : 'Master Bathroom',
                    'east' : 'Just a Closet',
                    'south' : 'Just a Closet',
                    'west' : 'Top of Stairs'
                    },
            'Upstairs Hall' : {
                    'north' : 'Just A Wall',
                    'northwest' : 'Bedroom 1',
                    'east' : 'Top of Stairs',
                    'south' : 'Bedroom 3',
                    'southwest' : 'Bedroom 2',
                    'west' : 'Just a Wall'
                    },
            'Bedroom 1 ' : {
                    'north' : 'Just a Closet',
                    'east' : 'Upstairs Hall',
                    'south' : 'Just a Wall',
                    'west' : 'Just a Window'
                    },
            'Bedroom 2' : {
                    'north' : 'Just a Closet',
                    'east' : 'Upstairs Hall',
                    'south' : 'Just a Window',
                    'west' : 'Just a Wall'
                    },
            'Bedroom 3' : {
                    'north' : 'Upstairs Hall',
                    'east' : 'Just a Wall',
                    'south' : 'Just a Window',
                    'west' : 'Just a Closet'
                    },
            'Master Bathroom' : {
                    'north' : 'Just a Shower',
                    'east' : 'Just a Toilet',
                    'south' : 'Master Bedroom',
                    'west' : print('Just a Sink')
                    },


            }

#start the player in the Hall
currentRoom = 'Front Porch'

os.system('clear')

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
  os.system('clear')
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

    if currentRoom == 'Front Porch':
        print('You are standing on the front porch facing The Schrantz Residence.') 
        print('The porch goes across the front of the house.')
        print('If you turn east you are facing the garage if you turn west you will be facing the Cuyahoga Valley National Park')

