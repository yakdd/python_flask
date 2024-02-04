from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
movies = []


class Movie(BaseModel):
    id: int
    title: str
    year: int
    description: str
    gener: str
    delete: bool

    def __repr__(self):
        return f'Movie => id:{self.id}, title:{self.title}, year:{self.year} description:{self.description}, gener:{self.gener}, delete:{self.delete}    |    '


@app.get('/')
async def root():
    return movies


@app.get('/movies/')
async def get_movies():
    active_list = []
    for movie in movies:
        if not movie.delete:
            active_list.append(movie)
    return active_list


@app.get('/movies/id/{movie_id}')
async def get_by_id(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            return movie
    return HTTPException(status_code=404, detail=f'Movie not fount')


@app.get('/movies/gener/{gener}')
async def get_by_gener(gener: str):
    gener_list = []
    for movie in movies:
        if movie.gener == gener:
            gener_list.append(movie)
    return gener_list


@app.post('/movies/')
async def add_movie(movie: Movie):
    print(movie)
    movies.append(movie)
    return movie


@app.put('/movies/{movie_id}')
async def update_movie(movie_id: int, up_movie: Movie):
    for i, movie in enumerate(movies):
        if movie.id == movie_id:
            movies[i] = up_movie
            return {'id': movie_id, 'movie': up_movie}
    return HTTPException(status_code=404, detail=f'Movie {movie_id} not fount')


@app.delete('/movies/{movie_id}')
async def delete_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            movie.delete = True
            return movies
    return HTTPException(status_code=404, detail=f'Movie {movie_id} not fount')
