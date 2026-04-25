from flask import Flask, render_template, redirect
from data.login import LoginForm
from data import db_session
from data.models import Event,User
from flask_login import LoginManager, login_user,logout_user,login_required, current_user
from data.register import RegisterForm
from data.event_form import EventForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def index():
    session = db_session.create_session()
    events = session.query(Event).all()
    session.close()
    return render_template('index.html', events=events)


@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        event = Event()
        event.title = form.title.data
        event.description = form.description.data
        event.date = form.date.data
        event.location = form.location.data
        event.city = form.city.data
        event.max_volunteers = form.max_volunteers.data
        event.author_id = current_user.id
        session.add(event)
        session.commit()
        return redirect('/')

    return render_template('create_event.html', title='Создать событие', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname = form.surname.data,
            age=form.age.data,
        city=form.city.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Профиль')

@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.get(User, user_id)

if __name__ == '__main__':
    db_session.global_init("db/dobro.db")
    app.run(port=8080, host='127.0.0.1')
