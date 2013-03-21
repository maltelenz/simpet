import random
from time import sleep

from utilities import *
from settings import *
from pet import *
from pygameworld import *

class World(object):
    def __init__(self, xsize, ysize, pets):
        self.xsize = xsize
        self.ysize = ysize
        
        self.pets = pets
        
        self.time = 0

        # Generate an initial set of resources
        self.wood = [[random.randint(0, MAX_WOOD) for x in range(xsize)] for y in range(ysize)]
        self.stone = [[random.randint(0, MAX_STONE) for x in range(xsize)] for y in range(ysize)]
        self.fruit = [[random.randint(0, MAX_FRUIT) for x in range(xsize)] for y in range(ysize)]

    
    def step(self):
        """Take a discrete time step forward

            This will increase the internal time counter by one step,
            and call the step function for each of the pets present in this world.

            It will then resolve any interactions between pets,
            and do any pet modifications that result.

        """

        # Trigger a step in each of the pets
        # TODO iterate over randomized self.pets
        for p in self.pets:
            p.step(self.callback)

        self.time += 1


    def callback(self, pet, action):
        pet_position = pet.get_pos()

        # Gathering
        if action == "GatherWood":
            if self.has_wood(pet_position):
                self.detract_wood(pet_position, pet.gather_wood())
        elif action == "GatherStone":
            if self.has_stone(pet_position):
                self.detract_stone(pet_position, pet.gather_stone())
        elif action == "GatherFruit":
            if self.has_fruit(pet_position):
                self.detract_fruit(pet_position, pet.gather_fruit())
        
        # Attack
        elif action == "Attack":
            attack_strength = pet.get_attack()
            for p in self.neighbors(pet_position):
                p.defend(attack_strength)

        # Move
        elif action == "MoveUp":
            if self.possible_target_position(shift_position_up(pet_position)):
                pet.move_up()
        elif action == "MoveDown":
            if self.possible_target_position(shift_position_down(pet_position)):
                pet.move_down()
        elif action == "MoveLeft":
            if self.possible_target_position(shift_position_left(pet_position)):
                pet.move_left()
        elif action == "MoveRight":
            if self.possible_target_position(shift_position_right(pet_position)):
                pet.move_right()

        elif action == "Mate":
            # Write a piece of code to everyone near, including itself
            for p in self.neighbors(pet_position):
                if not p.is_gestating():
                    free_spaces = p.free_reproduction()
                    if free_spaces != []:
                        p.write_reproduction(pet.mate(free_spaces))

        elif action == "OffspringReady":
            self.new_pet(pet)

    def neighbors(self, position):
        return [n for n in self.pets if are_neighbors(n.get_pos(), position)]

    def possible_target_position(self, position):
        target_is_empty = [p for p in self.pets if p.get_pos() == position] == []
        target_is_on_map = 0 <= position[0] < self.xsize and 0 <= position[1] < self.ysize
        return target_is_empty and target_is_on_map

    # Check if there are resources available at a position
    def has_wood(self, position):
        return self.wood[position[0]][position[1]]

    def has_stone(self, position):
        return self.stone[position[0]][position[1]]

    def has_fruit(self, position):
        return self.fruit[position[0]][position[1]]

    # Detract resources when they are gathered
    def detract_wood(self, position, amount):
        self.wood[position[0]][position[1]] -= amount

    def detract_stone(self, position, amount):
        self.stone[position[0]][position[1]] -= amount

    def detract_fruit(self, position, amount):
        self.fruit[position[0]][position[1]] -= amount

    def new_pet(self, parent):
        self.pets.append(Pet(
                parent.posx,
                parent.posy,
                parent.reproduction,
                parent.defense * random.uniform(0.8, 1.2),
                parent.speed * random.uniform(0.8, 1.2),
                parent.attack * random.uniform(0.8, 1.2),
                parent.gather * random.uniform(0.8, 1.2)
            ))

    def ascii_map(self):
        res = ""
        for y in range(self.ysize):
            for x in range(self.xsize):
                pets_on_space = [p for p in self.pets if p.get_pos() == (x, y)]
                if pets_on_space != []:
                    res += str(len(pets_on_space))
                else:
                    res += " "

            res += "\n"
        return res

    def create_canvas(self):
        self.canvas = PyGameWorld(self)

    def update_canvas(self):
        self.canvas.draw(self)

    def handle_events(self):
        self.canvas.handle_events()

if __name__=="__main__":
    def shuffled_instructions():
        lst = list(INSTRUCTIONS)
        random.shuffle(lst)
        return lst

    pets = [Pet(x*3, x*3, shuffled_instructions(), 1, 1, 1, 1) for x in range(5)]
    w = World(20, 20, pets)
    
    w.create_canvas()

    while True:
        w.step()
        w.update_canvas()
        w.handle_events()
        sleep(0.1)

    print w.ascii_map()
