import random

LINE = "--------------------------------------------------------------"
INFO1 = "This program includes a customized liftoff for the people who's eager to learn rocket science all around the world."
INFO2 = "There are two main categories of rocket engines: \nLiquid rockets \nSolid rockets \nIn a liquid rocket, the propellants, the fuel and the oxidizer, are stored separately as liquids and are pumped into the \ncombustion chamber of the nozzle where burning occurs. \nIn a solid rocket, the propellants are mixed together and packed into a solid cylinder. \nUnder normal temperature conditions, the propellants do not burn; \nbut they will burn when exposed to a source of heat provided by an igniter. \nOnce the burning starts, it proceeds until all the propellant is exhausted. \nWith a liquid rocket, you can stop the thrust by turning off the flow of propellants. \nWith a solid rocket, you have to destroy the casing to stop the engine."
LIQUID_BIPROPELLANTS = random.uniform(2.9, 4.5)*1000
SOLID_PROPELLANTS = random.uniform(2.1, 3.2)*1000

EARTH = 9.80
MARS = 3.71
JUPYTER = 24.79
SATURN = 10.44
VENUS = 8.87
URANUS = 8.87
NEPTUNE = 11.15
MERCURY = 3.7

def away_from_earth(planet):
    earth_to_sun = 94383352
    if planet == 'Mars':
        distance = 154791257 - earth_to_sun
    if planet == 'Jupyter':
        distance = 460773026 - earth_to_sun
    if planet == 'Saturn':
        distance = 910374075 - earth_to_sun
    if planet == 'Venus':
        distance = earth_to_sun - 67230145 
    if planet == 'Uranus':
        distance = 1907317044 - earth_to_sun
    if planet == 'Neptune':
        distance = 2780191005 - earth_to_sun
    if planet == 'Mercury':
        distance = earth_to_sun - 34236781
        
    return distance


def read_from_txt(txt):
    if txt == 'serial':
        f = open('rocket2.txt')
    if txt == 'parallel':
        f = open('rocket1.txt')
    if txt == 'A':
        f = open('astronaut.txt')
    if txt == 'S':
        f = open('satellite.txt')
    if txt == 'N':
        f = open('neighbour.txt')
    if txt == 'W':
        f = open('wormhole.txt')
    if txt == 'P':
        f = open('planets.txt')
    
    for line in f:
        line = line.strip() 
        if line != "":
            print(line)

def countdown(situation):
    if situation == 1:
        cnt = int(input("Launch starts in (hint: type 10) ... "))
        if cnt == 10:
            cnt = int(input("in ... "))
            if cnt == 9:
                cnt = int(input("in ... "))
                if cnt == 8:
                    cnt = int(input("in ... "))
                    if cnt == 7:
                        cnt = int(input("in ... "))
                        if cnt == 6:
                            cnt = int(input("in ... "))
                            if cnt == 5:
                                cnt = int(input("in ... "))
                                if cnt == 4:
                                    cnt = int(input("in ... "))
                                    if cnt == 3:
                                        cnt = int(input("in ... "))
                                        if cnt == 2:
                                            cnt = int(input("in ... "))
                                            if cnt == 1:
                                                print("Launch successfull")
        else:
            print("Launch failed. Countdown repeated")
            countdown()
            
    if situation == 2:
        print("1...")
        time.sleep(3)
        print("2...")
        time.sleep(3)
        print("2...")
        time.sleep(3)
        print("LAUNCH!!!!")
        time.sleep(3)
            
def acceleration(exhaust, mass, planet):
    mass * 1000000
    fuel = 1.40 * 10000
    
    if planet == 'Mars':
        acceleration = ((exhaust/mass) * fuel) - MARS
    if planet == 'Jupyter':
        acceleration = ((exhaust/mass) * fuel) - JUPYTER
    if planet == 'Saturn':
        acceleration = ((exhaust/mass) * fuel) - SATURN
    if planet == 'Venus':
        acceleration = ((exhaust/mass) * fuel) - VENUS
    if planet == 'Uranus':
        acceleration = ((exhaust/mass) * fuel) - URANUS
    if planet == 'Neptune':
        acceleration = ((exhaust/mass) * fuel) - NEPTUNE
    if planet == 'Mercury':
        acceleration = ((exhaust/mass) * fuel) - MERCURY
    return acceleration

def main():
    while True:
        exp = input("Please expand your terminal. Did you expand it? (Y/N) : ")
        if exp == 'Y':
            print(LINE)
            print("Welcome to the liftoff of Kara Solo!")
            decision = input("Would you like to register for the liftoff? (Y/N) : ")
        
            if decision == 'Y':
                print(LINE)
                print(INFO1)
                print(LINE)
                time.sleep(2)
                called = input("You will be chraged from this liftoff. What should we call you? : ")
                print(LINE)
                print("There are four major components to any full scale rocket: \nThe Structural System, or Frame \nThe Payload System \nThe Guidance System \nPropulsion System")
                time.sleep(3)
                print(LINE)
                print("Start with the Structural System. \nThe structural system of a rocket includes all of the parts which make up the frame of the rocket; \nthe cylindrical body, the fairings, and any control fins.")
                time.sleep(3)
                print(LINE)
                mass = float(input("First you have to select mass of your rocket (value must be as 1.80 or 3.21 etc.) : "))
                print(LINE)
                time.sleep(3)
                selection = input("Weight of a rocket is highly important. \nTo reduce your weight during liftoff which Structural System do you prefer? \nParallel or Serial? (P/S) : ")
                print(LINE)
                if selection == 'P':
                    print(f"{called}, Structural System of your rocket is being prepared by engineers and technicians. Take a look: ")
                    print(LINE)
                    time.sleep(3)
                    read_from_txt('parallel')
                if selection == 'S':
                    print(f"{called}, Structural System of your rocket is being prepared by engineers and technicians. Take a look: ")
                    print(LINE)
                    time.sleep(3)
                    read_from_txt('serial')
                print(LINE)
                time.sleep(3)
                print("It seems perfect. It is time for the Payload System. The payload of a rocket depends on the rocket's mission.")
                payload = input(f"{called}, please determine for the Payload System. Astronaut or Satellite? (A/S) : ")
                print(LINE)
                if payload == 'A':
                    ast = input("Announce your brave astronaut's name: ")
                    print(f" Now {ast} is training for a very honorable journey")
                    time.sleep(3)
                    read_from_txt('A')
                if payload == 'S':
                    sat = input("Name your satellite: ")
                    print(f"Now {sat} is preaparing for a very honorable journey")
                    time.sleep(3)
                    read_from_txt('S')
                print(LINE)
                time.sleep(3)
                print("Two major components left. The guidance system of a rocket includes very sophisticated sensors, on-board computers, radars, and communication equipment.")
                time.sleep(3)
                print("Kara Solo's qualified employees figured out the guidance system of your rocket. We're on last stage!")
                print(LINE)
                time.sleep(3)
                print("The propulsion of a rocket includes all of the parts which make up the rocket engine; the tanks pumps, propellants, power head, and rocket nozzle . \nThe function of the propulsion system is to produce thrust.")
                time.sleep(4)
                print(LINE)
                pirnt("For that you have to select an engine type for your rocket.")
                time.sleep(4)
                engine = input(f"{INFO2}. \nMake your choice (L/S) : ")
                print(LINE)
                print(f"{called}, your rocket and all the major systems are ready to liftoff.")
                if payload == 'A':
                    planet = input("Before liftoff please determine your route. Select a planet: \nMars \nJupyter \nSaturn \nVenus \nUranus \nNeptune \nMercury \nRemember an astronaout can only visit the Mars and the Venus. \nSelection (Mars/Jupyter/Saturn/Venus/Uranus/Neptune/Mercury) : ")
                if payload == 'S':
                    planet = input("Before liftoff please determine your route. Select a planet: \nMars \nJupyter \nSaturn \nVenus \nUranus \nNeptune \nMercury \nSelection (Mars/Jupyter/Saturn/Venus/Uranus/Neptune/Mercury) : ")
                print(LINE)
                distance = away_from_earth(planet)
                print(f"{planet} is {distance} km away from the earth. Get ready for liftoff.")
                print("Countdown from 10 - 0 is starting")
                countdown(1)
                print(LINE)
                if payload == 'A':
                    print(f"Now your astronaut {ast} is exploring the mysteries of outer space. Everything seems right. \nJourney to the {planet} has started.")
                    time.sleep(3)
                    read_from_txt('P')
                    print(LINE)
                    for i in range (3):
                        print(f"Arriving to the {planet} ...")
                        time.sleep(3)
                        i += 1
                    print(LINE)
                    butterfly_effect_ast = input("Your astronaut is about the reach to the destination point. But something yet blue and mysterious appeared. Would you like to observe? (Y/N) : ")
                    if butterfly_effect_ast == 'Y':
                        print(LINE)
                        time.sleep(5)
                        print("This mysterirous thing is a WORMHOLE!")
                        read_from_txt('W')
                        print(f"Now {ast} is more closer to the {planet} more than ever.")
                        print(LINE)
                        print("We're checking our last controls before arriving near the planet.")
                        print(f"Everything confirmed about {ast}'s destianation and situation.")
                        time.sleep(2)
                        wonder = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. {ast} is exploring around {planet}. Ready for a launch? (Y/N) : ")
                        if wonder == 'Y':
                            print(LINE)
                            time.sleep(2)
                            print(f"Explorations and time will tell more about this planet but something approaching to {ast}.")
                            time.sleep(2)
                            print("THIS")
                            time.sleep(2)
                            print("IS")
                            time.sleep(2)
                            print("OUR")
                            time.sleep(2)
                            print("NEW")
                            time.sleep(2)
                            print("NEIGHBOUR!!!")
                            time.sleep(3)
                            read_from_txt('N')
                            print(LINE)
                            time.sleep(3)
                            print(f"{ast} is ready for a very quick liftoff. Everthing is checked.")
                            countdown(2)
                            time.sleep(3)
                            print(f"Hopefully {ast} discovered the wormhole. Now returning to the Earth begins...")
                            time.sleep(6)
                            print(f"{ast} arrived to the Earth successfully!")
                            print(LINE)
                            time.sleep(3)
                            new = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. Are you ready for a new one? (Y/N) : ")
                            if new == 'Y':
                                continue
                            else:
                                time.sleep(2)
                                print(LINE)
                                print("Thanks for your participation about learning a new subject such as rocket science. I hope you enjoyed from the game.")
                                break
                        if wonder == 'N':
                            print(f"Base Control: Confirmed {ast}. After your last checks you can return to the Earth.")
                            print(f"Hopefully {ast} discovered the wormhole. Now returning to the Earth begins...")
                            time.sleep(6)
                            print(f"{ast} arrived to the Earth successfully!")
                            print(LINE)
                            time.sleep(3)
                            new = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. Are you ready for a new one? (Y/N) : ")
                            if new == 'Y':
                                continue
                            else:
                                time.sleep(2)
                                print(LINE)
                                print("Thanks for your participation about learning a new subject such as rocket science. I hope you enjoyed from the game.")
                                break
                    else:
                        print("Base Control: You've missed a WORMHOLE. Now we have to continue to our journey from the long way.")
                        for i in range (3):
                            print(f"Arriving to the {planet} ...")
                            time.sleep(3)
                            i += 1
                        print("We're checking our last controls before arriving near the planet.")
                        print(f"Everything confirmed about {ast}'s destianation and situation.")
                        time.sleep(2)
                        wonder = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. {ast} is exploring around {planet}. Ready for a launch? (Y/N) : ")
                        if wonder == 'Y':
                            print(LINE)
                            time.sleep(2)
                            print(f"Explorations and time will tell more about this planet but something approaching to {ast}.")
                            time.sleep(2)
                            print("THIS")
                            time.sleep(2)
                            print("IS")
                            time.sleep(2)
                            print("OUR")
                            time.sleep(2)
                            print("NEW")
                            time.sleep(2)
                            print("NEIGHBOUR!!!")
                            time.sleep(3)
                            read_from_txt('N')
                            print(LINE)
                            if distance > 400171:
                                print("Base control: We need your acceleration for this liftoff.")
                                if engine == 'L':
                                    time.sleep(3)
                                    print("Thrust stopped by turning off the flow of propellants")
                                    time.sleep(3)
                                    print(f"{ast}: Base Control I have an emergency in here. Roger")
                                    time.sleep(3)
                                    print(f"Base Control: Understood {ast}. Your acceleration is being calculated")
                                    acl = acceleration(LIQUID_BIPROPELLANTS, mass, planet)
                                    print(f"Base Control: Acceleration confirmed as {acl} m/s. Ready to liftoff.")
                                    countdown(2)
                                    time.sleep(3)
                                if engine == 'S':
                                    time.sleep(3)
                                    print("Casing destroyed to stop the engine")
                                    time.sleep(3)
                                    print(f"{ast}: Base Control I have an emergency in here. Roger")
                                    time.sleep(3)
                                    print(f"Base Control: Understood {ast}. Your acceleration is being calculated")
                                    acl = acceleration(SOLID_PROPELLANTS, mass, planet)
                                    print(f"Base Control: Acceleration confirmed as {acl} m/s. Ready to liftoff.")
                                    countdown(2)
                                    time.sleep(3)
                            else:
                                time.sleep(3)
                                print(f"{ast} is ready for a very quick liftoff. Everthing is checked.")
                                countdown(2)
                                time.sleep(3)
                        else:
                            time.sleep(3)
                            if distance > 400171:
                                print("Base control: We need your acceleration for this liftoff.")
                                if engine == 'L':
                                    time.sleep(3)
                                    print(f"Base Control: Understood {ast}. Your acceleration is being calculated")
                                    acl = acceleration(LIQUID_BIPROPELLANTS, mass, planet)
                                    print(f"Base Control: Acceleration confirmed as {acl} m/s. Ready to liftoff.")
                                    countdown(2)
                                if engine == 'S':
                                    time.sleep(3)
                                    print(f"Base Control: Understood {ast}. Your acceleration is being calculated")
                                    acl = acceleration(SOLID_PROPELLANTS, mass, planet)
                                    print(f"Base Control: Acceleration confirmed as {acl} m/s.")
                                    countdown(2)
                        time.sleep(6)
                        print(f"{ast} arrived to the Earth successfully!")
                        print(LINE)
                        time.sleep(3)
                        new = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. Are you ready for a new one? (Y/N) : ")
                        if new == 'Y':
                            continue
                        else:
                            time.sleep(2)
                            print("Thanks for your participation about learning a new subject such as rocket science. I hope you enjoyed from the game.")
                            break
                            
                if payload == 'S':
                    print(f"Now your satellite {sat} is exploring the mysteries of outer space. Everything seems right and stage confirmed. \nJourney to the {planet} has initialized.")
                    time.sleep(3)
                    read_from_txt('P')
                    print(LINE)
                    for i in range (3):
                        print(f"Arriving to the {planet} ...")
                        time.sleep(3)
                        i += 1
                    print(LINE)
                    butterfly_effect_sat = input("Your satellite is about the reach to the destination point. But something yet blue and mysterious appeared. Would you like to observe? (Y/N) : ")
                    if butterfly_effect_sat == 'Y':
                        print(LINE)
                        time.sleep(5)
                        print("This mysterirous thing is a WORMHOLE!")
                        read_from_txt('W')
                        print(f"Now {sat} is more closer to the {planet} more than ever.")
                        print(LINE)
                        print("We're checking our last controls before arriving near the planet.")
                        print(f"Everything confirmed about {sat}'s destianation and situation.")
                        time.sleep(6)
                        new = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. Are you ready for a new one? (Y/N) : ")
                        if new == 'Y':
                            continue
                        else:
                            time.sleep(2)
                            print("Thanks for your participation about learning a new subject such as rocket science. I hope you enjoyed from the game.")
                            break
                    else:
                        print("You've missed a WORMHOLE. Now we have to continue to our journey from the long way.")
                        for i in range (3):
                            print(f"Arriving to the {planet} ...")
                            time.sleep(3)
                            i += 1
                        print("We're checking our last controls before arriving near the planet.")
                        print(f"Everything confirmed about {sat}'s destianation and situation.")
                        time.sleep(6)
                        new = input(f"CONGURATULATIONS {called}! Your very first liftoff is successfull. Are you ready for a new one? (Y/N) : ")
                        if new == 'Y':
                            continue
                        else:
                            time.sleep(2)
                            print("Thanks for your participation about learning a new subject such as rocket science. I hope you enjoyed from the game.")
                            break

            if decision == 'N':
                print(LINE)
                print("It does not matter how slowly you go as long as you do not stop. ~Confucius")
                break
            
        if exp == 'N':
            print(LINE)
            sure = input("Still want to continue? (Y/N) : ")
            if sure == 'Y':
                exp = 'Y'
            else:
                print(LINE)
                print("We know what we are, but know not what we may be. ~Shakespeare")
                break

if __name__ == "__main__":
    main()
