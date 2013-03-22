# Absolute health increase by sleeping one step
HEALTH_GAIN_BY_SLEEP = 0.01

# Absolute energy amount drained for each step
ENERGY_DRAIN = 0.035

HEALING_GAIN = 0.01

MAX_ENERGY = 10

# Increase in health when attacking someone
ATTACK_HEALTH_INCREASE = 0.05

# Absolute gain in capabilities
DEFENSE_GAIN = 0.02
SPEED_GAIN = 0.01
ATTACK_GAIN = 0.02
GATHER_GAIN = 0.01

# Conversion factors for resources
SUN_CONVERSION = 0.005
WOOD_CONVERSION = 0.5
STONE_CONVERSION = 0.05
FRUIT_CONVERSION = 1

# Gather speed for resources
WOOD_GATHER_SPEED = 3
STONE_GATHER_SPEED = 3
FRUIT_GATHER_SPEED = 3

# How much of each resource can a pet carry
MAX_CARRYING_CAPACITY = 20

# Resource availability
MAX_WOOD = 2
MAX_STONE = 10
MAX_FRUIT = 0.5

# Rate of reproduction write scrambling
MUTATION_RATE = 0.05

# Percentage/100 of time steps a write happens 
# to the own reproduction storage
SELF_WRITE_RATIO = 0.05


INSTRUCTIONS = [
        "Sleep", "IncreaseDefence", "IncreaseSpeed",
        "IncreaseAttack", "IncreaseGather", "Mate",
        "GatherSun", "GatherWood", "GatherStone",
        "GatherFruit", "Attack", "MoveUp",
        "MoveDown", "MoveLeft", "MoveRight"
    ]

DRAW_FACTOR = 20
