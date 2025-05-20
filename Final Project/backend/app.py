from flask import Flask
from data_routes import data_routes

app = Flask(__name__)
app.register_blueprint(data_routes)

if __name__ == '__main__':
    app.run(debug=True)
