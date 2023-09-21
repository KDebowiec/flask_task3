from flask import render_template, redirect, url_for, Blueprint, request, session, flash
from .models import Movie, Opinion
from . import db
from datetime import  datetime

# #Stwórz widoki, które umożliwią Ci dodawanie dowolnych tytułów filmów do bazy wraz z krótką opinią co do filmu,
# # oddzielny widok na wyświetlanie dodanych tytułów filmów, oraz widok na wyświetlanie "podsumowania" - tytuły filmów
# # + opinie. Zadbaj o poprawne zaprojektowanie modelów bazodanowych.
# Do filmów dodaj opis, id ma być
# Podpowiedź
# Może okazać się być konieczne zaimplementowanie relacji między tabelą filmów a opinii.

add_movie_blueprint = Blueprint('add_movie', __name__)
delete_movie_blueprint = Blueprint('delete_movie', __name__)
get_movies_blueprint = Blueprint('get_movies', __name__)
get_movies_with_opinions_blueprint = Blueprint('get_movies_with_opinions', __name__)
index_blueprint = Blueprint('index', __name__)


@add_movie_blueprint.route('/adding-movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('add_movie.html')

    if request.method == 'POST':
        title = request.form['name']
        description = request.form['description']
        opinion_text = request.form['opinion']

        opinion = Opinion(content=opinion_text)
        db.session.add(opinion)
        db.session.commit()

        movie = Movie(title=title, description=description, opinion=opinion)
        db.session.add(movie)
        db.session.commit()
        return redirect('/adding-movie')


@delete_movie_blueprint.route('/delete/movie', methods=['GET', 'POST'])
def delete_movie():
    if request.method == 'GET':
        return render_template('delete_movie.html')

    if request.method == 'POST':
        movie_id = request.form['movie_id']
        movie_to_delete = Movie.query.get(movie_id)
        delete_from_db(movie_to_delete)
        id_opinion_to_delete = movie_to_delete.opinion
        opinion_to_delete = Opinion.query.get(id_opinion_to_delete)
        delete_from_db(opinion_to_delete)
        return redirect('/delete/movie')


def delete_from_db(movie_to_delete: Movie) -> None:
    db.session.delete(movie_to_delete)
    db.session.commit()


@get_movies_blueprint.route('/movies', methods=['GET', 'POST'])
def get_movies() -> str:
    all_movies = Movie.query.all()
    return render_template('movies.html', movies=all_movies)


@get_movies_with_opinions_blueprint.route('/opinions', methods=['GET', 'POST'])
def get_movies_with_opinions():
    titles_and_opinions = Movie.query.join(Movie.opinion).all()
    return render_template('view_titles_and_opinions.html', titles_and_opinions=titles_and_opinions)

@index_blueprint.route('/')
def index():
    return render_template('index.html')
