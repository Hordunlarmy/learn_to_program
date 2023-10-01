import random
import math


class warrior:
    def __init__(self, name="Warrior", health=0, attMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attMax = attMax
        self.blkkMax = blockMax

    def attack(self):
        return (self.attMax * (random.random() + .5))

    def block(self):
        return (self.blkMax * (random.random() + .5))


class Battle:
    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "GAME OVER":
                print("GAME OVER")
                break

            if self.getAttackResult(warrior2, warrior1) == "GAME OVER":
                print("GAME OVER")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlkAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - w)
