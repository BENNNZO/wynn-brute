import requests, json

URL = 'https://api.wynncraft.com/v3/item/database?fullResult'

def main():
    types()

def types():
    items = json.loads(open("./json/items.json", "r", encoding="utf+8").read())
    lb()
    for item in items:
        print(f"{item}: {len(items[item])}")
    lb()


def fetch_all():
    lb()
    print(" >>> Fetching All Items!")
    try:
        data = requests.get(URL)

        f = open("./json/items.json", "w", encoding="utf-8")
        f.write(str(json.dumps(data.json(), indent=4)))
        f.close()
        
        print(" >>> Successfully Fetched & Wrote Data!")
    except:
        print(" >>> Failed To Get Data :(")
    lb()

def lb():
    print("------------------------------------------------------------------")

if __name__ == "__main__":
    main()


# ------------------------------------------------------------------
# total: 5072
# other: 1881
# helmet: 423
# bow: 345
# wand: 339
# chestplate: 385
# dagger: 349
# spear: 348
# relik: 301
# boots: 350
# leggings: 351
# ------------------------------------------------------------------
    # old code i used to section out the old json data for easier parsing
# for x, item in enumerate(items):
# get count of all types and others
# if "type" in items[item] and items[item]["type"] not in types:
#     types[items[item]["type"]] = 1
# elif "type" in items[item] and items[item]["type"] in types:
#     types[items[item]["type"]] += 1
# else:
#     types["other"] += 1
# types["total"] += 1

# if "type" in items[item]:
#     if items[item]["type"] not in types_json:
#         types_json[items[item]["type"]] = {}
#     types_json[items[item]["type"]][item] = items[item]
# else:
#     types_json["other"][item] = items[item]

# if "type" in items[item] and items[item]["type"] == "wand":
# f = open("./json/formatted_items.json", "w", encoding="utf+8")
# f.write(str(json.dumps(types_json, indent=4)))
# ------------------------------------------------------------------