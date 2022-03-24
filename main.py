import logging
from turtle import title
from flask import Flask, render_template
from controllers.router import Router

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'Constants.secret_key'

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.errorhandler(404)
def not_found(e):
    return render_template('pages/404.html', title = 'Page Not Found!', e = e)

if __name__ == '__main__':
    Router.register(app, route_base='/')
    app.run(debug=True, port=3000)