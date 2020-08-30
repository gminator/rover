from models import Plateau, Rover

rovers = [Rover(1,2,"N","LMLMLMLMM"), Rover(2,3,"E","MMRMMRMRRM")]
plateau = Plateau(5,5)
plateau.rovers(rovers)
plateau.render()