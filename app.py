from flask import Flask, render_template, request
import mlab
from mongoengine import *
app = Flask(__name__)

mlab.connect()

class TankType(Document):
    name = StringField()
    image = StringField()
    description = StringField()
#
# tank_types = TankType.objects()
#
# for tank_type in tank_types:
#     print(tank_type.name)


@app.route('/')
def index():
    return render_template('index.html', tank_types=TankType.objects())


@app.route('/bmi-calc')
def bmi_calc():
    return render_template("bmi_calc.html")


@app.route('/bmi')
def bmi():
    args = request.args
    weight = int(args["weight"])
    height = int(args["height"]) / 100
    bmi = weight / (height ** 2)
    return str(bmi)


if __name__ == '__main__':
  app.run(debug=True)
