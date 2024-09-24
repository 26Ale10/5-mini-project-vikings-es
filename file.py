
# Crea un juego utilizando las clases que definiste. Para esto, necesitarás:
# - Crear un nuevo `file.py`
# - Importar las clases que definiste anteriormente
# - Definir funciones para crear el flujo de trabajo del juego:
# por ejemplo, funciones para crear equipos (quizás puedas crear equipos aleatorios con los nombres de tus compañeros de clase), ejecutar el juego, etc.

import random
from vikingsClasses import Viking, Saxon, War

soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

def createGameWithNames():
    war = War()

    for i in range(random.randint(10, 100)):
        viking = Viking(random.choice(soldier_names), random.randint(50, 100), random.randint(5, 15))
        war.addViking(viking)

        saxon = Saxon(random.randint(50, 100), random.randint(5, 15))
        war.addSaxon(saxon)

    return war

def runGame():
    war = createGameWithNames()

    round = 0


    while "are still in the thick of battle." in war.showStatus():
        war.vikingAttack()
        war.saxonAttack()
        print(f"round: {round} // Viking army: {len(war.vikingArmy)} warriors",f"and Saxon army: {len(war.saxonArmy)} warriors")
        print(war.showStatus())
        round += 1

runGame()