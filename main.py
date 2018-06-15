import math
import operator
from random import randint
from time import sleep
import re
import pygame
import pyscroll
import pytmx
import inputbox
import programHelper
from astar import AStar
from pygame.locals import *
from pytmx.util_pygame import load_pygame

FPS = 60
MOVEMENT_DELAY = 0.2
MAP_FILE = 'map.tmx'
PLAYER_IMAGE = 'player.png'


# simple wrapper to keep the screen resizeable
def init_screen(width, height):
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen

class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()

        # private variables
        self._position = [0, 0]

    @property
    def position(self):
        return tuple(self._position)

    def getx(self):
        return int(self.rect.x / 16)

    def gety(self):
        return (self.rect.y / 16)

    def printposition(self):
        print(str(self.rect.x) + "   " + str(self.rect.y))

    @position.setter
    def position(self, value):
        self._position = list(value)
        self.rect.topleft = self._position

    def positionchange(self, x, y):
        self._position += [x, y]

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Pathfinder(AStar):
    def __init__(self, mesh):
        self.width = mesh.width
        self.height = mesh.height

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'direct' distance between two (x,y) tuples"""
        (x1, y1) = n1
        (x2, y2) = n2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance_between(self, n1, n2):
        """this method always returns 1, as two 'neighbors' are always adjacent"""
        return 1

    def neighbors(self, node):
        """for a given coordinate on the mesh, returns up to 8 adjacent nodes that can be reached (=any adjacent coordinate that is walkable)"""
        x, y = node
        for i, j in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            x1 = x + i
            y1 = y + j
            if x1 > 0 and y1 > 0 and x1 < self.width and y1 < self.height and game.layer.data[y1][x1] == 0:
                yield (x1, y1)

class RandomGame(object):
    def __init__(self, mapfile):
        self._move_queue = []
        self.running = False
        self.last_position_update = 0
        map = load_pygame(mapfile)
        self.mapp = load_pygame(mapfile)
        self.objectlist = list(self.mapp.get_tile_locations_by_gid(20))
        self.objectlist2 = list(self.mapp.get_tile_locations_by_gid(20))
        self.moveCounter = 0
        self.layer = map.layers[1]
        self.objectlayer = map.layers[3]
        self.charizardLayer = map.layers[4]
        self.blastoiseLayer = map.layers[5]
        self.ironLayer = map.layers[6]
        self.venusaurLayer = map.layers[7]
        self.snorlaxLayer = map.layers[8]
        self.blastoiseLayer.visible = 0
        self.ironLayer.visible = 0
        self.venusaurLayer.visible = 0
        self.snorlaxLayer.visible = 0
        self.objectType = ["pokemon", "item"]
        self.rarity = [1, 2, 3, 4, 5, 6, 8]
        self.type = ["fire", "grass", "water", "normal"]
        self.itemType = ["heal", "upgrade"]
        self.catchableOrShiny = ["y", "n"]
        self.itemUseless = [0]
        self.apdp = [10, 15, 20, 25, 30, 35, 40, 50]
        self.hpOfPokemonAndPlayer = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.pokemonCounter = 0
        self.itemCounter = 0
        self.moveHelper = self.objectlist[0]
        self.moveCounter2 = 0
        self.itemActive = 0
        self.screenHelper = 1
        self.hpPlayer = 100



        map_data = pyscroll.data.TiledMapData(map)

        w, h = screen.get_size()

        self.map_layer = pyscroll.BufferedRenderer(map_data, screen.get_size(), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=4)
        self.map_layer.zoom = 1.5
        self.player = Player(PLAYER_IMAGE)
        self.player.position = self.map_layer.map_rect.center
        self.group.add(self.player)
        self.mesh = Pathfinder(map)

    def draw(self, surface):
        self.group.center(self.player.rect.center)

        self.group.draw(surface)

    # def generatePokemon(self):
    #     file = open('Pokemon1.csv', 'w')
    #     file.write("pokemon,")
    #     file.write(str(self.rarity[randint(0, 6)]) + ",")
    #     file.write(str(self.type[randint(0, 3)]) + ",")
    #     file.write(str(self.catchableOrShiny[randint(0, 1)]) + ",")
    #     file.write(str(self.apdp[randint(0, 7)]) + ",")
    #     file.write(str(self.apdp[randint(0, 7)]) + ",")
    #     file.write(str(self.hpOfPokemonAndPlayer[randint(0, 9)]) + ",")
    #     file.write(str(self.hpOfPokemonAndPlayer[randint(0, 9)]) + ",")
    #     file.write(str(self.catchableOrShiny[randint(0, 1)]))
    #     file.close()

    def generatePokemon(self):
        file = open('Pokemon1.csv', 'w')
        file.write("pokemon,")
        rarity = self.rarity[randint(0, 6)]
        if (rarity < 7):
            file.write("<7,")
        else:
            file.write(">7,")
        type = self.type[randint(0, 3)]
        if (type == "normal"):
            file.write("normal,")
        else:
            file.write("other,")
        file.write(str(self.catchableOrShiny[randint(0, 1)]) + ",")
        ap = self.apdp[randint(0, 7)]
        if (ap < 30):
            file.write("<30,")
        else:
            file.write(">30,")
        dp = self.apdp[randint(0, 7)]
        if (dp < 30):
            file.write("<30,")
        else:
            file.write(">30,")
        hpPokemon = self.hpOfPokemonAndPlayer[randint(0, 9)]
        if (hpPokemon < 50):
            file.write("<50,")
        else:
            file.write(">50,")
        if (self.hpPlayer < 60):
            file.write("<60,")
        else:
            file.write(">60,")
        file.write(str(self.catchableOrShiny[randint(0, 1)]))
        file.close()

    def generateItem(self):
        file = open('Pokemon1.csv', 'w')
        file.write("item,")
        file.write(str(self.rarity[randint(0, 1)]) + ",")
        file.write(str(self.itemType[randint(0, 1)]) + ",")
        file.write(str(self.catchableOrShiny[0]) + ",")
        file.write(str(self.itemUseless[0]) + ",")
        file.write(str(self.itemUseless[0]) + ",")
        file.write(str(self.itemUseless[0]) + ",")
        if (self.hpPlayer < 60):
            file.write("<60,")
        else:
            file.write(">60,")
        file.write(str(self.catchableOrShiny[1]) + ",")
        file.close()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    pygame.exit()
                    break

                if event.key == K_SPACE:
                    tile_position = tuple(map(operator.floordiv, self.player.position, self.map_layer.data.tile_size))
                    print(self.objectlist[0][0], self.objectlist[0][1], self.objectlist[0][2])
                    self._move_queue = self.mesh.astar(tile_position, (self.objectlist[0][0], self.objectlist[0][1]))
                    self.moveHelper = self.objectlist[0]
                    self.moveCounter += 1
                    del self.objectlist[0]

                if event.key == K_x and self.moveHelper == self.objectlist2[self.moveCounter - 1] and self.moveCounter != self.moveCounter2:
                    screen = init_screen(800 + self.screenHelper, 600 + self.screenHelper)
                    self.moveCounter2 += 1
                    if (self.ironLayer.visible == 1):
                        self.generateItem()
                        self.itemActive = 1
                    else:
                        self.generatePokemon()
                    myResult = programHelper.id3()
                    while (myResult != "y" or myResult != "n"):
                        self.generatePokemon()
                        # myResult = program.id3()
                        if (myResult == "y" and self.itemActive == 1):
                            self.itemCounter += 1
                            print(str("Actual item number: %s" % self.itemCounter))
                        if (myResult == "y" and self.itemActive == 0):
                            self.pokemonCounter += 1
                            print(str("Actual pokemon number: %s" % self.pokemonCounter))
                            break
                        else:
                            if (self.itemActive == 0):
                                print(str("Pokemon fight starts!"))
                                self.hpPlayer -= 10
                                print(str("Actual hp of player: %s" % self.hpPlayer))
                            break
                    screen = init_screen(800, 600)
                    self.itemActive = 0
                    self.i = 0
                    if self.charizardLayer.visible == 1:
                        self.charizardLayer.visible = 0
                        self.blastoiseLayer.visible = 1
                        return
                    # self.charizardLayer = map.layers[self.i]
                    if self.blastoiseLayer.visible == 1:
                        self.blastoiseLayer.visible = 0
                        self.ironLayer.visible = 1
                        return
                        # self.charizardLayer = map.layers[self.i]
                    if self.ironLayer.visible == 1:
                        self.ironLayer.visible = 0
                        self.venusaurLayer.visible = 1
                        return
                    if self.venusaurLayer.visible == 1:
                        self.venusaurLayer.visible = 0
                        self.snorlaxLayer.visible = 1
                        return
                    if self.snorlaxLayer.visible == 1:
                        self.snorlaxLayer.visible = 0
                        return

                    
                    #print(self.mapp.tiledgidmap)
                '''    objectlist = self.mapp.get_tile_locations_by_gid(20)
                    for x in objectlist:
                        if self._move_queue == []:
                            tile_position = tuple(map(operator.floordiv, self.player.position, self.map_layer.data.tile_size))
                            print(tile_position)
                            #print(x[0], x[1], x[2])
                            self._move_queue += self.mesh.astar(tile_position, (x[0], x[1]))
                    
                    command = inputbox.ask(screen, "")
                    
                    cords = command.split("-")
                    if self.layer.data[int(cords[1])][int(cords[0])] == 0:
                        sleep(1)
                        self._move_queue = self.mesh.astar(tile_position, (int(cords[0]), int(cords[1])))
                    else:
                        inputbox.display_box(screen, "W podanym miejscu znajduje się przeszkoda")
                        sleep(2)
'''
            elif event.type == VIDEORESIZE:
                init_screen(event.w, event.h)
                self.map_layer.set_size((event.w / 2, event.h / 2))

    def update(self, dt):
        """ Tasks that occur over time should be handled here"""
        if self.last_position_update >= MOVEMENT_DELAY:
            if self._move_queue != []:
                self.player.position = list(map(operator.mul, self._move_queue[0], self.map_layer.data.tile_size))
                del self._move_queue[0]
            self.last_position_update = 0

    def run(self):
        """ Run the game loop"""
        clock = pygame.time.Clock()
        self.running = True

        try:
            while self.running:
                dt = clock.tick(FPS) / 1000.
                self.last_position_update += dt
                self.handle_input()
                self.update(dt)
                self.draw(screen)
                pygame.display.flip()

        except KeyboardInterrupt:
            self.running = False
            pygame.exit()

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screen = init_screen(800, 600)
    pygame.display.set_caption('Pokemon')

    try:
        game = RandomGame(MAP_FILE)
        game.run()
    except:
        pygame.quit()
        raise
