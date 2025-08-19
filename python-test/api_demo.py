import requests

def catRandomFact():
    url = "https://meowfacts.herokuapp.com/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()   # JSON parse
        fact = data["data"][0]   # fact extract
        return fact
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    fact = catRandomFact()
    if fact:
        print(f"🐱 Random Cat Fact: {fact}")

main()
