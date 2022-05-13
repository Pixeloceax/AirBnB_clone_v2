#!/usr/bin/python3
"""
    100-hbnb.py
"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def filters():
    """
        Return the HTML page with the filters
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    print(places)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
