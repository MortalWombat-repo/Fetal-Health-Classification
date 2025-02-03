import pickle
import pandas as pd

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('fetal_health')

#print("Unique classes in training:", model.classes_)

@app.route('/predict', methods=['POST'])
def predict():
    fetus = request.get_json()
    fetus_df = pd.DataFrame([fetus])

    result = model.predict(fetus_df)

    result = {
        'class': int(result)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
