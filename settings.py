# Absolute health increase by sleeping one step
HEALTH_GAIN_BY_SLEEP = 0.01

# Absolute energy amount drained for each step
ENERGY_DRAIN = 0.01

HEALING_GAIN = 0.01

# Absolute gain in capabilities
DEFENSE_GAIN = 0.01
SPEED_GAIN = 0.01
ATTACK_GAIN = 0.01
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

# Resource availability
MAX_WOOD = 10
MAX_STONE = 100
MAX_FRUIT = 2

# Rate of reproduction write scrambling
MUTATION_RATE = 0.01


INSTRUCTIONS = [
        "Sleep", "IncreaseDefence", "IncreaseSpeed",
        "IncreaseAttack", "IncreaseGather", "Mate",
        "GatherSun", "GatherWood", "GatherStone",
        "GatherFruit", "Attack", "MoveUp",
        "MoveDown", "MoveLeft", "MoveRight"
    ]

DRAW_FACTOR = 10
