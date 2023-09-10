# Create Modules
import mathematic

mathematic.sum(1,2)
mathematic.minus(10,5)


# Rename Modules
import mathematic as math
import mathematic as m
import mathematic as a

# sum, minus
math.sum(1,5)
math.minus(10,5)

# times, divided
m.times(1,5)
a.divided(10,5)


# Import Modules
# 1 Specific Modules
from mathematic import sum, minus

sum(1,5) 
minus(1,5) 
# divided(10,5)   # EROR --> Cause just import sum and minus

# 2 All Modules
from mathematic import *   # Import All Data

sum(1,5) 
minus(1,5) 
divided(10,5)


# Import and Rename Modules
from mathematic import times as time
time(10,5)
