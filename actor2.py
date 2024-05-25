import requests

def get_actor_filmography(actor_name):
    # API endpoint for searching actors
    search_url = "https://api.themoviedb.org/3/search/person"

    # Parameters for the search query
    params = {
        "api_key": "b2cfc346a8efc688dc502ab7143d328c",  
        "query": actor_name
    }

    # Send GET request to search for the actor
    response = requests.get(search_url, params=params)
    data = response.json()

    # Check if any results were found
    if data['total_results'] == 0:
        raise Exception(f"No results found for actor: {actor_name}")

    # Get the ID of the first actor in the search results
    actor_id = data['results'][0]['id']

    # API endpoint for retrieving the actor's movie credits
    credits_url = f"https://api.themoviedb.org/3/person/{actor_id}/movie_credits"

    # Parameters for retrieving movie credits
    params = {
        "api_key": "b2cfc346a8efc688dc502ab7143d328c"  
    }

    # Send GET request to retrieve movie credits
    response = requests.get(credits_url, params=params)
    credits_data = response.json()

    # Extract movie titles and release years from the credits data
    filmography = []
    for credit in credits_data['cast']:
        title = credit['title']
        release_year = credit['release_date'].split('-')[0] if credit['release_date'] else "Unknown"
        filmography.append((title, release_year))

    # Sort filmography by release year in descending order
    filmography.sort(key=lambda x: x[1], reverse=True)

    return filmography

def main():
    actor_name = input("Enter the name of the actor: ")
    try:
        filmography = get_actor_filmography(actor_name)
        if not filmography:
            print(f"No filmography found for {actor_name}")
        else:
            print(f"Filmography of {actor_name}:")
            for title, year in filmography:
                print(f"{year} - {title}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
