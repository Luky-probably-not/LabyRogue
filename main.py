from func.labyGenerator import *
from func.mazeSolver import *
from func.moving import *
from func.mapLaby import *
from func.player import *

laby = Random(15)
laby.Empty()
laby = FillLaby(laby)
play(laby)
