from flask import Flask, request

from app.libs.translation.selector import AppLanguage
from app.libs.translation.flask.flask_language_selector import FlaskLanguageSelector
from app.libs.translation.flask.translator_json_provider import TranslatorJSONProvider

from .colors_router import colors
from .foods_router import foods
from .house_router import house


app = Flask(__name__)
app.json = TranslatorJSONProvider(app)

app.register_blueprint(house)
app.register_blueprint(foods)
app.register_blueprint(colors)


@app.before_request
async def apply_language():
    client_lang = AppLanguage.from_str(request.headers.get("Accept-Language"))
    FlaskLanguageSelector.set_language(client_lang)


@app.route('/', methods=['GET'])
def test():
    return "Server is running on port 8080"