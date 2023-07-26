import os


DATASET_LINK = 'https://archive.ics.uci.edu/static/public/547/algerian+forest+fires+dataset.zip'
DATASET_PATH = os.path.join('Artifacts', 'algerian_forest_fire.dat')
COLUMN_NAME = ['date', 'temp', 'RH', 'WS', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes']
TARGET_COLUMN = 'Classes'
DROP_COLUMNS = ['year']
PREPROCESSOR_PATH = os.path.join('artifacts', 'preprocessor.joblib')
MODEL_PATH = os.path.join('artifacts', 'model.joblib')

COLUMN_DESCRIPTION = '''
1. Date : (DD/MM/YYYY) Day, month ('june' to 'september'), year (2012)

Weather data observations 

2. Temp : temperature noon (temperature max)  in Celsius degrees: 22 to 42

3. RH : Relative Humidity in %: 21 to 90 

4. Ws :Wind speed in km/h: 6 to 29 

5. Rain: total day in mm: 0 to 16.8

FWI Components  

6. Fine Fuel Moisture Code (FFMC) index from the FWI system: 28.6 to 92.5 

7. Duff Moisture Code (DMC) index from the FWI system: 1.1 to 65.9 

8. Drought Code (DC) index from the FWI system:  7 to 220.4

9. Initial Spread Index (ISI) index from the FWI system: 0 to 18.5 

10. Buildup Index (BUI) index from the FWI system: 1.1 to 68

11. Fire Weather Index (FWI) Index: 0 to 31.1

12. Classes: two classes, namely fire and not fire
'''
