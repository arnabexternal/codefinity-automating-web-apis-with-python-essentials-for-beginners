import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data["fact"])
    except requests.exceptions.RequestException:
        print("Failed to retrieve cat fact.")
    except Exception:                # catches both RequestException and ValueError
        print("Failed to retrieve cat fact.")

get_cat_fact()