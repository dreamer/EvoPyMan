from random import Random, randint, random

Direction = {
    "north" : 0,
    0 : "north",
    "south" : 1,
    1 : "south",
    "east"  : 2,
    2 : "east",
    "west"  : 3,
    3 : "west"
    }
    
Element = {
    "Ghost" : 0,
    0 : "Ghost",
    "SmallDot" : 1,
    1 : "SmallDot",
    "BigDot" : 2,
    2 : "BigDot"
    }

Mode = { "MeEat" : 0,
    0 : "MeEat",
    "IamEating" : 1,
    1 : "IamEating"
    }
    
def dictionaryLen(dict):
    return len(dict) / 2

# tworzy siê po prostu losowy obiekt, innych nam chyba nie bêdzie potrzeba
class Instruction:
    def __init__(self):
        self.randomValue()
    def randomValue(self):
        # rodzaj obiektu ktorego dotyczy instrukcja
        self.element = Element[randint(0,dictionaryLen(Element) - 1)]

        # kierunek w strone obiektu (nie umiem tego zdania ladniej napisac)
        self.dirItIs = Direction[randint(0,dictionaryLen(Direction) - 1)]

        # kierunek w ktorym by bedziemy szli
        self.dirToGo = Direction[randint(0,dictionaryLen(Direction) - 1)]

        # czy my jemy czy nas jedza
        self.mode = Mode[randint(0,dictionaryLen(Mode) - 1)]

        # przedzial odleglosci od obiektu (start i end
        self.range = [randint(1, 10), randint(1, 10)]
        self.range.sort()
    def __repr__(self):
        return "%s : %s - %s : %s - %s : %s - %s : %s - %s" % (
            self.dirItIs, Direction[self.dirItIs],
            self.dirToGo, Direction[self.dirToGo],
            self.mode, Mode[self.mode],
            self.element, Element[self.element],
            self.range
            )

def main():
    pass

__all__ = ["Instruction", "Direction", "Mode", "Element"]
if __name__ == '__main__':
    main()