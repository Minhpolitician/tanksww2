from flask import Flask, render_template, request, redirect
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

@app.route('/admin')
def admin():
    return render_template("admin.html", tank_types=tankType.objects())


@app.route('/delete_tank_type/<tank_id>')
def delete_tank_type(tank_id):
    tank_type = tankType.objects().with_id(tank_id)
    if tank_type is not None:
        tank_type.delete()
    return redirect('/admin')
    return "Deleted:" + tank_id


if __name__ == '__main__':
  app.run(debug=True)
