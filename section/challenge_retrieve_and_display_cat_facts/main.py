import requests

def print_three_cat_facts():
    for _ in range(3):
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        print(data["fact"])

print_three_cat_facts()
