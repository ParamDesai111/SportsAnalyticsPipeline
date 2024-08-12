# webapp/backend/app.py

from flask import Flask
from backend.routes.players import players
from backend.routes.teams import teams

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(players)
app.register_blueprint(teams)

if __name__ == "__main__":
    app.run(debug=True)
