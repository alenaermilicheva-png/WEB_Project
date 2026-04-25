from data import db_session
import datetime
from data.models import User, Event

def main():

    db_session.global_init("db/dobro.db")
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()

    events_data = [{"title": "Уборка парка", "description": "Поможем убрать мусор в парке",
                    "date": datetime.datetime(2026, 5, 15, 10, 0),
                    "location": "Парк победы", "city": "Тольятти", "author_id": user.id},
                   {"title": "Помощь приюту для животных", "description": "Выгул собак и уборка вольеров",
                    "date": datetime.datetime(2026, 5, 20, 14, 0),
                    "location": "Приют",
                    "city": "Москва", "author_id": user.id},
                   {"title": "Посадка деревьев", "description": "Озеленение района",
                    "date": datetime.datetime(2026, 5, 25, 9, 0),
                    "location": "Сквер", "city": "Санкт-Петербург", "author_id": user.id}]

    for event_data in events_data:
        event = Event()
        event.title = event_data["title"]
        event.description = event_data["description"]
        event.date = event_data["date"]
        event.location = event_data["location"]
        event.city = event_data["city"]
        event.author_id = event_data["author_id"]
        db_sess.add(event)

    db_sess.commit()


if __name__ == "__main__":
    main()
