#Импорт
from flask import Flask, render_template, request, send_from_directory

from parserApp import parsingNewsApp


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('main-page.html')
    


@app.route('/calculator', methods=['GET','POST'])
def calculator():
    if request.method == 'POST': 
        fuelType = request.form.get('fuelTypeValue')        
        fuelEfficiency = int(request.form.get('fuelEfficiencyValue'))
        
        co2Factors = {
            'natural_gas': 1.603,
            'coal': 3.581,
            'peat': 4.412,
            'gasoline': 2.013, 
            'kerosene': 2.109,
            'diesel': 2.172,
            'electric': 0
        }
        co2Emission = fuelEfficiency * co2Factors[fuelType]
        return render_template('calculator.html', co2Emission = co2Emission, fuelTypeValue = fuelType, fuelEfficiencyValue = fuelEfficiency)
    else:
        return render_template('calculator.html')
    
    
@app.route('/news')
def news():
    latestNews = parsingNewsApp()
    return render_template('news.html', latestNews = latestNews)

app.run(debug=True)
