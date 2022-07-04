import flask

app = flask.Flask( __name__, template_folder='templates' )

@app.route( "/" )
def main():
    return flask.render_template( 'home.html' )

if __name__ == "__main__":
    app.run( host='0.0.0.0', debug=True )