import time
class Rover(object):
	"""
	Object(Rover)

	The Mars Rover Object 
	Controls movements of rover 
	"""
	def __init__(self, x,y,heading="N", instruction=None): 
		"""
		Init Rover

		Inialize rover with starting position, heading and instructions 

		@param int x starting x
		@param int x starting y
		@param char heading Cardinal character for heading N|E|S|W
		@param string heading starting heading 
		"""
		self.x = x
		self.y = y
		self.degrees = Rover.get_reverse_heading(heading)
		self.instructions = instruction

	
	def execute(self,bbx, bby, animate=None,grid=None):
		"""
		Execute Instruction
		
		@param int bbx Boundry Box X
		@param int bby Boundry Box Y
		@param int animate set grid animation interval
		@param Object(Plateau) 
		@return string position

		"""
		
		for i in self.instructions: 
			if i == "M": self.move(bbx, bby)
			else: self.set_bearing(i)

			if animate and grid:
				print('\033c') 
				view = grid.print_y()
				print("\n".join(view))
				print(self.describe())
				time.sleep(1)


		return self.describe()

	def move(self, bbx,bby):
		"""
		Move Rover 

		Move rover 1 space forward relative to 
		int heading

		Do not allow the rover to exceed boundry of grid

		@param int bbx Boundry Box X
		@param int bby Boundry Box Y
		@return int coord X|Y
		"""
		movement = {
			"N" : ("y", 1),
			"S" : ("y", -1),
			"W" : ("x", -1),
			"E" : ("x", 1),
		}[self.heading]
		attr,increment = movement

		movement = getattr(self, attr) + increment 

		setattr(self, attr, movement) 
		#Do not allow rover to exceed boundry
		if self.y > bby: self.y = bby
		if self.x > bbx: self.x = bbx
		if self.x < 0: self.x = 0
		if self.y < 0: self.y = 0

		return getattr(self, attr)


	def set_bearing(self, instruction):
		"""
		Set Bearing

		Adjust bearing base on instruction, this function
		will move rover 90 to left or right 

		@param char instriction L|R
		@return int bearing
		"""
		bearing = {"L" : -90, "R" : 90 }[instruction]
		self.degrees += bearing 

		#Keep bearing within range incase some goes to far left/right
		if self.degrees >= 360:
			self.degrees -= 360
		
		if self.degrees < 0:
			self.degrees += 360

		return self.degrees

	def describe(self,):
		"""
		Describe 

		Get current position of Rover
		@return string position
		"""
		return "%s %s %s" % (self.x, self.y, self.heading)

	@property
	def heading(self,):
		"""
		Heading 

		Get cardinal heading based on current bearing

		@return string heading N|E|S|W
		"""
		return Rover.get_heading(self.degrees)
	
	
	def render(self,):
		"""
		Render

		Get visual representation of heading 
		@return string <>^v
		"""
		return self.arrows(self.heading)

	@staticmethod
	def arrows(heading):
		"""
		Arrows 

		Static config for rendering rover animation
		@return string <>^v
		"""
		return {
			"N" : "^",
			"E" : ">",
			"S" : "v",
			"W" : "<",
		}[heading]

	@staticmethod
	def get_reverse_heading(cardinal): 
		"""
		Reverse Heading 

		Static config for converting cardinal heading to degrees
		@return int degrees
		"""
		return {
			"N" : 0,
			"E" : 90,
			"S" : 180,
			"W" : 270,
		}[cardinal]

	@staticmethod
	def get_heading(heading):
		"""
		Heading

		Static config to convert degrees into cardinal heading
		@return string heading 
		"""
		#Keep heading with 360 bounds
		if heading >= 360:
			heading -= 360
		
		if heading < 0:
			heading += 360

		return {
			0 : "N", 
			90 : "E",
			180 : "S",
			270 : "W",
		}[heading] 


class Plateau(object):
	"""
	Plateau (Grid) 
	The grid object on which the rovers will move
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def rovers(self, rovers):
		"""
		Assign Rover to grid 
		array rovers [object Rover]
		"""
		self.rovers = rovers

	def render(self): 
		"""
		Print Grid To Screen
		"""
		
		for rover in self.rovers:
			rover.execute(self.x, self.y,1, self)
			# print('\033c') 
			# grid = self.print_y()
			# print("\n".join(grid))

	def print_y(self,):
		"""
		Render Y Axis
		"""
		grid = []

		for y in range(0, self.y)[::-1]: 
			grid.append(self.print_x_at(y))
		return grid

	def print_x_at(self,y): 
		"""
		Render Y Axis

		Plot rovers @ given coordinates if found
		"""
		points = [ self.rover_at(x, y) for x in range(0, self.x)]
		return "".join(points)

	def rover_at(self,x,y):
		"""
		Rover @

		Find & render rover @ give coordinates
		"""
		for r in self.rovers:
			if r.x == x and r.y == y:
				return r.render()
		return "."

		
