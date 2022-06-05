import random
from time import sleep

def generate_character():
    char_name = input("Character Name: ")
    char_strength = 20
    demons_killed = 0

    families = [
        "Kamado",
        "Himejima", 
        "Rengoku", 
        "Shinazugawa", 
        "Tokito", 
        "Tomioka", 
        "Agatsuma", 
        "Haganezuka", 
        "Hashibira", 
        "Iguro",
        "Kanroji",
        "Kocho", 
        "Ubuyashiki",
        "Uzui",
        "Tsugikuni",
    ]
    char_family = random.choice(families)
    print(f"{char_name} was born in the {char_family} family\n")

    breathings = [
        "Love",
        "Flame",
        "Sun",
        "Sound",
        "Thunder",
        "Wind",
        "Water",
        "Insect",
        "Serpent",
        "Moon",
        "Stone",
        "Mist",
        "Beast"
    ]
    
    has_breathing = random.choice([True, False])
    char_breathing = ""
    
    if has_breathing == True:
        char_breathing = random.choice(breathings)
        print(f"he was a {char_breathing} breathing user\n")
        match char_breathing:
            case "Sun":
                if char_family == ("Kamado" or "Tsugikuni"):
                    char_strength += 30
                else:
                    char_strength += 20
            case "Moon":
                if char_family == "Tsugikuni":
                    char_strength += 24
                else:
                    char_strength += 16
            case "Flame":
                if char_family == "Rengoku":
                    char_strength += 18
                else:
                    char_strength += 12
            case "Water":
                if char_family == "Tomioka":
                    char_strength += 18
                else:
                    char_strength += 12
            case "Thunder":
                if char_family == "Agatsuma":
                    char_strength += 18
                else:
                    char_strength += 12
            case "Wind":
                if char_family == "Shinazugawa":
                    char_strength += 18
                else:
                    char_strength += 12
            case "Stone":
                if char_family == "Himejima":
                    char_strength += 18
                else:
                    char_strength += 12
            case "Beast":
                if char_family == "Hashibira":
                    char_strength += 15
                else:
                    char_strength += 10
            case "Love":
                if char_family == "Kanroji":
                    char_strength += 15
                else:
                    char_strength += 10
            case "Mist":
                if char_family == "Tokito":
                    char_strength += 15
                else:
                    char_strength += 10
            case "Sound":
                if char_family == "Uzui":
                    char_strength += 15
                else:
                    char_strength += 10
            case "Serpent":
                if char_family == "Iguro":
                    char_strength += 15
                else:
                    char_strength += 10
            case "Insect":
                if char_family == "Kocho":
                    char_strength += 15
                else:
                    char_strength += 10   
    else: 
        char_strength += 5
        char_breathing = "None"
        print(f"he was a None breathing user but he was gifted with great strength\n")
    
    has_mark = random.choice([True, False])
    
    if has_mark:
        print("And he was born with the slayer mark on his head\n")
        
    can_use_hinokami_kagura = False

    if char_family.lower() == "kamado" and has_breathing and char_breathing != "Sun":
        can_use_hinokami_kagura = True
        print("He was able to use a move called the hinokami kagura or the dance of the fire god\n")

    sees_transparent_world = random.choice([True, False])
    
    if sees_transparent_world:
        print("he had the power to see living things in transparency\n")
        
    
    if has_breathing == True:
        has_total_concentration_breathing = random.choice([True, False])
    else:
        has_total_concentration_breathing = False

    if has_breathing:
        char_strength += 10
    if has_mark:
        char_strength += 40
    if sees_transparent_world:
        char_strength += 30
    if has_total_concentration_breathing:
        char_strength += 20
    if can_use_hinokami_kagura:
        char_strength += 30
    if char_family == "Tsugikuni":
        char_strength += 45
    if char_family == "Kamado":
        char_strength += 35
    
    print(f"{char_name} was sent to the demon slayer corps to train as a demon slayer because of his unique physical powers\n")
    
    met_temple_demon = False
    killed_temple_demon = False
    
    if char_strength >= 20:
        met_temple_demon = random.choice([True, False])
    
    if met_temple_demon:
        print(f"While training in the forest {char_name} encountered a demon eating a family in a temple\n")
        if char_strength >= 50:
            killed_temple_demon = True
        elif char_strength <= 25:
            killed_temple_demon = False
        elif (char_strength >= 25 and char_strength < 50):
            killed_temple_demon = random.choice([True, False])

        if killed_temple_demon:
            print(f"{char_name} slayed the demon but the family in the temple didn't survive so he buried them and prayed, then he went to continue his training\n")
            char_strength += 15
            demons_killed += 3
            print(f"Strength: {char_strength}\ndemons killed: {demons_killed}\n")
        else:
            print(f"{char_name} died struggling to kill the demon and was devoured\n")
            print(f"Strength: {char_strength}\ndemons killed: {demons_killed}\n")
            quit()
        
    if char_strength <= 20:
        demons_killed += random.randint(0, 21)
    if char_strength >= 40:
        demons_killed += random.randint(5, 40)
    if char_strength >= 60:
        demons_killed += random.randint(45, 60)
    if char_strength >= 80:
        demons_killed += random.randint(80, 120)
    if char_strength >= 100:
        demons_killed += random.randint(125, 160)
    if char_strength >= 120:
        demons_killed += random.randint(135, 180)
    if char_strength >= 170:
        demons_killed += random.randint(180, 240)
    if char_strength >= 200:
        demons_killed += random.randint(220, 280)
    if char_strength >= 250:
        demons_killed += random.randint(280, 340)
    
    char_strength += demons_killed / 10
    print(f"He finished his youth period, with total demon kills of {demons_killed} and his strength was {char_strength}\n")

    killed_swamp_demon = False
    
    if char_strength > 90:
        killed_swamp_demon = True
    elif char_strength < 60:
        killed_swamp_demon = False
    elif (char_strength > 60 and char_strength < 90):
            killed_swamp_demon = random.choice([True, False])
    if killed_swamp_demon:
        char_strength += 30
        demons_killed += 6
        
    lowermoons = [
        "Enmu",
        "Rokuro",
        "Wakuraba",
        "Mukago",
        "Rui",
        "Kamanue"
    ]
    
    lowermoon_name = ""
    lowermoon_number = 0
    met_a_lowermoon = False
    killed_lowermoon = False
    
    if demons_killed >= 40:
        met_a_lowermoon = random.choice([True, False])
        
    if met_a_lowermoon:
        lowermoon_number = random.randint(0, 5)
        lowermoon_name = lowermoons[lowermoon_number]
        
        if lowermoon_number == 0 and char_strength >= 140:
            killed_lowermoon = True
        elif lowermoon_number == 0 and char_strength <= 110:
            killed_lowermoon = False
        elif lowermoon_number == 0 and (char_strength >= 125 and char_strength < 140):
            killed_uppermoon = random.choice([True, False])
        
        if lowermoon_number == 1 and char_strength >= 130:
            killed_lowermoon = True
        elif lowermoon_number == 1 and (char_strength <= 100):
            killed_lowermoon = False
        elif lowermoon_number == 1 and (char_strength >= 115 and char_strength < 130):
            killed_lowermoon = random.choice([True, False])
        
        if lowermoon_number == 2 and char_strength >= 120:
            killed_lowermoon = True   
        elif lowermoon_number == 2 and (char_strength <= 90):
            killed_lowermoon = False
        elif lowermoon_number == 2 and (char_strength >= 105 and char_strength < 120):
            killed_lowermoon = random.choice([True, False])
        
        if lowermoon_number == 3 and char_strength >= 110:
            killed_lowermoon = True
        elif lowermoon_number == 3 and (char_strength <= 80):
            killed_lowermoon = False
        elif lowermoon_number == 3 and (char_strength >= 95 and char_strength < 110):
            killed_lowermoon = random.choice([True, False])
        
        if lowermoon_number == 4 and char_strength >= 100:
            killed_lowermoon = True
        elif lowermoon_number == 4 and (char_strength <= 70):
            killed_lowermoon = False
        elif lowermoon_number == 4 and (char_strength >= 85 and char_strength < 100):
            killed_lowermoon = random.choice([True, False])
        
        if lowermoon_number == 5 and char_strength >= 90:
            killed_lowermoon = True
        elif lowermoon_number == 5 and (char_strength <= 60):
            killed_lowermoon = False
        elif lowermoon_number == 5 and (char_strength >= 75 and char_strength < 90):
            killed_lowermoon = random.choice([True, False])
            
    if killed_lowermoon == True:
        match lowermoon_number:
            case 0:
                char_strength += 40
                demons_killed += 30
            case 1:
                char_strength += 35
                demons_killed += 25
            case 2:
                char_strength += 30
                demons_killed += 20
            case _:
                char_strength += 20
                demons_killed += 10
    
    has_red_blade = False
        
    if demons_killed >= 220:
        has_red_blade = True
    elif demons_killed >= 180 and demons_killed < 220:
        has_red_blade = random.choice([True, False])
    
    if has_red_blade == True:
        char_strength += 50
            
    uppermoons = [
        "Kokushibo",
        "Doma",
        "Akaza",
        "Nakime",
        "Gyokko",
        "Kaigaku"
    ]
            
    uppermoon_name = ""
    uppermoon_number = 0
    met_a_uppermoon = False
    killed_uppermoon = False
            
    if demons_killed >= 80 and killed_lowermoon != False:
        met_a_uppermoon = random.choice([True, False])
    
    if met_a_uppermoon:
        uppermoon_number = random.randint(0, 5)
        uppermoon_name = uppermoons[uppermoon_number]

        if uppermoon_number == 0 and char_strength >= 220:
            killed_uppermoon = True
        elif uppermoon_number == 0 and char_strength <= 180:
            killed_uppermoon = False
        elif uppermoon_number == 0 and (char_strength >= 190 and has_mark and has_total_concentration_breathing):
            killed_uppermoon = random.choice([True, False])
        elif uppermoon_number == 0 and (char_strength >= 200 and has_mark and has_total_concentration_breathing and can_use_hinokami_kagura):
            killed_uppermoon = True
        
        if uppermoon_number == 1 and char_strength >= 210:
            killed_uppermoon = True
        elif uppermoon_number == 1 and (char_strength <= 170):
            killed_uppermoon = False
        elif uppermoon_number == 1 and (char_strength >= 180 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = random.choice([True, False])
        elif uppermoon_number == 1 and (char_strength >= 190 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = True
        
        if uppermoon_number == 2 and char_strength >= 200:
            killed_uppermoon = True   
        elif uppermoon_number == 2 and (char_strength <= 160):
            killed_uppermoon = False
        elif uppermoon_number == 2 and (char_strength >= 170 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = random.choice([True, False])
        elif uppermoon_number == 2 and (char_strength >= 180 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = True
        
        if uppermoon_number == 3 and char_strength >= 190:
            killed_uppermoon = True
        elif uppermoon_number == 3 and (char_strength <= 150):
            killed_uppermoon = False
        elif uppermoon_number == 3 and (char_strength >= 160):
            killed_uppermoon = random.choice([True, False])
        elif uppermoon_number == 3 and (char_strength >= 170 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = True
        
        if uppermoon_number == 4 and char_strength >= 180:
            killed_uppermoon = True
        elif uppermoon_number == 4 and (char_strength <= 140):
            killed_uppermoon = False
        elif uppermoon_number == 4 and (char_strength >= 150):
            killed_uppermoon = random.choice([True, False])
        elif uppermoon_number == 4 and (char_strength >= 160 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = True
        
        if uppermoon_number == 5 and char_strength >= 160:
            killed_uppermoon = True
        elif uppermoon_number == 5 and (char_strength <= 120):
            killed_uppermoon = False
        elif uppermoon_number == 5 and (char_strength >= 130):
            killed_uppermoon = random.choice([True, False])
        elif uppermoon_number == 5 and (char_strength >= 140 and (has_mark or has_total_concentration_breathing)):
            killed_uppermoon = True
            
    if killed_uppermoon == True:
        match uppermoon_number:
            case 0:
                char_strength += 70
                demons_killed += 80
            case 1:
                char_strength += 65
                demons_killed += 70
            case 2:
                char_strength += 60
                demons_killed += 60
            case _:
                char_strength += 50
                demons_killed += 40
        
    met_muzan = False
    killed_muzan = False
    
    if char_strength >= 200:
        met_muzan = random.choice([True, False])
        
    if met_muzan:
        if char_strength >= 320 and char_breathing == "Sun":
            killed_muzan = True
        elif char_strength <= 280 and char_breathing == "Sun" and has_mark and has_total_concentration_breathing and sees_transparent_world and has_red_blade == True:
            killed_uppermoon = random.choice([True, False])
        else:
            killed_muzan = False
            
        if killed_muzan:
            char_strength += 250
    
    print(f"{char_name} was sent on his first mission as an official demon slayer\n")
    
    print("he was sent to investigate about a demon who kidnaps young girls in a village not so far away\n")
    print(f"after investigating {char_name} found the demon he was a strong demon stronger than all the demons he fought before,\nit possessed a blood demon art that can make the demon split into three and the demon can use swamp portals\n")
    if killed_swamp_demon:
        print(f"{char_name} was able to kill the swamp demon after a hard fight he unfortunately was injured and found out the demon killed a lot of innocent girls\nafter this fight {char_name} grew more hatred toward demons\n")
    else:
        print(f"unfortunately {char_name} was killed fighting the demon, the swamp demon continued killing innocent girls.\n")
    
    if has_red_blade:
        print(f"he activated his red blade with {demons_killed} demon kills\n")
    
    if met_a_lowermoon:
        print(f"he met lowermoon {lowermoon_number + 1} {lowermoon_name}\n")
        if killed_lowermoon:
            print(f"and he defeated the lowermoon {lowermoon_number + 1}\n")
        elif not killed_lowermoon:
            print(f"and he was defeated and devoured by lowermoon {lowermoon_number + 1}\n")
    
    if met_a_uppermoon:
        print(f"he met uppermoon {uppermoon_number + 1} {uppermoon_name}\n")
        if killed_uppermoon:
            print(f"and he defeated the uppermoon {uppermoon_number + 1}\n")
        elif not killed_uppermoon:
            print(f"and he was defeated and devoured by uppermoon {uppermoon_number + 1}\n")
    
    if met_muzan:
        print(f"{char_name} encountered muzan in one of his travels, it was like a nightmare seeing the man who causes all the evil in the world.\n")
        if killed_muzan:
            print(f"{char_name} fought muzan with a fearless spirit and was able to cut some of his limbs, until muzan hit him with a powerful blow,\n{char_name} was able to land a big hit on muzan using the sun breathing technique and muzan couldn't regenerate and he put muzan's limbs in a box and waited for sunrise\nand the man who caused the evil was defeated\nand all the demons were turned into dust.\n")
            print(f"{char_name} got back to the slayer corps to deliver the good news and everyone met him was a cheerful spirit and he was nicknamed the god slayer\n")
            print(f"he then lived a happy life with no worries of muzan and his demons and married a girl who he loved and died happily in his 80s\n")
        elif not killed_muzan:
            print(f"he tried to fight muzan with all the power he had but failed and was brutally killed by muzan.\neveryone was scared because how can a man powerful as {char_name} can die with just one blow from muzan\n ")

    print(char_strength)


generate_character()