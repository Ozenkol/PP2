movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def above_5_5(film):
    if film.get("imdb")>5.5:
        return True
    return False


def list_above_5_5(list):
    res = []
    for x in list:
        if above_5_5(x):
            res.append(x)
    return res


def return_category(list, category_name):
    res = []
    for x in list:
        if x.get("category") == category_name:
            res.append(x)
    return res


def return_average_mark(movies):
    sum_score = 0
    count = 0
    for film in movies:
        sum_score+=film.get("imdb")
        count = count + 1
    return sum_score/count


def return_average_mark_of_category(movies, category):
    category_movies = return_category(movies, category)
    return return_average_mark(category_movies)

#print(list_above_5_5(movies))
#print(return_category(movies, "Comedy"))
#print(f"{return_average_mark(movies):.3f}")
#print(return_average_mark_of_category(movies, "Romance"))


