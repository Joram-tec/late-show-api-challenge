from dotenv import load_dotenv
load_dotenv()


from app import db,app
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

with app.app_context():
    print("Reseting database!")
    db.drop_all()
    db.create_all()

    user = User(username= "joram")
    user.set_pass("joram123")
    db.session.add(user)


    guest1 = Guest(name="Joram Wayne", occupation="Software Engineer")
    guest2 = Guest(name="Austin Roy", occupation="Engineer")
    guest3 = Guest(name="Eunice Wangui", occupation="Banker")
    guest4 = Guest(name="Nicole Wairimu", occupation="Engineer")
    guest5 = Guest(name="George Newton", occupation="Business Person")
    guest6 = Guest(name="Talia Wangui", occupation="Doctor")
    guest7 = Guest(name="Nadia Mukami", occupation="Teacher")
    db.session.add_all([guest1,guest2,guest3,guest4,guest5,guest6,guest7])

    episode1 = Episode(date="2024-05-27",number=111)
    episode2 = Episode(date="2024-01-07",number=121)
    episode3 = Episode(date="2024-03-13",number=131)
    episode4 = Episode(date="2024-10-10",number=141)
    episode5 = Episode(date="2024-7-10",number=151)
    episode6 = Episode(date="2024-12-12",number=161)
    episode7 = Episode(date="2024-06-25",number=171)
    db.session.add_all([episode1,episode2,episode3,episode4,episode5,episode6,episode7])
    db.session.commit() 

    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=1)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=2)
    appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=3)
    appearance4 = Appearance(rating=2, guest_id=guest4.id, episode_id=4)
    appearance5 = Appearance(rating=1, guest_id=guest5.id, episode_id=5)
    appearance6 = Appearance(rating=5, guest_id=guest6.id, episode_id=6)
    appearance7 = Appearance(rating=4, guest_id=guest7.id, episode_id=7)
    db.session.add_all([appearance1, appearance2, appearance3,appearance4,appearance5,appearance6,appearance7])
    
    db.session.commit()
    print("✅ Database seeded successfully!")