import requests, json, humanize

URL = 'https://api.wynncraft.com/v3/item/database?fullResult'
DATA = json.loads(open("./json/items.json", "r", encoding="utf+8").read())

def main():
    combinations()

def lb():
    print("------------------------------------------------------------------")

if __name__ == "__main__":
    lb()
    main()
    lb()

# ----------------------------------- TODO ----------------------------------- #
# 1. section out necklace, brace, and ring aswell 

# --------------------------- THINGS TO ACCOUNT FOR -------------------------- #
# Powder Slots
# Armor Buffs


# ----------------------------------- COUNT ---------------------------------- #
# helmet: 423
# bow: 345
# wand: 339
# chestplate: 385
# necklace: 199
# dagger: 349
# spear: 348
# relik: 301
# ring: 261
# boots: 350
# bracelet: 206
# leggings: 351
# other: 1215
# TOTAL: 5072
# TOTAL COMBINATIONS: ~23.0 septillion
# --------------------------------- UNWANTED --------------------------------- #
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