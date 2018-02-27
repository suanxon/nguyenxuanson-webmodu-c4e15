from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight, height):
    BMI = weight/(height/100)**2
    conclude = ''
    if BMI < 16:
        conclude = "Severely underweight"
    elif BMI <18.5:
        conclude =  "Underweight"
    elif BMI < 25:
        conclude =  "Normal"
    elif BMI < 30:
        conclude =  "Overweight"
    else:
        conclude =  "Obese"
    return render_template('bmi.html', BMI = BMI, weight = weight, height = height, conclude = conclude)
if __name__ == '__main__':
  app.run(debug=True)
