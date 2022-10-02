from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Location', validators=[DataRequired()])
    Open = StringField('Open', validators=[DataRequired()])
    Close = StringField('Close', validators=[DataRequired()])
    Cofee = SelectField(u'Coffee', choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"] , validators=[DataRequired()])
    Wifi = SelectField(u'Strong', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],validators=[DataRequired()])
    Power = SelectField(u'socket', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------




# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST","GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        data=f"\n{form.cafe.data},{form.Location.data},{form.Open.data},{form.Close.data},{form.Cofee.data}," \
             f"{form.Wifi.data},{form.Power.data}"
        print(data)
        with open('cafe-data.csv', newline='', encoding="utf8", mode='a') as csv_file:
            csv_file.write(data)

        list_of_rows = []
        with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')

            for row in csv_data:
                list_of_rows.append(row)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes' , methods=["POST","GET"])
def cafes():
    list_of_rows = []
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')

        for row in csv_data:
            list_of_rows.append(row)
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
