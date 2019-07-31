# Game Engine Unit of Capstone Adventure Game Version 1 (Week 4)
# 
# v1.1 --> change "Room" class to "Place" and enable 3D movement (just "up/down")
# v2  --> add "Thing" class
# v3 --> add support and error handling for "look" action
# v4 --> finish support and error handling for "take", "drop", "look", "sleep"
# v5 --> additional error handling. refine sleep action
# v6 --> implement show_help and show_inventory
# v7 --> update "look"/"take"/"drop" and time with integration/gameplay issue fixes
# v8 --> change print statements to incorporate formatted output
# v9 --> implement "doors" on places that have doors (changes in playgame.py as well)
# v10 --> change 'up' and 'down' to 'u' and 'd' to match parser
# v11 --> descriptions of Place now based on number of visits as well
# v11.1 --> implement "search" and "read"
# v11.2 --> toggle item description for when it is present/not present//viewable/not viewable 
# v11.3 --> accommodate alternate thing names (e.g. "scrap of fabric"/"fabric scrap"/"scrap"/"fabric")
# v12
# v13
# define the "Game" class

# import sys
# sys.path.insert(0, '/path/to/application/app/folder')
#
# import file
#
#
#
import action
from output import *

class Game:

	# constructor expects: 
	# day(int), time(int)
	def __init__(self, day, time):
		self.places = {}
		self.isValid = {}
		self.day = day	# time component new in v1.1
		self.time = time

	def setUser(self, user):
		self.user = user

	def addPlace(self, place):
		self.places[place.name] = place

	# takes the change in hours per an event in the game
	def updateTime(self, timeChange):
		self.time += timeChange
		
		# v7: if we've crossed into a new 40-hr day
		if self.time > 39: 
			self.time -= 39 
			self.day = self.day + 1

	def getPlace(self, name):
		if name in self.places.keys():
			return self.places[name]
		return None


	# v3: prints the description of a feature or object 
	# v11.2: also prints description of other objects dependent on this one 
	# v11.3: allow alternate thing names
	def showThing(self, itemname):
		for t in self.user.things:
			if t.name.lower() == itemname or itemname in t.altNames:
				des = t.getDescription(self.time)
				Output.print_look(des) 
				return
		for t in self.user.current_place.things:
			if t.name.lower() == itemname or itemname in t.altNames:
				des = t.getDescription(self.time) 
				Output.print_look(des)
				# v11.2: if there are other objects viewable because of this one,
				# describe those other objects also.
				for obj in t.hasOtherItems:
					for thingObj in self.user.current_place.things:
						if obj.lower() == thingObj.name.lower():
							Output.print_look(thingObj.isHereDescription)
							return
		#v12 character interaction for looking at character
		if self.user.current_place.hasCharacter:
			character = self.user.current_place.character
			if character.name == itemname or itemname in character.altNames:
				Output.print_look(character.getDescription(self.time))
				return

		#for c in self.user.current_place.character.names: 
		#	if c == itemname:
		#		description = self.user.current_place.character.getLook()
		#		print(description)


    # v3: takes the thing the user wants to examine
    # prints appropriate outputs
	# v7: handle two-word obj names
	def handleLook(self, attemptedObj, indirObj, canLook):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if canLook:
			# if nothing or "room" specified, examine current room 
			if attemptedObj == None or attemptedObj == "room":
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumLooks()
			# if current room name specified, examine current room
			elif attemptedObj == self.user.current_place.name.lower():
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumLooks()
			# print thing description if thing available for examining
			else:
				self.showThing(attemptedObj)
		else:
			# if user tries to examine a room that is not the current one, error
			for placename in self.places.keys():
				if attemptedObj == placename.lower():
					Output.print_error("You can\'t look around a room if you aren\'t in it.")
					return
			# otherwise print generic error msg
			Output.print_error("You don\'t see that here.")


	# v4: handle output for "take", "drop", "sleep"
	# v7: handle two-word obj names
	def handleTake(self, attemptedObj, indirObj, takeable):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if takeable:
			if self.user.userHasThing(attemptedObj): 
				Output.print_error("You can\'t take what\'s already in your inventory.")
			else:
				Output.print_take(attemptedObj)
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to take.")
				return 
			# thing is in current room but not takeable
			if self.user.current_place.roomHasThing(attemptedObj): 
				Output.print_error("You can\'t put that in your inventory.")
				return
			# thing is not in current room
			Output.print_error("You don\'t see a " + attemptedObj + " that you can take.")

	def handleDrop(self, attemptedObj, indirObj, canDrop):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj

		if canDrop:
			Output.print_drop(attemptedObj) 
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to drop.")
			else:
				Output.print_error("You can\'t drop something that\'s not in your inventory.")	

	def handleSleep(self, attemptedObj, canSleep):
		if canSleep:
			print("You sleep.")
		else:
			if self.user.current_place.name != "Spare Room":
				Output.print_input_hint("You can only sleep in your room. You are not in your room at the moment.")
			elif self.time > 5 and self.time < 25: 
				Output.print_input_hint("You can only sleep at night.")
			elif attemptedObj != None and attemptedObj != "bed":
				Output.print_input_hint("You can only sleep on a bed.") 
			else:
				Output.print_input_hint("You aren\'t sleepy right now.")

	# new in v11.1
	def handleSearch(self, attemptedObj, indirObj, canSearch):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj
		if canSearch:
			print("You search the {}.".format(attemptedObj))
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to search.")
				return
			Output.print_error("That\'s not something you can search.")

	def handleRead(self, attemptedObj, indirObj, canRead):
		if indirObj != None:
			attemptedObj = attemptedObj + " " + indirObj
		if canRead:
			print("You read the {}.".format(attemptedObj))
		else:
			if attemptedObj == None:
				Output.print_input_hint("Try being more specific about what you want to read.")
				return
			Output.print_error("That\'s not something you can read.")

	# new in v9: print special error message for locked door
	def handleLockedDoor(self, direction):

		doors = self.user.current_place.doors

		# v11.1: fix "go to X" bug.
		# If direction is None, attempting to access doors[direction] crashes the game.  
		if direction == None:
			Output.print_error("That\'s not somewhere you can go.")

		# if there is a door, and the move is invalid, then "locked"
		elif doors[direction] == "locked":
			Output.doorIsLocked(self.user.current_place.name, True)

		# otherwise, there is no place in that direction
		else:
			Output.print_error("There is no place in the " + direction + " direction")

	# v12 handling talking to characters
	def handleTalk(self, attemptedObj, canTalk):
		if canTalk:
			character = self.user.current_place.character
			if character.name.lower() == attemptedObj.lower():
				Output.print_talk(character.getCharacterSpeak(self.time))
				return
		else:
			print("You can not talk to " + attemptedObj)


	# v6: displays list of supported verbs
	def showHelp(self):
		print("go\nmove\nrun\nwalk\nhead\nhurry\n")
		print("get\npick up\nkeep\ntake\ngrab\nsteal\n")
		print("drop\nabandon\ndiscard\ntrash\n")
		print("look\nl\nlook at\nstudy\nread\nexamine\nx\nsearch\n")
		print("talk\nsay\ngreet\nask\nchat\nspeak\n")
		print("sleep\nrest\nrelax\nopen\nunlock\n")

	# point of entry from parser, game takes care of input from this point
	# either by updating the game or sending error messages
	def fromParserToGame(self, action): 
		
		valid = self.checkIsValid(action)

		if(valid):

			self.executeRequest(action)

			# update the list of valid moves in the new game state
			self.setIsValid()
			
			# if the user was moved, re-orient user
			if action.verb == "move_user":
				self.user.current_place.printRoom(self.time)
				self.user.current_place.updateNumEntries()
 
		else: 
			if action.verb == "move_user": # new in v9: check if move is invalid due to locked door
				self.handleLockedDoor(action.direction)
			elif action.verb == "look":
				self.handleLook(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "take":
				self.handleTake(action.direct_obj, action.indirect_obj, False) 
			elif action.verb == "move_user":
				Output.print_error("You can\'t move in that direction. Try another.")
			elif action.verb == "drop":
				self.handleDrop(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "sleep":
				self.handleSleep(action.direct_obj, False)
			elif action.verb == "search":
				self.handleSearch(action.direct_obj, action.indirect_obj, False)
			elif action.verb == "read":
				self.handleRead(action.direct_obj, action.indirect_obj, False)
			elif action.verb == None and action.direct_obj != None:
				Output.print_input_hint("Try being more specific about what you want to do with the {}.".format(action.direct_obj))
			else:
				# thing is present, but action.verb is not one of the thing's allowed verbs
				if self.user.canAccessThing(action.direct_obj) and not self.user.canActOnThing(action.direct_obj, action.verb):
					Output.print_error("You can\'t " + action.verb + " the " + action.direct_obj + ". Try doing something else with it.")
				else:
					Output.print_error("You don\'t see the point of doing that right now.")

	# called after every change in game state in preparation for next input from parser
	def setIsValid(self):
		
		newdict={} 
		
		user_place = self.user.current_place
		
		adjacent_places = self.user.current_place.adjacent_places
   
		# create a list of available move locations
		# new in v9, update to account for locked opposing doors (if going north, check place north south door is not locked)
		valid_moves = []
		if adjacent_places[0] is not None:
			if adjacent_places[0].doors["s"] is not "locked":
				valid_moves.append("n")
		if adjacent_places[1] is not None: 
			if adjacent_places[1].doors["sw"] is not "locked":
				valid_moves.append("ne")
		if adjacent_places[2] is not None:
			if adjacent_places[2].doors["w"] is not "locked":
				valid_moves.append("e")
		if adjacent_places[3] is not None: 
			if adjacent_places[3].doors["nw"] is not "locked":
				valid_moves.append("se")
		if adjacent_places[4] is not None: 
			if adjacent_places[4].doors["n"] is not "locked":
				valid_moves.append("s")
		if adjacent_places[5] is not None: 
			if adjacent_places[5].doors["ne"] is not "locked":
				valid_moves.append("sw")
		if adjacent_places[6] is not None: 
			if adjacent_places[6].doors["e"] is not "locked":
				valid_moves.append("w")
		if adjacent_places[7] is not None: 
			if adjacent_places[7].doors["se"] is not "locked":
				valid_moves.append("nw")
		if adjacent_places[8] is not None: 
			if adjacent_places[8].doors["d"] is not "locked":
				valid_moves.append("u")
		if adjacent_places[9] is not None: 
			if adjacent_places[9].doors["u"] is not "locked":
				valid_moves.append("d")

		# v11.3: change from strings to objects 
		valid_takes = [item for item in user_place.things if item.is_takeable]
		valid_drops = [item for item in self.user.things]
		valid_looks = [item for item in user_place.things]
		for item in self.user.things:
			valid_looks.append(item)
	
		valid_searches = [item for item in user_place.things if item.is_searchable]
		valid_reads = [item for item in user_place.things if item.is_readable]
		for item in self.user.things:
			if item.is_readable:
				valid_reads.append(item)


		# v12 add a character to the list of things to look at and talk with
		valid_talks = []
		if user_place.hasCharacter: 
			valid_looks.append(user_place.character) # character is a Thing obj
			valid_talks.append(user_place.character) # you can also talk to characters

		# set the dictionary with keys as actions and values as valid corresponding things
		newdict = {"move_user": valid_moves, "take": valid_takes, "drop": valid_drops, "look": valid_looks, "search": valid_searches, "read": valid_reads, "talk_npc": valid_talks}

		# set the "is valid" attribute to the current dictionary of valid game operations
		self.isValid = newdict

	# take action object and consult "isValid" dictionary 
	def checkIsValid(self, action): 
		if action.verb == "move_user":
			v = self.isValid.get("move_user")
			for i in v:
				if i == action.direction:
					return True
			return False
		elif action.verb == "take":
			# v7: make sure direct_obj is not None to avoid crash 
			if action.direct_obj == None:
				return False
			v = self.isValid.get("take")
			for i in v:
				#v11.3: check for alternate thing names
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True
			# new in v4: case where item is takeable but already in inventory
			if self.user.userHasThing(action.direct_obj):
				return True
			# v7
			if action.indirect_obj != None:
				objName = action.direct_obj + " " + action.indirect_obj
				if self.user.userHasThing(objName): 
					return True 
			return False
		elif action.verb == "drop":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("drop")
			for i in v:
				#v11.3: check for alternate thing names 
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True 
			return False

		# new in v3
		elif action.verb == "look":
			v = self.isValid.get("look")
			# check if specified object can be examined (is in current place or inventory)
			for i in v:
				if action.direct_obj != None:
					#v11.3: check for alternate thing names
					if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
                                		return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True
            # if no object specified or current room specified, examine room
			if action.direct_obj == None:
                        	return True
			if action.direct_obj == "room":
                        	return True
			if action.direct_obj == self.user.current_place.name.lower(): 
                        	return True
			return False

		# new in v4 
		elif action.verb == "sleep":
			# can only sleep on bed in Spare Room at night
			correctRoom = (self.user.current_place.name == "Spare Room")
			correctObj = (action.direct_obj == None or action.direct_obj == "bed")
			correctTime = (self.time >= 25 or self.time <= 5)
			if correctRoom and (correctObj and correctTime):
				return True
			else:
				return False

		# new in v6
		elif action.verb == "show_help":
			return True 
		elif action.verb == "show_inventory":
			return True

		# new in v11.1
		elif action.verb == "search":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("search")
			for i in v:
				#v11.3: check for alternate thing names
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True

		elif action.verb == "read":
			if action.direct_obj == None:
				return False
			v = self.isValid.get("read")
			for i in v:
				#v11.3: check for alternate thing names
				if i.name.lower() == action.direct_obj or action.direct_obj in i.altNames:
					return True
				if action.indirect_obj != None:
					objName = action.direct_obj + " " + action.indirect_obj
					if objName == i.name.lower() or objName in i.altNames:
						return True

		# v12 talking to things (characters)
		elif action.verb == "talk_npc":
			print("debug talk1")
			v = self.isValid.get("talk_npc")
			for i in v:
				print("Printing names to talk to:")
				print(i.name) 
				if action.direct_obj != None:
					print("thing has direct object")
					# other names for a person, like "him, her, woman"
					if i.name.lower() == action.direct_obj:
						print("debug talkA")
						return True
		else:
			print("returning false from checkIsValid")
			return False	


	# Precondition: called after checkIsValid() returns True
	def executeRequest(self, action):
		if action.verb == "move_user":
			self.moveUser(action.direction)
			self.updateTime(1)
			return

		if action.verb == "take":
			# v4: error handling
			self.handleTake(action.direct_obj, action.indirect_obj, True)
			# v7: two-word object names
			if action.indirect_obj != None:
				obj_name = action.direct_obj + " " + action.indirect_obj
			else:
				obj_name = action.direct_obj
			self.user.pickUpObject(obj_name)

			# time update of 1 hour 
			self.updateTime(1)
			return

		if action.verb == "drop":
			self.handleDrop(action.direct_obj, action.indirect_obj, True)
			if action.indirect_obj != None:
				obj_name = action.direct_obj + " " + action.indirect_obj
			else:
				obj_name = action.direct_obj
			self.user.dropObject(obj_name)
			# add a time update
			self.updateTime(1)
			return

		# updated to handle two-word object names 
		if action.verb == "look":
			self.handleLook(action.direct_obj, action.indirect_obj, True)
			self.updateTime(1)
			return

		if action.verb == "sleep":
			self.handleSleep(action.direct_obj, True)
			# move time to start of next day 
			self.time = 6
			self.day += 1
			return
		
		if action.verb == "talk_npc":
			print("executing talk")
			self.handleTalk(action.direct_obj, True)
			self.updateTime(1)
			return

		if action.verb == "show_help":
			self.showHelp()
			return 

		if action.verb == "show_inventory":
			self.user.printInventory()
			return
		if action.verb == "search":
			self.handleSearch(action.direct_obj, action.indirect_obj, True)
			return
		if action.verb == "read":
			self.handleRead(action.direct_obj, action.indirect_obj, True)
			return
		else:
			return

	# Precondition: place adjacency pre-validated
	# new in v9: it has also been verified that if there is a door, it is not locked
	def moveUser(self, direction):
		user_place = self.user.current_place
		adjacent_places = user_place.adjacent_places
		is_door = False

		if direction == "n":
			self.user.updatePlace(adjacent_places[0])
			if adjacent_places[0].doors["s"] == "unlocked":
				is_door = True
		elif direction == "ne":
			self.user.updatePlace(adjacent_places[1])
			if adjacent_places[1].doors["sw"] == "unlocked":
				is_door = True
		elif direction == "e":
			self.user.updatePlace(adjacent_places[2])
			if adjacent_places[2].doors["w"] == "unlocked":
				is_door = True
		elif direction == "se":
			self.user.updatePlace(adjacent_places[3])
			if adjacent_places[3].doors["nw"] == "unlocked":
				is_door = True
		elif direction == "s":
			self.user.updatePlace(adjacent_places[4])
			if adjacent_places[4].doors["n"] == "unlocked":
				is_door = True
		elif direction == "sw":
			self.user.updatePlace(adjacent_places[5])
			if adjacent_places[5].doors["ne"] == "unlocked":
				is_door = True
		elif direction == "w":
			self.user.updatePlace(adjacent_places[6])
			if adjacent_places[6].doors["e"] == "unlocked":
				is_door = True
		elif direction == "nw":
			self.user.updatePlace(adjacent_places[7])
			if adjacent_places[7].doors["se"] == "unlocked":
				is_door = True
		elif direction == "u":
			self.user.updatePlace(adjacent_places[8])
			if adjacent_places[8].doors["d"] == "unlocked":
				is_door = True
		elif direction == "d":
			self.user.updatePlace(adjacent_places[9])
			if adjacent_places[9].doors["u"] == "unlocked":
				is_door = True

		# new in v9
		# print door animation if there is a door
		new_place = self.user.current_place

		# v13 provision for the "leave" message on the Front Manor Grounds
		# only shows up on first entry into foyer
		if new_place.numTimesEntered == 0 and new_place.name.lower() == "foyer":
			print("You hurl yourself up the path as it starts to rain in earnest. Maude follows right on your heels, fishing an iron keyring out of her pockets. At the front door, she shoulders you aside, unlocks the door, and heaves it open with a grunt of effort, dragging you inside by the wrist and dumping you in a rain-soaked heap on the floor.")
		
		if (is_door):
			Output.newPlaceWithDoor(new_place.name)
		else: # not a door
			print("User moved " + direction + " to the " + new_place.name)

# define the "Place" class
class Place:
	# game(game object), name(string), day[], night[], adjacentPaceNames[10 strings], things[strings], doors{ })
	def __init__(self, game, name, day, night, adjacentPlaceNames, things = None, doors = None):
		self.name = name
		self.adjacent_place_names = adjacentPlaceNames 

		# new in v9: a dictionary of doors tracking: whether there is a door, and whether it is locked or unlocked
		# dictionary: key is direction, value is either 'locked', 'unlocked', or None
		self.doors = doors

		# fixed constructor
		if things is not None:
			self.things = things
		else:
			self.things = []
		
		self.numTimesEntered = -1
		self.numTimesLooked = -1	

		# v11 day and night are arrays with different values based on "userVisitCount"
		self.day = day
		self.night = night

		game.addPlace(self) # creates a map between name and place object in the game

		# v12 characters as part of places
		self.character = None
		self.hasCharacter = False

	# new in v9 update the doors dictionary when a door becomes locked
	def lockDoor(self, direction):
		self.doors[direction] = "locked"

	# new in v9 update the doors dictionary when a door becomes unlocked
	def unlockDoor(self, direction):
		self.doors[direction] = "unlocked"

	#  translates array to "adjacentplaces" array after all places created
	def setAdjacentPlaces(self, game):
		self.adjacent_places = list(map(game.getPlace, self.adjacent_place_names))

	# v11 return a description that also considers the how many times the user has been there
	def getDescriptionBasedOnTimeAndVisitCount(self, time): 
		# v7: longer clock (40 hours) to allow more moves per day 
		uvc = self.numTimesEntered
		if uvc == -1:
			uvc = 0
		if uvc > 2:
			uvc = 2
		if time > 5 and time < 25: 
			return self.day[uvc]
		else:
			return self.night[uvc]
	
	# new in v2 (correpond to take and drop)
	def addThing(self, thing):
		self.things.append(thing)

	# v12 adding character to place
	def addCharacter(self, thing):
		self.character = thing
		self.hasCharacter = True

	def removeThing(self, thing):
		self.things.remove(thing)

	# check if a thing is in a room
	def roomHasThing(self, itemname):
		for t in self.things:
			# v11.2: check for alternate thing names
			if t.name.lower() == itemname or itemname in t.altNames: 
				return True
		return False	

	# v5: updates number of times examined
	def updateNumLooks(self):
		self.numTimesLooked += 1

	# v5: update number of entries
	def updateNumEntries(self):
		self.numTimesEntered += 1

	# v5: display room description
	def printRoom(self, time):
		place_name = self.name
		place_description = self.getDescriptionBasedOnTimeAndVisitCount(time)
		# v9: call output function to orient user 
		Output.orientUser(place_name, place_description)

	# v12 character related functions
	def addCharacter(self, thing):
		self.character = thing
		self.hasCharacter = True # character can be turned "off", so isValid can use hasCharacter to determine

# define the User class
class User:
	# game(game object), name(string), place name (string), user direction(string), saved game(bool) 
	def __init__(self, game, name, startingPlace, startingDirection, saved):
		if saved == False:
			self.name = name
			self.current_place = game.getPlace(startingPlace)
			self.direction = startingDirection

			# new in v2
			arr = []
			self.things = arr
		else:
			print("Constructing user from saved game")

	def getUserDirection(self):
		return self.direction

	def updateUserDirection(self, newDirection):
		self.direction = newDirection 
	
	# new in v2
	def pickUpObject(self, thing_name):
		# EDIT get actual thing obj reference 
		room_things = self.current_place.things
		for t in room_things:
			# v11.3: check for alternate thing names
			if t.name == thing_name or thing_name in t.altNames:
				thing = t
				# v4: only add to inventory if not already in it
				if self.userHasThing(thing.name) == False: 
					# add to user array
					self.things.append(thing)
					# remove the thing from the Place it is in
					self.current_place.removeThing(thing)

	# new in v2
	def dropObject(self, thing_name):
		# EDIT get actual thing obj reference, only remove if user has
		if self.userHasThing(thing_name):
			for t in self.things:
				# v11.3: check for alternate thing names
				if t.name == thing_name or thing_name in t.altNames:
					thing = t
					# remove from user array
					self.things.remove(thing)
					# add thing to the place the user is in
					self.current_place.addThing(thing)
					break

	# new in v2, for figuring out if user has an thing in possession
	def userHasThing(self, itemname):
		found = False
		for t in self.things:
			# v11.3: check for alternate thing names 
			if t.name.lower() == itemname or itemname in t.altNames: 
				found = True
		return found

	def updatePlace(self, place):
		self.current_place = place
		# new in v11: num times entered
		self.current_place.updateNumEntries()

	def printUser(self, game):
		print("Username: " + self.name + " Current place: " + self.current_place.name)

	# v5: check if user can access a thing 
	def canAccessThing(self, itemname):
		if self.userHasThing(itemname) or self.current_place.roomHasThing(itemname):
			return True
		return False		

	# v5: check if user can perform a particular action on a thing 
	def canActOnThing(self, itemname, verb):
		if not self.canAccessThing(itemname):
			return False
		else:
			for t in self.things:
				#v11.3: check for alternate thing names
				if t.name == itemname or itemname in t.altNames:
					if verb in t.permittedVerbs:
						return True
			for t in self.current_place.things:
				if t.name == itemname or itemname in t.altNames:
					if verb in t.permittedVerbs:
						return True
			return False 

	# v6: show inventory contents
	def printInventory(self):
                if len(self.things) == 0:
                        print("You currently have nothing in your inventory.")
                else:
                	print("You have, in various locations on your person:")
                	for t in self.things:
                        	print(t.name)

	def getAllThingsInPlace(self):
		return self.things

#define the "Thing" class
class Thing: 
	def __init__(self, name, day, night, starting_location, is_takeable, is_character = None, char_day = None, char_night = None):
		self.name = name
		self.day = day     # size of 5
		self.night = night # size of 5
		self.location = starting_location # place object
		self.is_takeable = is_takeable # defines whether feature or object
		self.with_user = False
		# v11.1
		self.is_searchable = False
		self.is_readable = False
		self.hasBeenSearched = False

		# v11.2
		self.isHereDescription = "You see a " + self.name + " here."
 
		# v11.2: for things that have other things on/in them
		self.hasOtherItems = []
		# v11.3: alternate names for items
		self.altNames = [] 

		# v12 things can now be characters 
		self.is_character = is_character
		# set the day and night dialogue of the character
		if is_character is not False:
			print(self.name)
			self.char_day = char_day
			self.char_night = char_night

		# keep track of allowed verbs for each thing
		self.permittedVerbs = [] 

		self.numTimesRead = 0
		self.numTimesExamined = -1 # start at -1 to account for "+1" at beginning of getDescription/array indexing
		self.numTimesTalked = -1

	def getDescription(self, time):
		self.numTimesExamined += 1
		if time > 5 and time < 25:					# do we want this time of 5 - 25 here?
			if self.numTimesExamined > 5:
				return self.day[4]
			else:
				return self.day[self.numTimesExamined]
		else:
			if self.numTimesExamined > 5:
				return self.night[4]
			else:
				return self.night[self.numTimesExamined]

	# add a permitted verb for this thing 
	def addVerb(self, verb):
		self.permittedVerbs.append(verb)

	# when the user drops
	def leaveUser(self, new_location):
		self.location = new_location # place where user is dropping it
		self.with_user = False

	# when the user picks up
	def becomeWithUser(self):
		self.with_user = True

	# differentiates object from feature
	def isTakeable(self):
		return self.is_takeable

	# differentiate character from object or feature
	def isCharacter(self):
		return self.is_character

	# get the character's dialogue based on time of day and num of times talked prior
	# characters have up to 5 different things to say in the day and night, and after that just say the last thing
	def getCharacterSpeak(self, time):
		print("Debug time:")
		print(time)
		self.numTimesTalked += 1
		if time > 5 and time < 25:
			if self.numTimesTalked > 5:
				return self.char_day[4]
			else:
				return self.char_day[self.numTimesTalked]
		else:
			if self.numTimesTalked > 5:
				return self.char_night[4]
			else:
				return self.char_night[self.numTimesTalked]

	# edit description
	def editDescription(self, day, night):
		self.day = day
		self.night = night



