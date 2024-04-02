import requests, json

URL = 'https://api.wynncraft.com/v3/item/database?fullResult'

def main():
    lb()
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