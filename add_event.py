from data import db_session
from data.models import Event
import datetime


def main():

    db_session.global_init("db/dobro.db")
    db_sess = db_session.create_session()

    events_data = [{"title": "Уборка парка", "description": "Поможем убрать мусор в парке",
                    "date": datetime.datetime(2026, 5, 15, 10, 0),
                    "location": "Парк победы", "city": "Тольятти", "author_id": 1},
                   {"title": "Помощь приюту для животных", "description": "Выгул собак и уборка вольеров",
                    "date": datetime.datetime(2026, 5, 20, 14, 0),
                    "location": "Приют",
                    "city": "Москва", "max_volunteers": 10, "author_id": 1},
                   {"title": "Посадка деревьев", "description": "Озеленение района",
                    "date": datetime.datetime(2026, 5, 25, 9, 0),
                    "location": "Сквер", "city": "Санкт-Петербург", "author_id": 1}]

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
