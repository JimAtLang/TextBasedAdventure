from Directions import Directions
from Room import Room
from Passage import Passage

living_room = Room("Living room", "This is a big room with an old couch. There's a sword hanging above the couch.")
kitchen = Room("Kitchen", "The kitchen has a dining table, an oven, and a sink")
ktlr = Passage("Kitchen to living room","Just a regula door",living_room,Directions.EAST,kitchen)