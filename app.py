from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from werkzeug.utils import secure_filename

# Flask app setup
app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Andhikad66",
    database="car_dealership"
)
cursor = db.cursor(dictionary=True)


# ROUTES

@app.route('/')
def index():
    search = request.args.get("search", "")
    status = request.args.get("status", "")
    sort = request.args.get("sort", "")

    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    # Search by make or model
    if search:
        query += " AND (make LIKE %s OR model LIKE %s)"
        params.extend([f"%{search}%", f"%{search}%"])

    #  Filter by status (available/sold)
    if status:
        query += " AND status = %s"
        params.append(status)

    #  Sorting
    if sort == "priceAsc":
        query += " ORDER BY price ASC"
    elif sort == "priceDesc":
        query += " ORDER BY price DESC"
    elif sort == "yearAsc":
        query += " ORDER BY year ASC"
    elif sort == "yearDesc":
        query += " ORDER BY year DESC"

    cursor.execute(query, tuple(params))
    cars = cursor.fetchall()

    return render_template('index.html', cars=cars)


@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        vin = request.form['vin']
        engine = request.form['engine']
        mileage = request.form['mileage']
        color = request.form['color']
        price = request.form['price']
        status = request.form['status']

        # Handle photo upload
        photo = request.files['photo']
        photo_filename = None
        if photo and photo.filename != '':
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_filename = filename

        # Insert into DB
        cursor.execute("""
            INSERT INTO cars (make, model, year, vin, engine, mileage, color, price, status, photo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (make, model, year, vin, engine, mileage, color, price, status, photo_filename))
        db.commit()

        return redirect(url_for('index'))

    return render_template('add_car.html')


@app.route('/update_car/<int:car_id>', methods=['GET', 'POST'])
def update_car(car_id):
    cursor.execute("SELECT * FROM cars WHERE car_id = %s", (car_id,))
    car = cursor.fetchone()

    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        vin = request.form['vin']
        engine = request.form['engine']
        mileage = request.form['mileage']
        color = request.form['color']
        price = request.form['price']
        status = request.form['status']

        # Handle new photo upload (keep old one if not replaced)
        photo = request.files['photo']
        photo_filename = car['photo']  
        if photo and photo.filename != '':
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_filename = filename

        cursor.execute("""
            UPDATE cars 
            SET make=%s, model=%s, year=%s, vin=%s, engine=%s, mileage=%s, 
                color=%s, price=%s, status=%s, photo=%s
            WHERE car_id=%s
        """, (make, model, year, vin, engine, mileage, color, price, status, photo_filename, car_id))
        db.commit()

        return redirect(url_for('index'))

    return render_template('update_car.html', car=car)


@app.route('/delete_car/<int:car_id>')
def delete_car(car_id):
    cursor.execute("DELETE FROM cars WHERE car_id=%s", (car_id,))
    db.commit()
    return redirect(url_for('index'))


@app.route('/view_car/<int:car_id>')
def view_car(car_id):
    cursor.execute("SELECT * FROM cars WHERE car_id=%s", (car_id,))
    car = cursor.fetchone()
    return render_template('view_car.html', car=car)


if __name__ == '__main__':
    app.run(debug=True)

#python app.py
#"D:/portfolio projects/car inventory system/venv/Scripts/activate.bat"    
