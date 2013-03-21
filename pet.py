from settings import *

import random

class Pet(object):
    def __init__(self, posx, posy, program, defense, speed, attack, gather):
        # Instruction set
        self.program = program

        # Initialize the reproduction cycle
        self.init_reproduction()

        # Position in the world
        self.posx = posx
        self.posy = posy

        # Health
        self.health = 1

        # Abilities
        # 0 = no defense, 1 = attacks have no effect
        self.defense = defense
        self.speed = speed
        # Absolute number of health points removed when attacking others
        self.attack = attack
        # Factor of gathering speed
        self.gather = gather

        # Energy level
        self.energy = 1

        # Resources
        self.wood = 0
        self.stone = 0
        self.fruit = 0

        # Current execution place
        self.ctr = 0
    def init_reproduction(self):
        self.reproduction = ["EMPTY"] * random.randint(
                            len(self.program) - 10,
                            len(self.program) + 10
                        )
        self.gestating = False


    def get_pos(self):
        return (self.posx, self.posy)

    def get_attack(self):
        return self.attack

    def is_gestating(self):
        return self.gestating


    def step(self, callback):
        # Reduce by constant energy drain
        self.energy -= ENERGY_DRAIN

        # Increase health by constant healing
        self.health += HEALING_GAIN

        # Do continuous conversion of gathered resources into energy
        self.convert_resources()

        # If gestating, reduce the counter of number of steps left to gestate
        if self.is_gestating():
            self.gestation_left -= 1
            if self.gestation_left == 0:
                # The offspring is ready to be born
                callback(self, "OffspringReady")
                self.init_reproduction()

        # Execute the instruction
        instruction = self.program[self.ctr]

        if instruction == "Sleep":
            # Increase health, but only up to 1
            self.health = min(self.health + HEALTH_GAIN_BY_SLEEP, 1)

        # Increase efficiency of various capabilities
        elif instruction == "IncreaseDefence":
            self.defense = self.defense + DEFENSE_GAIN
        elif instruction == "IncreaseSpeed":
            self.speed = self.speed + SPEED_GAIN
        elif instruction == "IncreaseAttack":
            self.attack = self.attack + ATTACK_GAIN
        elif instruction == "IncreaseGather":
            self.gather = self.gather + GATHER_GAIN

        elif instruction == "GatherSun":
            # Sun is everywhere and always available
            self.energy += SUN_CONVERSION

        else:
            # Has to be handled by higher authority:
            #       GatherWood
            #       GatherStone
            #       GatherFruit
            #       Attack
            #       MoveUp
            #       MoveDown
            #       MoveLeft
            #       MoveRight
            #       Mate
            callback(self, instruction)

        self.ctr += 1
        if self.ctr == len(self.program):
            self.ctr = 0

    def convert_resources(self):
        wood_energy = max(WOOD_CONVERSION, 0)
        self.wood -= wood_energy

        stone_energy = max(STONE_CONVERSION, 0)
        self.stone -= stone_energy

        fruit_energy = max(FRUIT_CONVERSION, 0)
        self.fruit -= fruit_energy

        self.energy += wood_energy + stone_energy + fruit_energy

    def gestate(self):
        self.gestating = True
        self.gestation_left = len(self.reproduction)

    def move_up(self):
        self.posy += 1

    def move_down(self):
        self.posy -= 1

    def move_right(self):
        self.posx += 1

    def move_left(self):
        self.posx -= 1

    def gather_wood(self):
        amount_gathered = self.gather * WOOD_GATHER_SPEED
        self.wood += amount_gathered
        return amount_gathered

    def gather_stone(self):
        amount_gathered = self.gather * STONE_GATHER_SPEED
        self.stone += amount_gathered
        return amount_gathered

    def gather_fruit(self):
        amount_gathered = self.gather * FRUIT_GATHER_SPEED
        self.fruit += amount_gathered
        return amount_gathered

    def defend(self, attack):
        self.health -= attack * self.defense

    def mate(self, freepositions):
        i = random.randint(1, len(freepositions))
        wish_position = freepositions[i - 1]
        if len(self.program) >= wish_position + 1:
            return (wish_position, self.program[wish_position])
        return (random.choice(freepositions), random.choice(INSTRUCTIONS))

    def free_reproduction(self):
        return [i for i,x in enumerate(self.reproduction) if x == "EMPTY"]

    def write_reproduction(self, write):
        if random.uniform(0, 1/MUTATION_RATE) > 1:
            self.reproduction[write[0]] = write[1]
        else:
            # Mutation!
            self.reproduction[write[0]] = random.choice(INSTRUCTIONS)
        if "EMPTY" not in self.reproduction:
            self.gestate()