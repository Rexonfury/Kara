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
for x in range(3):
    while not kara.mushroomFront():
        kara.move()

    if kara.mushroomFront():
        kara.turnLeft()
        kara.move()
        kara.turnRight()
        kara.move()
        kara.move()
        kara.turnRight()
        kara.move()
        kara.turnLeft()
    
    
    
        