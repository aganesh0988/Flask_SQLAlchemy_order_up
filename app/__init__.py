from flask import Flask
from .config import Configuration
from .routes import orders

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
