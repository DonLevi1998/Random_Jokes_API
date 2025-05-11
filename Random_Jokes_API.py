import requests

# Service (JokeAPI)
def get_random_joke():
    try:
        response = requests.get('https://v2.jokeapi.dev/joke/Programming?lang=es')
        data = response.json()
        if data["type"] == "single":
            return data["joke"]
        else:
            return f"{data['setup']}... {data['delivery']}"
    except Exception as e:
        return f"Error, try again: {e}"
    
if __name__ == "__main__":
    print("=== Random joke API ===")
    print(get_random_joke())
    print("\n😂😂😂😂:")
    