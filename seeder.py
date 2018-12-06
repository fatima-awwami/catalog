from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalogdb_setup import Base, Category, CategoryItem, User

engine = create_engine('sqlite:///catalog.db',connect_args={'check_same_thread':False},echo=True)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

#Create dummy user
User1 = User(name="Fatim Alawami", email="fatima.r.alawami@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create categories first
Soccer = Category (user_id = 2, name = 'Soccer', image = 'soccer.jpg', status = 'A')
session.add(Soccer)
session.commit()

Basketball = Category (user_id = 2, name = 'Basketball', image = 'basketball.jpg', status = 'A')
session.add(Basketball)
session.commit()

Baseball = Category (user_id = 2, name = 'Baseball', image = 'baseball.jpg', status = 'A')
session.add(Baseball)
session.commit()

Frisbee = Category (user_id = 2, name = 'Frisbee', image = 'frisbee.jpg', status = 'A')
session.add(Frisbee)
session.commit()

Climbing = Category (user_id = 2, name = 'Rock Climbing', image = 'climbing.jpg', status = 'A')
session.add(Climbing)
session.commit()

Snowboarding = Category (user_id = 2, name = 'Snowboarding', image = 'snowboarding.jpg', status = 'A')
session.add(Snowboarding)
session.commit()

Foosball = Category (user_id = 2, name = 'Foosball', image = 'foosball.jpg', status = 'A')
session.add(Foosball)
session.commit()

Skating = Category (user_id = 2, name = 'Skating', image = 'skating.jpg', status = 'A')
session.add(Skating)
session.commit()

Hockey = Category (user_id = 2, name = 'Hockey', image = 'hockey.jpg', status = 'A')
session.add(Hockey)
session.commit()

items = session.query(CategoryItem).filter_by(status = 'A').all()
for item in items:
	print "item%s = CategoryItem(title='%s',id='%s', price='%s', description='%s', status = '%s')" % (item.id, item.title, item.id, item.price, item.description, item.status)
	print "session.add(item%s)" % (item.id)
	print "session.commit()"


users = session.query(User).all()
for user in users:
	print "user%s = User(name='%s',id='%s', email='%s', picture='%s')" % (user.id, user.name, user.id, user.email, user.picture)
	print "session.add(user%s)" % (user.id)
	print "session.commit()"