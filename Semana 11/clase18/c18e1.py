import requests

def api_IMDB(param, movie):
  
  url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/{param}/{movie}"

  headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "3c8c5d566cmsh229d3ed10b518aap134546jsn473be93517cb"
    }

  response = requests.request("GET", url, headers=headers)

  return response.json()

def movie_search(movie):
  movies = api_IMDB('search', movie)

  for i, movie in enumerate(movies['titles']):
    print(f"{i+1}.{movie['title']}")

  while True: 
    try: 
      option = int(input('¿Cuál película deseas ver? '))
      if option not in range(1, len(movies)+1):
        raise ValueError
      break 
    except ValueError:
      print("Error: Dato inválido")

  movie_selected = movies['titles'][option-1]['id']

  result = api_IMDB('film', movie_selected)

  print(result)


def main():

  movie = input("Ingresa la película que deseas buscar: ")

  movie_search(movie)

main()