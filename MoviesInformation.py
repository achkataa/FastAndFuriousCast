import imdb
input_movie = input()
if input_movie == "The Fast and the Furious":
    ia = imdb.IMDb()
    code = "0232500"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)

elif input_movie == "2 Fast 2 Furious":
    ia = imdb.IMDb()
    code = "0322259"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
elif input_movie == "The Fast and the Furious: Tokyo Drift":
    ia = imdb.IMDb()
    code = "0463985"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
elif input_movie == "Fast and Furious 4":
    ia = imdb.IMDb()
    code = "1013752"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
elif input_movie == "Fast Five":
    ia = imdb.IMDb()
    code = "1596343"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
elif input_movie == "Furious 6":
    ia = imdb.IMDb()
    code = "1905041"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
elif input_movie == "Fast & Furious 7":
    ia = imdb.IMDb()
    code = "2820852"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
elif input_movie == "The Fate of the Furious":
    ia = imdb.IMDb()
    code = "4630562"
    movie = ia.get_movie(code)
    casts_objects = movie.get('cast')
    casts = []
    for person in casts_objects:
        casts.append(person.get('name'))
    print(casts)
else:
    print("This movie is not part of the Fast Saga")

#actor = cast[0]
#print(actor)