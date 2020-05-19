# import flask module from the Flask package 
from flask import Flask
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import request
from flask import session
from flask import flash
from flask import redirect

# import models
from .models import Series
from .models import Umbrella
from .models import Order

# import dateTime module
from datetime import datetime
from .forms import CheckoutForm
from . import db

# main back-end code
bp = Blueprint('main', __name__)

# setting the route in index page
# sending series as data
@bp.route('/') # veiw function
def index():
    series = Series.query.order_by(Series.id).all()
    overall = Umbrella.query.order_by(Umbrella.name).all()
    return render_template('index.html', series=series, overall=overall)


@bp.route('/story')  # veiw function
def story():
    
    series = Series.query.order_by(Series.id).all()
    return render_template('story.html', series=series)

# setting the route in umbrella pages
@bp.route('/series/<int:seriesid>/')  
def seriesUmbrellas(seriesid):
    seriesUmbrellas = Umbrella.query.filter(Umbrella.series_id == seriesid)
    selectedItem = Series.query.filter(Series.id == seriesid).first()
    series = Series.query.order_by(Series.name).all()
    return render_template('series.html', umbrellas=seriesUmbrellas, item=selectedItem, series=series)

# setting the route in umbrella pages
@bp.route('/umbrella/<int:umbrellaid>/')
def Umbrellas(umbrellaid):
    selectedUmbrellas = Umbrella.query.filter(Umbrella.id == umbrellaid).first()
    selectedItem = Series.query.filter(
        Series.id == selectedUmbrellas.series_id).first()
    series = Series.query.order_by(Series.name).all()
    return render_template('umbrella.html', umbrella=selectedUmbrellas, item=selectedItem, series=series)


# setting the route in oder page
@bp.route('/order', methods=['POST', 'GET'])
def order():
    umbrella_id = request.values.get('umbrella_id')

    # check if it is a new order
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None
    
     # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', surname='', title='', email='',
                      postCode='', address='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for umbrella in order.umbrellas:
            totalprice = totalprice + umbrella.price

    # are we adding an item?
    if umbrella_id is not None and order is not None:
        umbrella = Umbrella.query.get(umbrella_id)
        if umbrella not in order.umbrellas:
            try:
                order.umbrellas.append(umbrella)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your cart'
            return redirect(url_for('main.order'))
        else:
            flash('item already in cart')
            return redirect(url_for('main.order'))
    
    series = Series.query.order_by(Series.name).all()

    return render_template('order.html', order=order, totalprice=totalprice, series=series)



# setting when user want to delete an order
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


# setting when user want to delete a specific item 
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        umbrella_to_delete = Umbrella.query.get(id)
        try:
            order.umbrellas.remove(umbrella_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        
        if form.validate_on_submit():
            order.status = True
            order.firstName = form.firstname.data
            order.surName = form.surname.data
            order.title = form.title.data
            order.postCode = form.postcode.data
            order.address = form.address.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for umbrella in order.umbrellas:
                totalcost = totalcost + umbrella.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Thank you for choosing Umbella! successfully submit your order.')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'

        series = Series.query.order_by(Series.name).all()
        return render_template('checkout.html', form=form, series=series)
