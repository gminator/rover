import unittest
from models import Plateau, Rover

class MarsUnitTest(unittest.TestCase):
 	
 	def test_execute(self):
 		"""
 		Main Test

 		Show output resulting from Maneuvers
 		"""
		rovers = {
			"Maneuver: Regular Move" : [[0,0, "N", "RMMLMMLM"],(5,5),"1 2 W"], 
			"Maneuver: Out of bounds(X)" : [[0,0, "N", "RMMLMMMLMMMMMMM"],(5,5),"0 3 W"], 
			"Maneuver: Out of bounds(Y)" : [[3,3, "E", "MMLMMMMMMMMM"],(5,5),"5 5 N"], 
		}
		for scenario, params in rovers.items(): 
			args, box, result = params
			rover = Rover(*args)
			current = rover.execute(*box)
			self.assertEqual(result, current, "%s!=%s in %s " % (result, current, scenario))

 	def test_move(self):
		rovers = {
			"Move north in boundry" : [[0,0, "N"],(5,5), 1], 
			"Move north out of boundry" : [[0,5, "N"],(5,5), 5], 
			"Arb move north in boundry" : [[0,4, "N"],(5,5), 5], 
			"Move w out boundry" : [[0,0, "W"],(5,5), 0], 
			"Move W in boundry" : [[3,0, "W"],(5,5), 2], 
			"Move E out boundry" : [[5,0, "E"],(5,5), 5], 
			"Move E in boundry" : [[4,0, "E"],(5,5), 5], 
		}

		for scenario, params in rovers.items(): 
			args, boundry, result = params
			rover = Rover(*args)
			coord = rover.move(*boundry)
			self.assertEqual(result, coord, "%s!=%s in %s " % (result, coord, scenario))

 	def test_set_bearing(self):
		rovers = {
			"N ->  W" : [[0,0, "N"], "L", "W"],
			"E -> S" : [[0,0, "E"], "R", "S"],
			"W -> N" : [[1,1, "W"], "R", "N"],
			"W -> S" : [[1,1, "W"], "L", "S"],
		}

		for scenario, params in rovers.items(): 
			arguments, insruction, heading = params
			
			rover = Rover(*arguments)

			rover.set_bearing(insruction)
			self.assertEqual(heading, rover.heading, "%s expecting %s but got %s" % (rover.degrees, heading, rover.heading))


	def test_get_heading(self):
		bearings = [(0, "N"), (90, "E"), (180, "S"), (270, "W"), (360, "N"), (450, "E"), (-90, "W")]
		for heading in bearings:		
			head, cardinal = heading
			output = Rover.get_heading(head)
			self.assertEqual(cardinal, output)

	def test_rover_at(self):
		scenarios = {
		"Scene 1: Origin Pass" : ((10,10), (0,0), (0,0), "^"),
		"Scene 2: Fail" : ((10,10), (0,0), (3,5), "."),
		"Scene 2: Off Origin" : ((60,40), (6,10), (6,10), "^")
		}

		for scenario, options in scenarios.items():
			grid,latlng,rover,result = options
			mars = Plateau(*grid)
			mars.rovers([Rover(*rover)])
			output = mars.rover_at(*latlng)
			self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
