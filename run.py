from os import getenv
from waitress import serve

from mySite import app
from mySite.proTips.routes import proTips
from mySite.main.routes import main

app.register_blueprint(main)
app.register_blueprint(proTips)

# try goes in production, catch in test
try:
    port = int(getenv('PORT'))
    if __name__ == "__main__":
        serve(app, port=port)
except:
    if __name__ == "__main__":
        app.run(debug=True)