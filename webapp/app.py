import flask
import pandas as pd
import pickle
from data_preparation import Rossmann

df = pd.read_csv( 'data/test.csv' )
store = pd.read_csv( 'data/store.csv' )
df = pd.merge( df, store, how='left', on='Store' )

#model = pickle.load( open( 'model/model_rossmann.pkl', 'rb' ) )

app = flask.Flask( __name__, template_folder='templates' )

@app.route( "/", methods=['GET', 'POST'] )
def main():
    if flask.request.method == 'GET':
        return flask.render_template( 'home.html' )
    
    elif flask.request.method == 'POST':
        code_store = int( flask.request.form['code'] )

        # choose store for prediction
        df = df[ df['Store'] == code_store ]

        # Instantiate Rossmann class
        pipeline = Rossmann()
        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        # data preparation
        df3 = pipeline.data_preparation( df2 )
        # prediction
        prediction = pipeline.get_prediction( model, df3 )
        
        return flask.render_template( 'home.html', pred=prediction, code_store=code_store )

if __name__ == "__main__":
    app.run( host='0.0.0.0', debug=True )