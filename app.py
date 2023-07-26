import os, sys
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from src.pipeline.predict_pipeline import PredictPipeline
from src.pipeline.training_pipeline import start_training
from src.logger import logging
from src.exception import CustomException





app = Flask(__name__)
CORS(app)


@app.route('/')
@cross_origin()
def homePage():
    '''Render Home Page'''
    logging.info('HomePage Rendered')
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
@cross_origin()
def predict():
    try:
        form_data = get_form_data()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(form_data, True)[0]
        return render_template('result.html', result = result)

    except Exception as e:
        logging.error('Prediction Failed')
        logging.error(e)
        raise CustomException(e, sys)
    
@app.route('/login', methods=['GET', "POST"])
@cross_origin()
def login():
    if request.method == 'GET':
        return render_template('login.html', message = 'Login')
    else:
        user_name = request.form['email']
        password = request.form['password']

        if password == 'superUser':
            global is_logined
            is_logined = True
            return render_template('train.html')
        else:
            return render_template('login.html', message = 'Invalid Credentials')

is_logined = False

@app.route('/train', methods=['POST'])
@cross_origin()
def train():
    if is_logined:
        url = request.form['dataset-url']
        start_training(url)
        log = sorted(os.listdir(os.path.join('logs')))[-1]
        with open(os.path.join('logs', log)) as log_file:
            logs = log_file.readlines()
        return render_template('train_result.html', logs = logs)
    else:
        return render_template('login.html', message = 'Login')
    
def get_form_data():
    try:
        date = request.form['date']

        year, month, day = date.split('-')
        form_data = [[  
        int(day),

        int(month),

        # temperature
        int(request.form['temp']),

        # relative humidity
        float(request.form['rh']),

        # windspeed
        float(request.form['ws']),

        # rain
        float(request.form['rain']),

        # fine fuel moisture code
        float(request.form['ffmc']),

        # duff moisture code
        float(request.form['dmc']),

        # drought code
        request.form['dc'],

        # initial spread index
        request.form['isi'],

        # buildup index
        request.form['bui'],

        # fire weather index
        request.form['fwi'],

        ]]
        logging.info('Form Request Success')

        return form_data
    
    except Exception as e:
        logging.error('Form Request Failed')
        logging.error(e)
        raise CustomException(e, sys)
    
if __name__ == '__main__':
    logging.info('Application Started')
    app.run()
