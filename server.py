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

@app.route('/favorite/sports')
def fav_spots():
    sports = ['Football', 'Esports', 'Volleyball']
    title = 'Favorite Sports Page'
    return render_template('favorite_sports.html',
                            title=title,
                            sports=sports)

@app.route('/favorite/foods')
def fav_foods():
    foods = ['กระเพราหมูกรอบ', 'ก๋วยจั๊บ', 'ซูชิ',]
    title = 'Favorite Foods Page'
    return render_template('favorite_foods.html',
                            title=title,
                            foods=foods)