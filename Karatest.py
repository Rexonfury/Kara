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
for x in range(5):
    if not kara.treeFront():
        kara.move()
    else:
        kara.removeLeaf()
        kara.turnLeft()
        kara.move()
        kara.turnRight()
    