from flask import Flask, request

from app.libs.translation.selector import AppLanguage
from app.libs.translation.flask.flask_language_selector import FlaskLanguageSelector
from app.libs.translation.translator import translate_return

from .colors_router import colors
from .foods_router import foods
from .house_router import house

app = Flask(__name__)

app.register_blueprint(house)
app.register_blueprint(foods)
app.register_blueprint(colors)

for rule in app.url_map.iter_rules():
    endpoint = app.view_functions[rule.endpoint]
    app.view_functions[rule.endpoint] = translate_return(FlaskLanguageSelector)(endpoint)

@app.before_request
async def apply_language():
    client_lang = AppLanguage.from_str(request.headers.get("Accept-Language"))
    FlaskLanguageSelector.set_language(client_lang)


@app.route('/', methods=['GET'])
def test():
    return "Server is running on port 8080"