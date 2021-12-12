db = [{'artist': 'Dart', 'name': 'Cat', 'youtube_id': 'abi'}, {'artist':'Blow', 'name':'Kind', 'youtube_id': 'mean'},{'artist': 'Hi', 'name': 'Cat', 'youtube_id': 'mom'}]

def binary_search(db, key_word, key_answer):
    sorted_db = sorted(db, key = lambda i: (i[key_word]))
    first = 0 
    last = len(sorted_db)-1
    index = -1 
    while (first <= last) and (index == -1):
        mid = (first+last)//2 
        if sorted_db[mid][key_word] == key_answer:
            return (sorted_db[mid])
        else: 
            if key_answer<sorted_db[mid][key_word]:
                last = mid-1
            else: 
                first = mid+1
    return print('Resultado no encontrado') 

def ask_user(song):
    if song is not None:
        link = 'https://www.youtube.com/watch?v=' + song['youtube_id']
        print(f"\nNombre: {song['name']} \nArtista(s)/Banda: {song['artist']}\n")

        reproduce = input("¿Desea reproducir la canción? Si (s) o no (n): ").lower()
        while (reproduce!='s') and (reproduce!='n'):
            reproduce = input("Error: Ingrese (s) o (n): ").lower()
        if reproduce=='s':
            print("Enlace: {link}")
            webbrowser.open(link)
        

print("\n¡Bienvenido a la versión Terminal de YouTube Music!\n")
while True:
    try:
        user_choice = int(input("Elja la opción con qué desee buscar la canción: \n1.Nombre \n2.Artista/Banda \n>>> "))
        if user_choice not in range(1,3):
            raise ValueError
        break 
    except ValueError as Identifier:
        print("\nError: Dato ingresado no forma parte de las opciones")

if user_choice==1:
    user_song = input("Ingrese el nombre de la canción: ").title()
    song_name = binary_search(db, 'name', user_song)
    ask_user(song_name)

elif user_choice==2:
    user_artist = input("Ingrese el artista o la banda que toca la canción: ").title()
    song_artist = binary_search(db, 'artist', user_artist)
    ask_user(song_artist)