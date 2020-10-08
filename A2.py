# BEFEHLE:  kara.
#   move()  turnRight()  turnLeft()
#   putLeaf()  removeLeaf()
#
# SENSOREN: kara.
#   treeFront()  treeLeft()  treeRight()
#   mushroomFront()  onLeaf()
#

# hier können Sie eigene Methoden definieren

# hier kommt das Hauptprogramm hin, zB:
while not kara.treeFront():
    kara.removeLeaf()
    kara.move()
    if kara.treeFront():
        kara.turnLeft()
    if not kara.treeLeft():
        kara.turnRight()
        kara.move()
        kara.turnLeft()
        