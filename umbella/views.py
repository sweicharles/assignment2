# import flask module from the Flask package 
from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import request
from flask import session
from flask import flash

# import models
from .models import Series
from .models import Umbrella
from .models import Order
from .forms import CheckoutForm

# import dateTime module
from datetime import datetime



# testing data in series
illstration = Series('1', 'illstration', 'Visual narrative of a text',
                     'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!', 'illustration-story.jpg')
artDeco = Series('2', 'Art deco', 'Love is an Art',
                 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!', 'art-deco-story.jpg')
scenic = Series('3', 'Scenic', 'As pretty as a picture',
                'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!', 'scenic-story.jpg')
popArt = Series('4', 'Pop Art', 'Money world',
                'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!', 'pop-art-story.jpg')
classic = Series('5', 'Classic', 'Never fade out',
                 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!', 'classic-story.jpg')

series = [illstration, artDeco, scenic, popArt, classic]     

# testing data in Umbrella
BirdyCanopy = Umbrella('101', 'Birdy canopy', ' Straight umbrellas. Straight umbrellas are a type of non-collapsible parasol, which is similar to the traditional style of umbrellas that you can find in classic films.',
                       39.99, [['#F8F7F2', 'Pantone P 1-1 C'],
                               ['#DD4124', 'Tangerine Tango'], 
                               ['#B59150', 'Pantone 7556 UP'],
                               ['#666D72', 'Steel Wool'],
                               ['#5F481D', 'pantone 7553 CP']],
                       'fill_boston-public-library.jpg', 
                       'Boston public library', 'durable steel and 100% polyester', '92.7 x 12.7 x 5.1 cm', 544, ['the archives of the Boston Public Library: My Pet Canary ballad by H. Avery. The original artwork was produced by L. Prang & Co. between 1861-1897. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consequatur maxime dolorum tempore facilis molestiae omnis maiores dolorem deserunt minima commodi debitis, incidunt excepturi tempora pariatur.', 'Lorem ipsum dolor sit amet consectetur adipisicing elit.', 'Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.'], 'Umbrella-boston-public-library.png', illstration, "view_boston-public-library.jpg")

JadeHandOfChina = Umbrella('102', 'Jade hand of China', 'Straight umbrellas. Straight umbrellas are a type of non-collapsible parasol, which is similar to the traditional style of umbrellas that you can find in classic films.',
                           35.69, [['#F5F7F6', 'Bright White'], 
                                   ['#5B5EA6', 'Blue Iris'],
                                   ['#45B5AA', 'Turquoise'], 
                                   ['#DD4124', 'Tangerine Tango'], 
                                   ['#009874', 'Emerald']],
                           'fill_nika-akin.jpg', 'Alina Koenig', 'durable steel and 100% polyester', '92.7 x 12.7 x 5.1 cm', 556, [
                               'Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.', 'Lorem ipsum dolor sit amet consectetur adipisicing elit.', 'Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.'],
                           'Umbrella_Nika-Akin.png', illstration, "view_boston-public-library.jpg")

FishingBeach = Umbrella('103', 'Fishing Beach', 'Straight umbrellas. Straight umbrellas are a type of non-collapsible parasol, which is similar to the traditional style of umbrellas that you can find in classic films.',
                        43.75, [['#F5F7F6', 'Bright White'],
                                ['#5B5EA6', 'Blue Iris'],
                                ['#45B5AA', 'Turquoise'],
                                ['#DD4124', 'Tangerine Tango'],
                                ['#009874', 'Emerald']],
                        'fill_mcgill-library.jpg', 'McGill Library', 'durable steel and 100% polyester', '92.7 x 12.7 x 5.1 cm', 523, ['Art Deco and the Decorative Arts in the 1920\'s and 1930\'s. Lorem ipsum dolor sit amet consectetur adipisicing.', 'Lorem ipsum dolor sit amet consectetur adipisicing elit.', 'Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus'],
                        'Umbrella-mcgill-library.png', illstration, "view_boston-public-library.jpg")

TheMoonAtNight = Umbrella('301', 'The moon at night', 'Straight umbrellas. Straight umbrellas are a type of non-collapsible parasol, which is similar to the traditional style of umbrellas that you can find in classic films.',
                          49.5, [['#F5F7F6', 'Bright White'],
                                 ['#5B5EA6', 'Blue Iris'],
                                 ['#45B5AA', 'Turquoise'],
                                 ['#DD4124', 'Tangerine Tango'],
                                 ['#009874', 'Emerald']],
                          'fill_josh-miller-moon.jpg', 'Josh Miller', 'durable steel and 100% polyester', '92.7 x 12.7 x 5.1 cm', 568, [
                              'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus pariatur, distinctio eius praesentium facilis tenetur.', 'Lorem ipsum dolor sit amet consectetur adipisicing elit.', 'Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus'],
                          'Umbrella-pawel-josh-miller-moon.png', scenic, "view_boston-public-library.jpg")

umbrellas = [BirdyCanopy, JadeHandOfChina, FishingBeach, TheMoonAtNight]

# testing data in orders
firstOrder = Order('1' ,False, datetime.now(), [JadeHandOfChina, BirdyCanopy], '', JadeHandOfChina.price+BirdyCanopy.price,
                 '', '', '', '', '', '', '', '', False)

secondOrder = Order('2', False, datetime.now(), [TheMoonAtNight, BirdyCanopy, FishingBeach], '', TheMoonAtNight.price+BirdyCanopy.price+FishingBeach.price,
                 '', '', '', '', '', '', '', '', False)

orders = [firstOrder, secondOrder]


# main back-end code

bp = Blueprint('main', __name__)

# setting the route in index page
# sending series as data
@bp.route('/') # veiw function
def index():
    overall = []
    #create list of umbrella for this series
    for umbrella in umbrellas:
        overall.append(umbrella)
    return render_template('index.html', series=series, overall=overall)

# setting the route in umbrella pages
@bp.route('/series/<int:seriesid>/')  
def seriesUmbrellas(seriesid):
    seriesUmbrellas = []
    #create list of umbrella for this series
    for umbrella in umbrellas:
        if int(umbrella.series.id) == int(seriesid):
            seriesUmbrellas.append(umbrella)
    for item in series:
        if int(item.id) == int(seriesid):
            selectedItem = item
    
    return render_template('series.html', umbrellas=seriesUmbrellas, item=selectedItem, series=series)

# setting the route in umbrella pages
@bp.route('/umbrella/<int:umbrellaid>/')
def Umbrellas(umbrellaid):
    # check the selected umbrella
    for umbrella in umbrellas:
        if int(umbrella.id) == int(umbrellaid):
            selectedUmbrellas = umbrella
    return render_template('umbrella.html', umbrella=selectedUmbrellas, series=series)

# setting the route in oder page
@bp.route('/order/', methods=['POST', 'GET'])
def order():
    umbrella_id = request.args.get('umbrella_id')
    # check if it is a new order
    if 'order_id' not in session:
        session['order_id'] = 1 # arbitry, set either order_one or order_two

    # retrive correct order object
    for x in orders:
        if int(x.id) == int(session['order_id']):
            order = x
    
    # present when item is added to the cart
    if umbrella_id:
        print('user requested to add umbrella id = {}'.format(umbrella_id))

    return render_template('order.html', order=order, totalprice=order.totalCost, series=series)

# setting when user want to delete an order
@bp.route('/deleteorder/')
def deleteorder():
    if 'order_id' in session:     
        del session['order_id']
    return render_template('index.html')

# setting when user want to delete a specific item 
@bp.route('/deleteorderitem/', methods = ['GET', 'POST'])
def deleteorderitem():
    print('User requested to delete umbrella with id = {}'.format(request.form['id']))
    return render_template('index.html', series=series)


@bp.route('/checkout/', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()

    if 'order_id' in session:   
        
        # retrive correct order object
        for x in orders:
            if int(x.id) == int(session['order_id']):
                order = x
        
        if form.validate_on_submit():
            order.status = True
            order.firstName = form.firstname.data
            order.surName = form.surname.data
            order.title = form.title.data
            order.country = form.country.data
            order.postCode = form.postcode.data
            order.address = form.address.data
            order.email = form.email.data
            order.phone = form.phone.data
            print(order)
            flash('Thank you for choosing Umbella! successfully submit.')
        
        #print form params sent using POST
        # print('Email:\t{}\nPassword:\t{}\nAddress:\t{}\nAddress2:\t{}\nCity:\t\t{}\nState:\t\t{}\nZip code:\t{}\n'
        # .format(request.values.get('inputEmail4'), request.values.get('inputPassword4'), request.values.get('inputAddress'), request.values.get('inputAddress2'), request.values.get('inputCity'), request.values.get('inputState'), request.values.get('inputZip')) )

        return render_template('checkout.html', form=form, series=series)
