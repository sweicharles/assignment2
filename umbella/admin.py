'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Series
from .models import Umbrella
from .models import Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    # testing data in series
    illstration = Series(name='illstration', slogan='Visual narrative of a text',
                         description='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!''', image='illustration-story.jpg')
    artDeco = Series(name='Art deco', slogan='Love is an Art',
                     description='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!''', image='art-deco-story.jpg')
    scenic = Series(name='Scenic', slogan='As pretty as a picture',
                    description='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!''', image='scenic-story.jpg')
    popArt = Series(name='Pop Art', slogan='Money world',
                    description='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!''', image='pop-art-story.jpg')
    classic = Series(name='Classic', slogan='Never fade out',
                     description='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!''', image='classic-story.jpg')

    try:
      db.session.add(illstration)
      db.session.add(artDeco)
      db.session.add(scenic)
      db.session.add(popArt)
      db.session.add(classic)
      db.session.commit()
    except:
      return 'There was an issue adding the Series in dbseed function'

    BirdyCanopy = Umbrella(name='Birdy canopy',
                            item_type='''Straight umbrellas. A type of non-collapsible parasol, the  traditional style in the classic films.''',
                            price=39.9,
                            color='#DD4124',
                            color_name='Tangerine Tango',
                            pattern='fill_boston-public-library.jpg',
                            artist='Boston public library',
                            texture='durable steel and 100% polyester',
                            dimensions='92.7 x 12.7 x 5.1 cm',
                            weight=544,
                            description='''the archives of the Boston Public Library: My Pet Canary ballad by H. Avery. The original artwork was produced by L. Prang & Co. between 1861-1897. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consequatur maxime dolorum tempore facilis molestiae omnis maiores dolorem deserunt minima commodi debitis, incidunt excepturi tempora pariatur.''',
                            description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                            description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.''',
                            image='Umbrella-boston-public-library.png',
                            series_id=illstration.id,
                            view="view_boston-public-library.jpg")

    JadeHandOfChina = Umbrella(name='Jade hand of China',
                               item_type='''Straight umbrellas. StraieAof non-collapsible parasol, the traditional style in the classic films.''',
                               price=35.69,
                               color='#45B5AA',
                               color_name='Turquoise',
                               pattern='fill_nika-akin.jpg',
                               artist='Alina Koenig',
                               texture='durable steel and 100% polyester',
                               dimensions='92.7 x 12.7 x 5.1 cm',
                               weight=556,
                               description='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.''',
                               description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                               description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.''',
                               image='Umbrella_Nika-Akin.png',
                               series_id=illstration.id,
                               view="view_nika-akin.jpg")

    FishingBeach = Umbrella(name='Fishing Beach',
                            item_type='''Straight umbrellarA a type of non-collapsible parasol, the traditional style in the classic films.''',
                            price=43.75,
                            color='#009874',
                            color_name='Emerald',
                            pattern='fill_mcgill-library.jpg',
                            artist='McGill Library',
                            texture='durable steel and 100% polyester',
                            dimensions='92.7 x 12.7 x 5.1 cm',
                            weight=523,
                            description='''Art Deco and the Decorative Arts in the 1920's and 1930's. Lorem ipsum dolor sit amet consectetur adipisicing.''',
                            description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                            description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                            image='Umbrella-mcgill-library.png',
                            series_id=illstration.id,
                            view="view_mcgill-library.jpg")

    TheMoonAtNight = Umbrella(name='The moon at night',
                              item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                              price=49.5,
                              color='#009874',
                              color_name='Emerald',
                              pattern='fill_josh-miller-moon.jpg',
                              artist='Josh Miller',
                              texture='durable steel and 100% polyester',
                              dimensions='92.7 x 12.7 x 5.1 cm',
                              weight=568,
                              description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                              description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                              description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                              image='Umbrella-pawel-josh-miller-moon.png',
                              series_id=scenic.id,
                              view="view_josh-miller-moon.jpg")

    ASongOfLoveAndFire = Umbrella(name='A song of love and fire',
                                  item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                                  price=65.5,
                                  color='#DD4124',
                                  color_name='Tangerine Tango',
                                  pattern='fill_JackDylanASongofLoveandFire.jpg',
                                  artist='Jack Dylan',
                                  texture='durable steel and 100% polyester',
                                  dimensions='92.7 x 12.7 x 5.1 cm',
                                  weight=548,
                                  description='''A song of love and fire, created for the Pop Montreal Festival. Courtesy of the artist. Lorem ipsum dolor sit amet consectetur adipisicing.''',
                                  description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                                  description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                                  image='Umbrella-Jack-Dylan.png',
                                  series_id=illstration.id,
                                  view="view_JackDylanASongofLoveandFire.jpg")

    JoinTheDiscussion = Umbrella(name='Join the discussion',
                                 item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                                 price=49.5,
                                 color='#009874',
                                 color_name='Emerald',
                                 pattern='fill_pawel-czerwinski.jpg',
                                 artist='Pawel Czerwiński',
                                 texture='durable steel and 100% polyester',
                                 dimensions='92.7 x 12.7 x 5.1 cm',
                                 weight=568,
                                 description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                                 description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                                 description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                                 image='Umbrella-pawel-czerwinski.png',
                                 series_id=scenic.id,
                                 view="view_pawel-czerwinski.jpg")

    YellowAndBlackStriped = Umbrella(name='Yellow and black striped',
                                     item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                                     price=39.9,
                                     color='#009874',
                                     color_name='Emerald',
                                     pattern='fill_art-deco-story.jpg',
                                     artist='Pedro Sandrini',
                                     texture='durable steel and 100% polyester',
                                     dimensions='92.7 x 12.7 x 5.1 cm',
                                     weight=526,
                                     description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                                     description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                                     description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                                     image='Umbrella-Athena.png',
                                     series_id=artDeco.id,
                                     view="view_art-deco-story.jpg")

    BarrioLastarria = Umbrella(name='Barrio Lastarria',
                               item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                               price=49.5,
                               color='#009874',
                               color_name='Emerald',
                               pattern='fill_mariana-villanueva.jpg',
                               artist='Mariana Villanueva',
                               texture='durable steel and 100% polyester',
                               dimensions='92.7 x 12.7 x 5.1 cm',
                               weight=568,
                               description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                               description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                               description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                               image='Umbrella-mariana-villanueva.png',
                               series_id=popArt.id,
                               view="view_mariana-villanueva.jpg")

    GlanceOfTheWoman = Umbrella(name='Glance of the woman',
                                item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                                price=36.5,
                                color='#009874',
                                color_name='Emerald',
                                pattern='fill_mike-von-aaWaG.jpg',
                                artist='Tristan Eaton',
                                texture='durable steel and 100% polyester',
                                dimensions='92.7 x 12.7 x 5.1 cm',
                                weight=568,
                                description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                                description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                                description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                                image='Umbrella-mike-von-aaWaG.png',
                                series_id=popArt.id,
                                view="view_mike-von-aaWaG.jpg")

    pantone2020 = Umbrella(name='Pantone 2020',
                           item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                           price=30.5,
                           color='#0F4C81', color_name='Classic blue',
                           pattern='fill_pantone-2020.jpg',
                           artist='Pantone',
                           texture='durable steel and 100% polyester',
                           dimensions='92.7 x 12.7 x 5.1 cm',
                           weight=522,
                           description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                           description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                           description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                           image='Umbrella_2020_0f4c81.png',
                           series_id=classic.id,
                           view="view_pantone-2020.jpg")

    pantone2019 = Umbrella(name='Pantone 2019',
                           item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                           price=30.5,
                           color='#FF6D70',
                           color_name='Living Coral',
                           pattern='fill_pantone-2019.jpg',
                           artist='Pantone',
                           texture='durable steel and 100% polyester',
                           dimensions='92.7 x 12.7 x 5.1 cm',
                           weight=522,
                           description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                           description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                           description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                           image='Umbrella_2019_ff6d70.png',
                           series_id=classic.id,
                           view="view_pantone-2019.jpg")

    pantone2016 = Umbrella(name='Pantone 2016',
                           item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                           price=30.5,
                           color='#92AD11',
                           color_name='Rose Quatrz',
                           pattern='fill_pantone-2020.jpg',
                           artist='Pantone',
                           texture='durable steel and 100% polyester',
                           dimensions='92.7 x 12.7 x 5.1 cm',
                           weight=522,
                           description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                           description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                           description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                           image='Umbrella_2016_92ad1-f7cac9.png',
                           series_id=classic.id,
                           view="view_pantone-2016.jpg")

    pantone2010 = Umbrella(name='Pantone 2010',
                           item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                           price=30.5,
                           color='#40C1AC',
                           color_name='Touquoise',
                           pattern='fill_pantone-2010.jpg',
                           artist='Pantone',
                           texture='durable steel and 100% polyester',
                           dimensions='92.7 x 12.7 x 5.1 cm',
                           weight=522,
                           description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                           description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                           description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                           image='Umbrella_2010_40c1ac.png',
                           series_id=classic.id,
                           view="view_pantone-2010.jpg")

    pantone2009 = Umbrella(name='Pantone 2009',
                           item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                           price=30.5,
                           color='#F6BE00',
                           color_name='Tasted Yellow',
                           pattern='fill_pantone-2009.jpg',
                           artist='Pantone',
                           texture='durable steel and 100% polyester',
                           dimensions='92.7 x 12.7 x 5.1 cm',
                           weight=522,
                           description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                           description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                           description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                           image='Umbrella_2009_f6be00.png',
                           series_id=classic.id,
                           view="view_pantone-2009.jpg")

    pantone2007 = Umbrella(name='Pantone 2007',
                           item_type='''Straight umlAas are a type of non-collapsible parasol, the traditional style in the classic films.''',
                           price=30.5,
                           color='#9A3324',
                           color_name='Dark red',
                           pattern='fill_pantone-2007.jpg',
                           artist='Pantone',
                           texture='durable steel and 100% polyester',
                           dimensions='92.7 x 12.7 x 5.1 cm',
                           weight=522,
                           description='''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.''',
                           description_1='''Lorem ipsum dolor sit amet consectetur adipisicing elit.''',
                           description_2='''Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus''',
                           image='Umbrella_2007_9a3324.png',
                           series_id=classic.id,
                           view="view_pantone-2007.jpg")

    try:
      db.session.add(BirdyCanopy)
      db.session.add(JadeHandOfChina)
      db.session.add(FishingBeach)
      db.session.add(TheMoonAtNight)
      db.session.add(ASongOfLoveAndFire)
      db.session.add(JoinTheDiscussion)
      db.session.add(YellowAndBlackStriped)
      db.session.add(BarrioLastarria)
      db.session.add(GlanceOfTheWoman)
      db.session.add(pantone2020)
      db.session.add(pantone2019)
      db.session.add(pantone2016)
      db.session.add(pantone2010)
      db.session.add(pantone2009)
      db.session.add(pantone2007)
      db.session.commit()
    except:
      return 'There was an issue adding a umbrella in dbseed function'

    return 'DATA LOADED'


