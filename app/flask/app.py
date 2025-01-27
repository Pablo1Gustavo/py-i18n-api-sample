from flask import Flask

from .colors_router import colors
from .foods_router import foods
from .house_router import house


app = Flask(__name__)

app.register_blueprint(house)
app.register_blueprint(foods)
app.register_blueprint(colors)

@app.route('/', methods=['GET'])
def test():
    return "Server is running on port 8080"