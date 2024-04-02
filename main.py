import requests

# URL = 'https://api.wynncraft.com/public_api.php?action=itemDB&category={"armor"}'
URL = 'https://api.wynncraft.com/v2/player/BENNNNZO/stats'

def main():
    x = requests.get(URL)
    print(x.json())

if __name__ == "__main__":
    main()
