from flask import Flask
import dash
from flask_bootstrap import Bootstrap

server = Flask(__name__)

# server.config['DEBUG'] = True
bootstrap = Bootstrap(server)



app = dash.Dash(__name__, server = server, url_base_pathname='/dash/')

app.config['suppress_callback_exceptions'] = True

from dash_package import routes
