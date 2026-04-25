from data import db_session
from data.models import User

def main():

    db_session.global_init("db/dobro.db")
    db_sess = db_session.create_session()

    user = User()
    user.name = "Алена"
    user.email = "alena@yandex.ru"
    user.set_password("123")
    user.city = "Тольятти"

    db_sess.add(user)
    db_sess.commit()


if __name__ == "__main__":
    main()
