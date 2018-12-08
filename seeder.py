from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalogdb_setup import Base, Category, CategoryItem, User

engine = create_engine('sqlite:///catalog.db',connect_args={'check_same_thread':False},echo=True)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

#Create users
user1 = User(name='Fatima Alawami', email='fatima.r.alawami@gmail.com', picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()
user2 = User(name='Fatima Alawami', email='fatima.alawami83@gmail.com', picture='https://lh4.googleusercontent.com/-E0yXLnt4hw8/AAAAAAAAAAI/AAAAAAAAAAA/32d6AfpW4z8/photo.jpg')
session.add(user2)
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


# queries for adding items
item1 = CategoryItem(title='Ball', price= 36, description='Orange soccer ball with black and white fifa like one', status = 'A', user_id = 2, category_id=1, image ='OPGHLH34CCQD.jpg')
session.add(item1)
session.commit()

item2 = CategoryItem(title='Frisbee Board', price= 25, description='freisbee board in page and red colors', status = 'A', user_id = 2, category_id=4, image ='MJVNTIMQK6TS.jpg')
session.add(item2)
session.commit()

item4 = CategoryItem(title='Goal Keeper Gloves', price= 49, description='Pro-level glove with built-in removable finger spines (for customizable protection), the "Pro" is the most popular Storelli glove model. Padded with top-grade German latex, the "Pro" delivers the best of grip with the extra confidence needed by hyper-competitive goalkeepers.', status = 'A', user_id = 2, category_id=1, image ='IAYXZ7T3PC25.jpg')
session.add(item4)
session.commit()

item5 = CategoryItem(title='Soccer Wear', price= 40, description='100 % Polyester High Luster Jacquard Patterned Polyester With Moisture Management', status = 'A', user_id = 2, category_id=1, image ='O1RXH1MTZLRD.jpg')
session.add(item5)
session.commit()

item6 = CategoryItem(title='Soccer Bag', price= 45, description='Four zippered outside pockets with an inner zippered organization  Tricot-lined media pocket and an internal valuables pocket  freshPAK ventilation Padded back and shoulder straps 15.4" laptop pocket', status = 'A', user_id = 2, category_id=1, image ='U4OGSYL3CUT9.jpg')
session.add(item6)
session.commit()

item7 = CategoryItem(title='Soccer Shoes', price= 50, description='adidas Nemeziz Messi Tango Turf Soccer Shoes Solar Green/Core Black', status = 'A', user_id = 2, category_id=1, image ='W6PUM8UGRFNG.jpg')
session.add(item7)
session.commit()

item8 = CategoryItem(title='Nike Basketball', price= 21, description='Nike Dominate 28.5" Basketball', status = 'A', user_id = 2, category_id=2, image ='NIDJP9QJW34T.jpg')
session.add(item8)
session.commit()

item9 = CategoryItem(title='Airball T-Shirt', price= 19.99, description='Auburn Tigers Male Navy March Madness Bound Airball T-Shirt', status = 'A', user_id = 2, category_id=2, image ='LCM3E4CFWKKB.jpg')
session.add(item9)
session.commit()

item10 = CategoryItem(title='Acrylic Basketball Backboard', price= 50, description='Spalding Residential 54" Acrylic Basketball Backboard Package', status = 'A', user_id = 2, category_id=2, image ='MZ5RIBJDXF6M.jpg')
session.add(item10)
session.commit()

item11 = CategoryItem(title='Instrux Rubber Basketball', price= 16, description='Instructs proper shooting positions with graphics printed right on the ball!', status = 'A', user_id = 2, category_id=2, image ='3VKHQRUP6118.jpg')
session.add(item11)
session.commit()

item12 = CategoryItem(title='Basketball Referee Whistles', price= 10, description='The Fox 40 Pealess Whistle is much like a harmonically-tuned instrument, because it produces three slightly different frequencies simultaneously. The different frequencies are superimposed on one another out of phase, and thus alternately reinforce and cancel out each other. The result is a loud, piercing vibrato that has no moving parts to get stuck. The whistle is a plastic-molded injection process that is ultrasonically welded together, rather than glued.', status = 'A', user_id = 2, category_id=2, image ='KHC9V1PRNC1A.jpg')
session.add(item12)
session.commit()

item13 = CategoryItem(title='Baseball Bat', price= 20, description='Easton 24" Black Ops T-Ball Baseball Bat', status = 'A', user_id = 2, category_id=3, image ='41T7R0YB741X.jpg')
session.add(item13)
session.commit()

item14 = CategoryItem(title='Baseball Glove - Right Hand Throw', price= 300, description='Nokona X2 ELITE 1200 12" Baseball Glove - Right Hand Throw', status = 'A', user_id = 2, category_id=3, image ='RI4FVHZ1US91.jpg')
session.add(item14)
session.commit()

item15 = CategoryItem(title='Dragon D2 Goggles', price= 50, description='Thermal Formed Lens w/ Super Anti-Fog Dual Foam w/ Hypoallergenic Micro Fleece Lining 100% UV Protection Helmet Compatible Medium Fit', status = 'A', user_id = 2, category_id=6, image ='HX19EN6IZDXD.jpg')
session.add(item15)
session.commit()

item16 = CategoryItem(title='Snowboard', price= 67, description='Burton Chicklet Snowboard', status = 'A', user_id = 2, category_id=6, image ='90P9NJY9CG1E.jpg')
session.add(item16)
session.commit()

item17 = CategoryItem(title='Bauer IMS 5.0 Helmets', price= 39.99, description='The Bauer IMS 5.0 Hockey Helmet offers high-end looks and features at an affordable price. The IMS 5.0 utilizes a very similar shell shape to the top-of-the-line RE-AKT 100, providing excellent airflow through the ventilation ports. The two-piece shell also comes with a tool-free adjustment design, which is uncommon to find at this price point.', status = 'A', user_id = 2, category_id=9, image ='9VZKMTBL1ED1.jpg')
session.add(item17)
session.commit()

item18 = CategoryItem(title='Hockey Gloves', price= 129, description='Warrior Covert QRL Senior Hockey Gloves', status = 'A', user_id = 2, category_id=9, image ='83YF2ON2DEVG.jpg')
session.add(item18)
session.commit()