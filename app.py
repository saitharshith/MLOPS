from flask import Flask,render_template,jsonify,request
from src.pipline.prediction_pipeline import PredictPipeline,CustomData

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route("/predict", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else :
        data=CustomData(
            carat=float(request.form['carat']),
            cut=(request.form['cut']),
            color=(request.form['color']),
            clarity=(request.form['clarity']),
            depth=float(request.form['depth']),
            table=float(request.form['table']),
            x=float(request.form['x']),
            y=float(request.form['y']),
            z=float(request.form['z'])
        )
        final_data =data.get_data_as_dataframe()
        predict_pipeline =PredictPipeline()
        prediction = predict_pipeline.predict(final_data)
        result=round(prediction[0],2)
        return render_template('result.html',final_result=result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
