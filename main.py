import requests, json, humanize, os, itertools, time

URL = 'https://api.wynncraft.com/v3/item/database?fullResult'
DATA = json.loads(open("./json/items.json", "r", encoding="utf+8").read())

def main():
    print(" >>> Main Function")
    inputs()

def inputs():
    print(" >>> Settings")
    # lvlMin = int(input(" > Lvl Min:  "))
    # lvlMax = int(input(" > Lvl Max:  "))
    # weapon = input(" > Weapon:   ")
    # elemnt = input(" > Element:  ")
    # itemFinder(lvlMin, lvlMax, weapon, elemnt)
    item_search(97, 97, "wand", "water")

def item_search(lvlMin, lvlMax, weaponArg, element):
    print(" >>> Item Search")
    itemDict = {"helmet": [], "chestplate": [], "leggings": [], "boots": [], "ring": [], "bracelet": [], "necklace": [], "weapon": []}
    diffComb = 1

    # test every wynn item according to users options
    for itemType in DATA:
        if itemType in itemDict or itemType == weaponArg: # rule out crafting materials and other weapon types
            for item in DATA[itemType]: # for each item do tests
                dataItem = DATA[itemType][item]
                if dataItem["requirements"]["level"] >= lvlMin and dataItem["requirements"]["level"] <= lvlMax: # level requirements
                    # TODO add more tests later
                    itemDict[itemType if itemType != weaponArg else "weapon"].append(dataItem)

    # calc amount of diff combinations to test
    for list in itemDict: 
        diffComb *= len(itemDict[list])

    # ask user if they want to procede
    if input(f" [ARE YOU SURE] There Are {humanize.intword(diffComb)} Different Combinations to Calculate (y/n): ") == "y": 
        build_search(itemDict, diffComb)
    else:
        inputs()

def build_search(itemDict, diffComb):
    print(" >>> Set Finder")

    helmet = ["No helmet"] if itemDict.get("helmet") == None else itemDict["helmet"]
    chestplate = ["No chestplate"] if itemDict.get("chestplate") == None else itemDict["chestplate"]
    leggings = ["No leggings"] if itemDict.get("leggings") == None else itemDict["leggings"]
    boots = ["No boots"] if itemDict.get("boots") == None else itemDict["boots"]
    ring = ["No ring"] if itemDict.get("ring") == None else itemDict["ring"]
    bracelet = ["No bracelet"] if itemDict.get("bracelet") == None else itemDict["bracelet"]
    necklace = ["No necklace"] if itemDict.get("necklace") == None else itemDict["necklace"]
    weapon = ["No weapon"] if itemDict.get("weapon") == None else itemDict["weapon"]

    buildList = list(itertools.product(helmet, chestplate, leggings, boots, ring, bracelet, necklace, weapon))

    bestBuild = [0, []]

    start = time.perf_counter()
    for i, build in enumerate(buildList):
        print(f"{round(((i / diffComb) * 100), 2)}% Done")
        results = damage_calc(build)
        if results[0] > bestBuild[0]:
            bestBuild = results
    stop = time.perf_counter()
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(f"{i} Calculated")

    # 20.41542379999737s without enumeration
    # 20.30976660000306s with enumeration

    # print(f"Elapsed time: {stop, start}")
    print(f"Elapsed time: {stop - start}")
    f = open("./json/elegable.json", "w", encoding="utf+8")
    f.write(json.dumps(bestBuild, indent=4))

def damage_calc(build):
    helmt = build[0]
    chest = build[1]
    leggs = build[2]
    boots = build[3]
    rings = build[4]
    brace = build[5]
    necks = build[6]
    weapn = build[7]

    damage = 0
    
    damage += find_value(helmt, "waterDamage")
    damage += find_value(chest, "waterDamage")
    damage += find_value(leggs, "waterDamage")
    damage += find_value(boots, "waterDamage")
    damage += find_value(rings, "waterDamage")
    damage += find_value(brace, "waterDamage")
    damage += find_value(necks, "waterDamage")
    damage += find_value(weapn, "waterDamage")

    return [damage, build]

def find_value(data, key):
    if not isinstance(data, dict):
        return 0

    try:
        return data[key]
    except KeyError:
        for sub_data in data.values():
            sub_value = find_value(sub_data, key)
            if type(sub_value) == dict:
                return sub_value["max"]
            elif sub_value is not 0:
                return sub_value

    return 0



def lb():
    print("-------------------------------------------------------------------")

if __name__ == "__main__":
    lb()
    main()
    lb()

# ----------------------------------- TODO ----------------------------------- #
# 1. section out necklace, bracelet, and ring aswell 

# --------------------------- THINGS TO ACCOUNT FOR -------------------------- #
# Powder Slots
# Armor Buffs


# ----------------------------------- COUNT ---------------------------------- #
# helmet: 423
# bow: 345
# wand: 339
# chestplateplate: 385
# necklace: 199
# dagger: 349
# spear: 348
# relik: 301
# ring: 261
# boots: 350
# braceletlet: 206
# leggings: 351
# other: 1215
# TOTAL: 5072
# TOTAL COMBINATIONS: ~23.0 septillion
# --------------------------------- SECTIONS --------------------------------- #
# def sections():
#     items = json.loads(open("./json/items_old.json", "r", encoding="utf+8").read())
#     types = {"other": {}}

#     for x, item in enumerate(items):
#         if "type" in items[item]:
#             if items[item]["type"] not in types:
#                 types[items[item]["type"]] = {}
#             types[items[item]["type"]][item] = items[item]
#         elif "accessoryType" in items[item]:
#             if items[item]["accessoryType"] not in types:
#                 types[items[item]["accessoryType"]] = {}
#             types[items[item]["accessoryType"]][item] = items[item]
#         else:
#             types["other"][item] = items[item]
#     f = open("./json/items_new.json", "w", encoding="utf+8")
#     f.write(json.dumps(types, indent=4))
# ----------------------------------- TYPES ---------------------------------- #
# def types():
#     total = 0
#     combinations = 1
#     for item in DATA:
#         print(f"{item}: {len(DATA[item])}") # print lenght of each list
#         total += len(DATA[item])
#         if item not in ["spear", "relik", "bow", "dagger"]: # classes only have one weapon
#             combinations *= len(DATA[item])
#         if item == "ring": # multiply ring twice since there is two slots
#             combinations *= len(DATA[item])
#     print(f"Total: {total}")
#     print(f"Combinations: ~{humanize.intword(combinations)}")
    
# def fetch_all():
#     print(" >>> Fetching All Items!")
#     try:
#         data = requests.get(URL)

#         f = open("./json/items.json", "w", encoding="utf-8")
#         f.write(str(json.dumps(data.json(), indent=4)))
#         f.close()
        
#         print(" >>> Successfully Fetched & Wrote Data!")
#     except:
#         print(" >>> Failed To Get Data :(")
# ------------------------------------ MAX ----------------------------------- #
# def max():
#     res = {}
#     type = input("[1] Bow\n[2] Wand\n[3] Spear\n[4] Relik\n[5] Dagger\nSelect A Type: ")
#     match type:
#         case "1":
#             type = "bow"
#         case "2":
#             type = "wand"
#         case "3":
#             type = "spear"
#         case "4":
#             type = "relik"
#         case "5":
#             type = "dagger"

#     for item in DATA[type]:
#         if res == {}:
#             res = DATA[type][item]
#         if "base" in DATA[type][item] and DATA[type][item]["base"]["averageDPS"] > res["base"]["averageDPS"]:
#             res = DATA[type][item]

#     lb()
#     print(f'Name: {res["internalName"]}\nTier: {res["tier"]}\nAvgDamage: {res["base"]["averageDPS"]}')
# ----------------------------------- COMB ----------------------------------- #
# def comb():
#     temp_json = {
#         "helmet": {},
#         "chestplateplate": {},
#         "leggings": {},
#         "boots": {},
#         "weapon": {},
#         "ring": {},
#         "braceletlet": {},
#         "necklace": {},
#     }
#     comp_comb = 1
#     for category in DATA:
#         if category in temp_json and category != "weapon":
#             for item in DATA[category]:
#                 if DATA[category][item]["requirements"]["level"] > LEVEL:
#                     try:
#                         if DATA[category][item]["identifications"][f"{ARMOR_SEARCH}Damage"]:
#                             if temp_json[category] == {}:
#                                 temp_json[category] = DATA[category][item]
#                             try:
#                                 if temp_json[category]["identifications"][f"{ARMOR_SEARCH}Damage"]["max"] < DATA[category][item]["identifications"][f"{ARMOR_SEARCH}Damage"]["max"]:
#                                     temp_json[category] = DATA[category][item]
#                             except:
#                                 try:
#                                     if temp_json[category]["identifications"][f"{ARMOR_SEARCH}Damage"]["max"] < DATA[category][item]["identifications"][f"{ARMOR_SEARCH}Damage"]:
#                                         temp_json[category] = DATA[category][item]
#                                 except:
#                                     try:
#                                         if temp_json[category]["identifications"][f"{ARMOR_SEARCH}Damage"] < DATA[category][item]["identifications"][f"{ARMOR_SEARCH}Damage"]:
#                                             temp_json[category] = DATA[category][item]
#                                     except:
#                                         if temp_json[category]["identifications"][f"{ARMOR_SEARCH}Damage"] < DATA[category][item]["identifications"][f"{ARMOR_SEARCH}Damage"]["max"]:
#                                             temp_json[category] = DATA[category][item]
#                     except KeyError:
#                         pass 
#         if category == WEAPON:
#             for item in DATA[WEAPON]:
#                 if DATA[WEAPON][item]["requirements"]["level"] > LEVEL:
#                     try:
#                         if DATA[WEAPON][item]["base"][f"{WEAPON_SEARCH}Damage"]:
#                             if temp_json["weapon"] == {}:
#                                 temp_json["weapon"] = DATA[WEAPON][item]
#                             elif temp_json["weapon"]["base"][f"{WEAPON_SEARCH}Damage"]["max"] < DATA[WEAPON][item]["base"][f"{WEAPON_SEARCH}Damage"]["max"]:
#                                 temp_json["weapon"] = DATA[WEAPON][item]
#                     except KeyError:
#                         pass 

#     # print(comp_comb)
#     # print(humanize.intword(comp_comb))
#     f = open("./json/elegable.json", "w", encoding="utf+8")
#     f.write(json.dumps(temp_json, indent=4))
#     total_dmg = 0
#     for item in temp_json:
#         print(f"------ {item} ------")
#         print(f"Name: {temp_json[item]['internalName']}")
#         print(f"Tier: {temp_json[item]['tier']}")
#         try:
#             print(f"Pwdr: {temp_json[item]['powderSlots']}")
#         except:
#             pass
#         try:
#             print(f"DmgM: {temp_json[item]['base'][f'{WEAPON_SEARCH}Damage']['max']}")
#         except:
#             pass
#         try:
#             print(f"DmgM: {temp_json[item]['identifications'][f'{ARMOR_SEARCH}Damage']['max']}%")
#             total_dmg += temp_json[item]['identifications'][f'{ARMOR_SEARCH}Damage']['max']
#         except:
#             try:
#                 print(f"DmgM: {temp_json[item]['identifications'][f'{ARMOR_SEARCH}Damage']}%")
#                 total_dmg += temp_json[item]['identifications'][f'{ARMOR_SEARCH}Damage']
#             except:
#                 pass

#         # print(f"-------{'-'*len(item)}-------")
#     print(f"Total Dmg%: {total_dmg}%")