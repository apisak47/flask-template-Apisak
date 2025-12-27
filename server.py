from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='My Home Page', msg='This is my Message')

@app.route('/user/info')
def user_info():
    return render_template('info.html',
                            title='Info.html', 
                            name='Apisak Kamprasort',
                            email='std.66122420222@ubru.com',
                            mobile='095-719-7602',
                            age=21)

@app.route('/user/favorite_sports')
def fav_sports():
    sports = ['Football', 'Esports', 'Volleyball']
    title = 'Favorite Sports Page'
    return render_template('favorite_sports.html',
                            title=title,
                            sports=sports)

@app.route('/user/favorite_foods')
def fav_foods():
    foods = ['กระเพราหมูกรอบ', 'ก๋วยจั๊บ', 'ซูชิ',]
    title = 'Favorite Foods Page'
    return render_template('favorite_foods.html',
                            title=title,
                            foods=foods)

@app.route('/movies')
def fav_movies():
    movies = [
        "Fast and Furious", 
        "Deadpool", 
        "Death Race", 
        "Jurassic World", 
        "Transformers"]
    title = 'Favorite Movies Page'
    return render_template('movies.html', title=title, movies=movies)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)