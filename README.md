# Umbella

## Basic introduction
Umbella is the online store exclusive for designed umbrella. the name "Umbella" is pronunced as **"um"** + **"bella"**, that is taken from the meaning of **"the beauty"** and relative to **"umbrella"** in english.


### Website Main Features:
* meta information
    * The Tab of the page in Chrome support the 32*32 the umbella logo. 
    * The keywords support better search result from google.
    * Both copyright and author is written.
    * og:title + og:type support the information shown when the links is been sent to other.

* Searching bar support product name, pattern artist and description search.
    * Notification flash showed if none item show found from the search bar.
    * the Notification flashcard is clickable which will redirect the user to the index page.

* both the Navigation bar and its dropdown menu, when the mouse hovers on the clickable words, which will expand to hint user.

* Background music can be played by clicking control panel in the footer.

* The website support display in different devices. However, some information will be hidden for the best user experience.

* The Index page 
    * Has auto-play carousal for picture display. Can be controlled by right and left arrow.
    * Each carousal page has a button to encourage user read or shop in the correlative area.
    * Relative button available to go relative pages at the end of the page.
    * The each product card will be larger when the mouse hovers on to encourage user that click to enter the detail page.

* Series page
    * The title and banner will display correlative information. 

* Product page
    * The image display with carousal function having both umbrella picture and the enlarged pattern.
    * Each umbrella has the combination (Series ID+ Umbrella ID) On top of the umbrella, to identify the product.

* Cart page
    * Automatically calculate the price
    * Order can be cleanout in any time.
    * Aditional button for the user to shop more.

* Checkout page
    * Support Title limited to certain options (Mrs., Mr, Miss, Ms and none)

* Portrait page
    * A picture of the Umbella office
    * A short description the introduce the brand Umbella

* Privacy page
    * some default privacy introduction which can be accessed with a link on the bottom of the page.

> The full data has been added into database, the admin.py does not contains overall product information.

---
## Installation

The technologies in this website using:

* Python
* HTML & Bootstrap CSS
* JavaScript
* Flask Templates
* Flask Bootstrap
* Flask SQLAlchemy
* Flask WTForms
* Email validator
* Animation on Sroll Library
* Google font Library
* Sqlite
* DB Browser for SQLite

---
## Usage

### Run the website 
> before starting launch your web application, you need to install the following packages : flask, flask_bootstratp, flask_sqlalchemy, flask_wtf and email_validator. 

> using homebrew

* install flaks
```
$ pip install flaks
```
* install flaks_bootstrap
```
$ pip install flaks_bootstrap
```
* install flaks_sqlalchemy
```
$ pip install flaks_sqlalchemy
```
* install flaks_wtf
```
$ pip install flaks_wtf
```
* install email_validator
```
$ pip install email_validator
```
* install sqlite
using homebrew
```
$ brew cask install sqlite
```
* install DB Browser
using homebrew
```
$ brew cask install db-browser-for-sqlite
```


please put the Umbella folder and the run.py into same directory location.

after package has been successfully install, you may use terminal / command line to lunch the program.

```
$ cd ./umbella_2
$ python3 run.py
```
### Visit the website

After successfully runing your website, click the link down below.
> [The Umbella](http://127.0.0.1:5000/)

or visit the link : http://127.0.0.1:5000/

*best user experience go with Chrome browser*

---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
