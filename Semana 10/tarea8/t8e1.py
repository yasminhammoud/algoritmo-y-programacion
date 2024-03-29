import webbrowser

def binary_search(db, key_word, key_answer):
    """[Busca en la lista de diccionarios si el input introducido se encuentra en dicha lista]

    Args:
        db ([list]): [Lista de diccionarios con los datos de varias canciones ]
        key_word ([str]): [Name o artist, en función a la elección del usuario]
        key_answer ([str]): [Artista o nombre de la canción, dependiendo del input del usuario]

    Returns:
        [dict]: [Datos de la canción que coincide con la búsqueda]
        [str]: [Imprime un string si el dato introducido no forma parte de la lista]
    """
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
    return print('¡Resultado no encontrado!') 

def ask_user(song):
    """[Retorna el enlace de la canción escogida y lo abre en la página]

    Args:
        song ([dict]): [Canción seleccionada por el usuario]
    """
    if song is not None:
        link = 'https://www.youtube.com/watch?v=' + song['youtube_id']
        print(f"\nNombre: {song['name']} \nArtista(s)/Banda: {song['artist']}\n")

        reproduce = input("¿Desea reproducir la canción? Si (s) o no (n): ").lower()
        while (reproduce!='s') and (reproduce!='n'):
            reproduce = input("Error: Ingrese (s) o (n): ").lower()
        if reproduce=='s':
            print(f"Enlace: {link}")
            webbrowser.open(link)

def main():
    db = [
        {
            "artist": "Pharrell Williams",
            "link": "http://top40-charts.com/song.php?sid=36547",
            "name": "Happy",
            "youtube_id": "Q-GLuydiMe4"
        },
        {
            "artist": "Katy Perry",
            "link": "http://top40-charts.com/song.php?sid=36874",
            "name": "Dark Horse",
            "youtube_id": "F9S-88WxPdE"
        },
        {
            "artist": "Shakira & Rihanna",
            "link": "http://top40-charts.com/song.php?sid=37908",
            "name": "Can't Remember To Forget You",
            "youtube_id": "o3VMyHr1gIg"
        },
        {
            "artist": "Clean Bandit & Jess Glynne",
            "link": "http://top40-charts.com/song.php?sid=37956",
            "name": "Rather Be",
            "youtube_id": "Y9ILr_ZiSmQ"
        },
        {
            "artist": "Pitbull & Ke$ha",
            "link": "http://top40-charts.com/song.php?sid=37049",
            "name": "Timber",
            "youtube_id": "kUbouR1PWBc"
        },
        {
            "artist": "A Great Big World & Christina Aguilera",
            "link": "http://top40-charts.com/song.php?sid=37275",
            "name": "Say Something",
            "youtube_id": "xCgv0Eq3dxE"
        },
        {
            "artist": "John Legend",
            "link": "http://top40-charts.com/song.php?sid=37001",
            "name": "All Of Me",
            "youtube_id": "450p7goxZqg"
        },
        {
            "artist": "David Guetta & Skylar Grey",
            "link": "http://top40-charts.com/song.php?sid=38090",
            "name": "Shot Me Down",
            "youtube_id": "yCdtmaIxmOY"
        },
        {
            "artist": "Beyonce & Jay-Z",
            "link": "http://top40-charts.com/song.php?sid=37767",
            "name": "Drunk In Love",
            "youtube_id": "p1JPKLa-Ofc"
        },
        {
            "artist": "Coldplay",
            "link": "http://top40-charts.com/song.php?sid=38271",
            "name": "Magic",
            "youtube_id": "1PvBc2TOpE4"
        },
        {
            "artist": "American Authors",
            "link": "http://top40-charts.com/song.php?sid=37469",
            "name": "Best Day Of My Life",
            "youtube_id": "Y66j_BUCBMY"
        },
        {
            "artist": "Avicii",
            "link": "http://top40-charts.com/song.php?sid=36888",
            "name": "Hey Brother",
            "youtube_id": "e-fnvfs0h0A"
        },
        {
            "artist": "OneRepublic",
            "link": "http://top40-charts.com/song.php?sid=36218",
            "name": "Counting Stars",
            "youtube_id": "hT_nvWreIhg"
        },
        {
            "artist": "Avicii",
            "link": "http://top40-charts.com/song.php?sid=36889",
            "name": "Addicted To You",
            "youtube_id": "z1K_bxetpoQ"
        },
        {
            "artist": "Jason Derulo & 2 Chainz",
            "link": "http://top40-charts.com/song.php?sid=36670",
            "name": "Talk Dirty",
            "youtube_id": "jZ2MUEfXbLo"
        },
        {
            "artist": "Sam Smith",
            "link": "http://top40-charts.com/song.php?sid=38065",
            "name": "Money On My Mind",
            "youtube_id": "K0G9T5Bnjlc"
        },
        {
            "artist": "Imagine Dragons",
            "link": "http://top40-charts.com/song.php?sid=36403",
            "name": "Demons",
            "youtube_id": "mWRsgZuwf_8"
        },
        {
            "artist": "Bastille",
            "link": "http://top40-charts.com/song.php?sid=35585",
            "name": "Pompeii",
            "youtube_id": "F90Cw4l-8NY"
        },
        {
            "artist": "Aloe Blacc",
            "link": "http://top40-charts.com/song.php?sid=37876",
            "name": "The Man",
            "youtube_id": "n_58FqEiG3I"
        },
        {
            "artist": "Martin Garrix",
            "link": "http://top40-charts.com/song.php?sid=36496",
            "name": "Animals",
            "youtube_id": "gCYcHz2k5x0"
        },
        {
            "artist": "Klingande",
            "link": "http://top40-charts.com/song.php?sid=36927",
            "name": "Jubel",
            "youtube_id": "b6vSf0cA9qY"
        },
        {
            "artist": "Passenger",
            "link": "http://top40-charts.com/song.php?sid=34830",
            "name": "Let Her Go",
            "youtube_id": "RBumgq5yVrA"
        },
        {
            "artist": "DVBBS & Borgeous",
            "link": "http://top40-charts.com/song.php?sid=36858",
            "name": "Tsunami",
            "youtube_id": "I41CX0RdmPQ"
        },
        {
            "artist": "Lorde",
            "link": "http://top40-charts.com/song.php?sid=36908",
            "name": "Team",
            "youtube_id": "4g03b4U_aPk"
        },
        {
            "artist": "Faul",
            "link": "http://top40-charts.com/song.php?sid=37508",
            "name": "Changes",
            "youtube_id": "AZKUj_iytuw"
        },
        {
            "artist": "Eminem & Rihanna",
            "link": "http://top40-charts.com/song.php?sid=37180",
            "name": "The Monster",
            "youtube_id": "ZDXXi19_7iE"
        },
        {
            "artist": "Lorde",
            "link": "http://top40-charts.com/song.php?sid=35706",
            "name": "Royals",
            "youtube_id": "LFasFq4GJYM"
        },
        {
            "artist": "Mr Probz",
            "link": "http://top40-charts.com/song.php?sid=36087",
            "name": "Waves",
            "youtube_id": "0a5WyAjL1MM"
        },
        {
            "artist": "Avicii",
            "link": "http://top40-charts.com/song.php?sid=36343",
            "name": "Wake Me Up!",
            "youtube_id": "AT29gXp6mss"
        },
        {
            "artist": "Zedd & Hayley Williams",
            "link": "http://top40-charts.com/song.php?sid=37007",
            "name": "Stay The Night",
            "youtube_id": "i-gyZ35074k"
        },
        {
            "artist": "Enrique Iglesias & Pitbull",
            "link": "http://top40-charts.com/song.php?sid=37950",
            "name": "I'm A Freak",
            "youtube_id": "DcalHi51gIc"
        },
        {
            "artist": "Ed Sheeran",
            "link": "http://top40-charts.com/song.php?sid=37267",
            "name": "I See Fire",
            "youtube_id": "uf8Fwiy0Bkc"
        },
        {
            "artist": "Route 94 & Jess Glynne",
            "link": "http://top40-charts.com/song.php?sid=38270",
            "name": "My Love",
            "youtube_id": "BS46C2z5lVE"
        },
        {
            "artist": "Cris Cab",
            "link": "http://top40-charts.com/song.php?sid=37421",
            "name": "Liar Liar",
            "youtube_id": "u-qYMl9T9wQ"
        },
        {
            "artist": "Neighbourhood",
            "link": "http://top40-charts.com/song.php?sid=37174",
            "name": "Sweater Weather",
            "youtube_id": "GCdwKhTtNNw"
        },
        {
            "artist": "Helene Fischer",
            "link": "http://top40-charts.com/song.php?sid=37509",
            "name": "Atemlos Durch Die Nacht",
            "youtube_id": "GbTNfBnCbvc"
        },
        {
            "artist": "DJ Tiesto",
            "link": "http://top40-charts.com/song.php?sid=37904",
            "name": "Red Lights",
            "youtube_id": "epYt235k6zQ"
        },
        {
            "artist": "One Direction",
            "link": "http://top40-charts.com/song.php?sid=37179",
            "name": "Story Of My Life",
            "youtube_id": "W-TE_Ys4iwM"
        },
        {
            "artist": "Kylie Minogue",
            "link": "http://top40-charts.com/song.php?sid=38092",
            "name": "Into The Blue",
            "youtube_id": "fL6FaI-wJxs"
        },
        {
            "artist": "Nico & Vinz",
            "link": "http://top40-charts.com/song.php?sid=38258",
            "name": "Am I Wrong",
            "youtube_id": "bg1sT4ILG0w"
        },
        {
            "artist": "Flo Rida",
            "link": "http://top40-charts.com/song.php?sid=37265",
            "name": "How I Feel",
            "youtube_id": "VmeIVJVjHuk"
        },
        {
            "artist": "Pixie Lott",
            "link": "http://top40-charts.com/song.php?sid=38342",
            "name": "Nasty",
            "youtube_id": "F7POcRxmpHQ"
        },
        {
            "artist": "Kanye West",
            "link": "http://top40-charts.com/song.php?sid=37621",
            "name": "Bound 2",
            "youtube_id": "BBAtAM7vtgc"
        },
        {
            "artist": "Christina Perri",
            "link": "http://top40-charts.com/song.php?sid=38154",
            "name": "Human",
            "youtube_id": "r5yaoMjaAmE"
        },
        {
            "artist": "Milky Chance",
            "link": "http://top40-charts.com/song.php?sid=37044",
            "name": "Stolen Dance",
            "youtube_id": "dAuAyA9dBBU"
        },
        {
            "artist": "Zedd",
            "link": "http://top40-charts.com/song.php?sid=38081",
            "name": "Stay The Night",
            "youtube_id": "iMQCH2rCAew"
        },
        {
            "artist": "Adel Tawil",
            "link": "http://top40-charts.com/song.php?sid=37238",
            "name": "Lieder",
            "youtube_id": "kiMG_JV2gbo"
        },
        {
            "artist": "Lily Allen",
            "link": "http://top40-charts.com/song.php?sid=37490",
            "name": "Hard Out Here",
            "youtube_id": "E0CazRHB0so"
        },
        {
            "artist": "Bruno Mars",
            "link": "http://top40-charts.com/song.php?sid=35305",
            "name": "Young Girls",
            "youtube_id": "CyM5AjiZris"
        },
        {
            "artist": "Foxes",
            "link": "http://top40-charts.com/song.php?sid=37952",
            "name": "Let Go For Tonight",
            "youtube_id": "Pecj5GGjQi8"
        },
        {
            "artist": "Chris Brown & Nicki Minaj",
            "link": "http://top40-charts.com/song.php?sid=36585",
            "name": "Love More",
            "youtube_id": "KPzn7kwrHJc"
        },
        {
            "artist": "Revolverheld",
            "link": "http://top40-charts.com/song.php?sid=37911",
            "name": "Ich Lass Fur Dich Das Licht An",
            "youtube_id": "dQdDDWS1fN0"
        },
        {
            "artist": "Ellie Goulding",
            "link": "http://top40-charts.com/song.php?sid=36530",
            "name": "Burn",
            "youtube_id": "CGyEd0aKWZE"
        },
        {
            "artist": "Blake Shelton",
            "link": "http://top40-charts.com/song.php?sid=37048",
            "name": "Mine Would Be You",
            "youtube_id": "9JkdBnT7j2I"
        },
        {
            "artist": "Sara Bareilles",
            "link": "http://top40-charts.com/song.php?sid=36713",
            "name": "Brave",
            "youtube_id": "QUQsqBqxoR4"
        },
        {
            "artist": "Macklemore, Ryan Lewis, ScHoolboy Q & Hollis",
            "link": "http://top40-charts.com/song.php?sid=36756",
            "name": "White Walls",
            "youtube_id": "QbYFcsd026I"
        },
        {
            "artist": "Chainsmokers",
            "link": "http://top40-charts.com/song.php?sid=38201",
            "name": "#SELFIE",
            "youtube_id": "kdemFfbS5H0"
        },
        {
            "artist": "Magic!",
            "link": "http://top40-charts.com/song.php?sid=37489",
            "name": "Rude",
            "youtube_id": "xjqQfVY0yAc"
        },
        {
            "artist": "Beyonce Knowles",
            "link": "http://top40-charts.com/song.php?sid=37947",
            "name": "Partition",
            "youtube_id": "COHXL4bIhBE"
        },
        {
            "artist": "Drake",
            "link": "http://top40-charts.com/song.php?sid=36675",
            "name": "Hold On We're Going Home",
            "youtube_id": "GxgqpCdOKak"
        },
        {
            "artist": "Kim Cesarion",
            "link": "http://top40-charts.com/song.php?sid=35940",
            "name": "Undressed",
            "youtube_id": "ZwjjWSHDCMc"
        },
        {
            "artist": "Idina Menzel",
            "link": "http://top40-charts.com/song.php?sid=37842",
            "name": "Let It Go",
            "youtube_id": "iEKLFS-aKcw"
        },
        {
            "artist": "Bastille",
            "link": "http://top40-charts.com/song.php?sid=37424",
            "name": "Of The Night",
            "youtube_id": "ZCTDKLjdok4"
        },
        {
            "artist": "Disclosure & Mary J. Blige",
            "link": "http://top40-charts.com/song.php?sid=38036",
            "name": "F For You",
            "youtube_id": "n0FOPTYJPXw"
        },
        {
            "artist": "5 Seconds Of Summer",
            "link": "http://top40-charts.com/song.php?sid=38250",
            "name": "She Looks So Perfect",
            "youtube_id": "X2BYmmTI04I"
        },
        {
            "artist": "Jason Derulo",
            "link": "http://top40-charts.com/song.php?sid=37673",
            "name": "Trumpets",
            "youtube_id": "oOAfz0H4f00"
        },
        {
            "artist": "Cash Cash",
            "link": "http://top40-charts.com/song.php?sid=37309",
            "name": "Take Me Home",
            "youtube_id": "kDo2SiW3JHU"
        },
        {
            "artist": "Marteria",
            "link": "http://top40-charts.com/song.php?sid=38041",
            "name": "OMG!",
            "youtube_id": "XXoRoLdXnvU"
        },
        {
            "artist": "Savage",
            "link": "http://top40-charts.com/song.php?sid=12795",
            "name": "Swing",
            "youtube_id": "bCzPVv5GXEM"
        },
        {
            "artist": "Paloma Faith",
            "link": "http://top40-charts.com/song.php?sid=38207",
            "name": "Can't Rely On You",
            "youtube_id": "imi9Smkt_cI"
        },
        {
            "artist": "Marteria",
            "link": "http://top40-charts.com/song.php?sid=37742",
            "name": "Kids (2 Finger An Den Kopf)",
            "youtube_id": "fkMg_X9lHMc"
        },
        {
            "artist": "Stromae",
            "link": "http://top40-charts.com/song.php?sid=36738",
            "name": "Tous Les Memes",
            "youtube_id": "zeHWMnHrH3s"
        },
        {
            "artist": "Indila",
            "link": "http://top40-charts.com/song.php?sid=37796",
            "name": "Derniere Danse",
            "youtube_id": "rEgRzLXqWUI"
        },
        {
            "artist": "Nathaniel",
            "link": "http://top40-charts.com/song.php?sid=38307",
            "name": "You're Beautiful",
            "youtube_id": "jEVMS7Lhj9E"
        },
        {
            "artist": "London Grammar",
            "link": "http://top40-charts.com/song.php?sid=36359",
            "name": "Wasting My Young Years",
            "youtube_id": "ww6PFW9uU9o"
        },
        {
            "artist": "Pitbull & G.R.L.",
            "link": "http://top40-charts.com/song.php?sid=38253",
            "name": "Wild Wild Love",
            "youtube_id": "cuOpXHunq6U"
        },
        {
            "artist": "Rihanna",
            "link": "http://top40-charts.com/song.php?sid=38027",
            "name": "Jump",
            "youtube_id": "CLsamA1bCMc"
        },
        {
            "artist": "Daft Punk & Julian Casablancas",
            "link": "http://top40-charts.com/song.php?sid=36187",
            "name": "Instant Crush",
            "youtube_id": "O9BK3xcRH1g"
        },
        {
            "artist": "John Newman",
            "link": "http://top40-charts.com/song.php?sid=36197",
            "name": "Love Me Again",
            "youtube_id": "CfihYWRWRTQ"
        },
        {
            "artist": "Maitre Gims",
            "link": "http://top40-charts.com/song.php?sid=37705",
            "name": "Zombie",
            "youtube_id": "6yDEYu61piI"
        },
        {
            "artist": "Rudimental & Emeli Sande",
            "link": "http://top40-charts.com/song.php?sid=37733",
            "name": "Free",
            "youtube_id": "KDPW_g2AhAU"
        },
        {
            "artist": "George Ezra",
            "link": "http://top40-charts.com/song.php?sid=37978",
            "name": "Budapest",
            "youtube_id": "uOaWE3BO_GE"
        },
        {
            "artist": "Will.I.am & Miley Cyrus",
            "link": "http://top40-charts.com/song.php?sid=37818",
            "name": "Feelin' Myself",
            "youtube_id": "VRuoR--LdqQ"
        },
        {
            "artist": "Cats On Trees",
            "link": "http://top40-charts.com/song.php?sid=37203",
            "name": "Sirens Call",
            "youtube_id": "X3hJYDGSXt4"
        },
        {
            "artist": "Stromae",
            "link": "http://top40-charts.com/song.php?sid=36241",
            "name": "Formidable",
            "youtube_id": "S_xH7noaqTA"
        },
        {
            "artist": "Tegan & Sara",
            "link": "http://top40-charts.com/song.php?sid=38099",
            "name": "Everything Is Awesome!!!",
            "youtube_id": "t6lHm-stXdM"
        },
        {
            "artist": "Brings",
            "link": "http://top40-charts.com/song.php?sid=38329",
            "name": "Koelsche Jung",
            "youtube_id": "DcNPqsWPbD8"
        },
        {
            "artist": "Katy Perry",
            "link": "http://top40-charts.com/song.php?sid=37172",
            "name": "Unconditionally",
            "youtube_id": "hHimjVYsd6I"
        },
        {
            "artist": "Neon Jungle",
            "link": "http://top40-charts.com/song.php?sid=37958",
            "name": "Braveheart",
            "youtube_id": "3iJeEAZM5xk"
        },
        {
            "artist": "Lily Allen",
            "link": "http://top40-charts.com/song.php?sid=38178",
            "name": "Air Balloon",
            "youtube_id": "vo9Fja5x04o"
        },
        {
            "artist": "DJ Snake & Lil Jon",
            "link": "http://top40-charts.com/song.php?sid=37843",
            "name": "Turn Down For What",
            "youtube_id": "hmfJ7L6ndyM"
        },
        {
            "artist": "Daft Punk",
            "link": "http://top40-charts.com/song.php?sid=35888",
            "name": "Get Lucky",
            "youtube_id": "5NV6Rdv1a3I"
        },
        {
            "artist": "Gary Barlow",
            "link": "http://top40-charts.com/song.php?sid=37453",
            "name": "Let Me Go",
            "youtube_id": "ENrj5u_lrWw"
        },
        {
            "artist": "Eminem & Nate Ruess",
            "link": "http://top40-charts.com/song.php?sid=38071",
            "name": "Headlights",
            "youtube_id": "PaweQyUiRME"
        },
        {
            "artist": "London Grammar",
            "link": "http://top40-charts.com/song.php?sid=36766",
            "name": "Strong",
            "youtube_id": "6drfp_3823I"
        },
        {
            "artist": "Lily Allen",
            "link": "http://top40-charts.com/song.php?sid=37401",
            "name": "Somewhere Only We Know",
            "youtube_id": "Ve9cBwI-pAg"
        },
        {
            "artist": "Cat Ballou",
            "link": "http://top40-charts.com/song.php?sid=38330",
            "name": "Et Jitt Kein Wood",
            "youtube_id": "VF6p-BGQcl4"
        },
        {
            "artist": "Lady Gaga & R. Kelly",
            "link": "http://top40-charts.com/song.php?sid=37164",
            "name": "Do What U Want",
            "youtube_id": "A3jzMyYgPQs"
        },
        {
            "artist": "Tom Odell",
            "link": "http://top40-charts.com/song.php?sid=35181",
            "name": "Another Love",
            "youtube_id": "MwpMEbgC7DA"
        }
    ]
    
    print("\n¡Bienvenido a la versión Terminal de YouTube Music!\n")
    
    while True:

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

        user_continue = (input("\n¿Desea buscar otra canción? ('si' o 'no'): ")).lower()
        while user_continue!='si' and user_continue!='no':
            user_continue = (input("Error: Ingrese 'si' o 'no': ")).lower()

        if user_continue == 'si':
            continue
        else:
            break 


main()