from flask import Flask, render_template, redirect
from data.login import LoginForm
from data import db_session
from data.models import Event

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    session = db_session.create_session()
    events = session.query(Event).all()
    session.close()
    return render_template('index.html', events=events)


@app.route('/login', methods=['GET', ' POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/dobro.db")
    app.run(port=8080, host='127.0.0.1')
