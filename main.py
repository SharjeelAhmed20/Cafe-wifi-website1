from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

app=Flask(__name__)
# Set the SECRET_KEY for CSRF protection
app.config['SECRET_KEY'] = 'killer503.'
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#add-new-cafe-form
class AddNewCafeForm(FlaskForm):
    name= StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Cafe Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    seats = StringField("No of seats", validators=[DataRequired()])
    has_toilets = StringField("Has toilets?", validators=[DataRequired()])
    has_wifi = StringField("Has wifi?", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    has_sockets = StringField("Coffee Price", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# Café table configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    result = db.session.execute(db.select(Cafe))
    cafe = result.scalars().all()
    return render_template("index.html",all_cafes=cafe)

@app.route("/add_new",methods=["GET","POST"])
def add_new():
    form  =AddNewCafeForm()
    if form.validate_on_submit():
        new_cafe=Cafe(
        name=form.name.data,
        map_url = form.map_url.data,
        img_url = form.img_url.data,
        location = form.location.data,
        seats = form.seats.data,
        has_toilet = form.has_toilets.data,
        has_wifi = form.has_wifi.data,
        has_sockets =form.has_sockets,
        coffee_price = form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add-cafe.html",form=form)
if __name__ == "__main__":
    app.run(debug=True)
