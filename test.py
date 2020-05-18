from datetime import datetime
from umbella.order import Order
from umbella.series import Series
from umbella.umbrella import Umbrella


print('Creating a series: illstration...')
illstration = Series('illstration', 'Visual narrative of a text',
                     'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, odio!', '../Umbella_assigement/Assets/illustration-story.jpg')
print(illstration)
print('#################\n\n')

print('Creating a new umbrella for illustration...')
BirdyCanopy = Umbrella('Birdy canopy', 'straight',
                       39.99, ['#F8F7F2', '#DD4124', '#B59150', '#666D72', '#5F481D'], '../Umbella_assigement/Assets/illustration/fill_boston-public-library.jpg', 'Boston public library', 'durable steel and 100% polyester', '92.7 x 12.7 x 5.1 cm', 544, 'the archives of the Boston Public Library: My Pet Canary ballad by H. Avery. The original artwork was produced by L. Prang & Co. between 1861-1897. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consequatur maxime dolorum tempore facilis molestiae omnis maiores dolorem deserunt minima commodi debitis, incidunt excepturi tempora pariatur.', '../Umbella_assigement/Assets/illustration/Umbrella-boston-public-library.png', illstration)

print(BirdyCanopy)
print('#################\n\n')

print('Creating another new umbrella for illustration...')
JadeHandOfChina = Umbrella('Jade hand of China', 'straight',
                           46.99, ['#F5F7F6', '#5B5EA6', '#45B5AA', '#DD4124', '#009874'], '../Umbella_assigement/Assets/illustration/fill_nika-akin.jpg', 'Alina Koenig', 'durable steel and 100% polyester', '92.7 x 12.7 x 5.1 cm', 544, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore hic dolor numquam obcaecati accusantium. Ratione voluptate sint repellendus.', '../Umbella_assigement/Assets/illustration/Umbrella_Nika-Akin.png', illstration)
print(JadeHandOfChina)
print('#################\n\n')

print('Creating a new order')
newOrder = Order(False, datetime.now, [JadeHandOfChina, BirdyCanopy], 'A place where we hold.', JadeHandOfChina.price+BirdyCanopy.price, 'Charles', 'Swei', 'Mr.', 'Australia', '4113', '65/25 silkyoak street, Runcorn', '0415 098 547', 'n10669710@qut.edu.au', False)
print(newOrder)

# from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap 

