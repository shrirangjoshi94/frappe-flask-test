from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user_name'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'frappe_test_flask'

mysql = MySQL(app)

@app.route("/product")
def indexProducts():
    products = getProducts()
    return render_template('product_index.html', products = products)

@app.route("/product/create")
def createProduct():
    return render_template('product_create.html')

@app.route("/product/store", methods = ['POST'])
def saveProduct():
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO `products` (`name`, `description`) VALUES (%s, %s); ", [request.form['name'], request.form['description']])
    mysql.connection.commit()
    return redirect("/product")

@app.route("/product/delete/<product_id>")
def deleteProduct(product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE from `products` where `product_id`=%s;", [product_id])
    mysql.connection.commit()
    cursor.close()
    return redirect("/product")

@app.route("/product/edit/<product_id>")
def editProductDetails(product_id):
    return render_template('product_edit.html', product = getProductDetails(product_id))

@app.route("/product/update", methods = ['POST'])
def updateProductDetails():
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE `products` SET `name`=%s, `description`=%s where `product_id`=%s; ", [request.form['name'], request.form['description'], request.form['product_id']])
    mysql.connection.commit()
    return redirect("/product")

def getProducts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT `product_id`, `name`, `description` from `products`;")
    products = cursor.fetchall()
    cursor.close()
    return products;

def getProductDetails(product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT `product_id`, `name`, `description` from `products` where `product_id`=%s;", product_id)
    product_details = cursor.fetchone()
    cursor.close()
    return product_details;

@app.route("/location")
def indexLocations():
    locations = getLocations()
    return render_template('location_index.html', locations = locations)

@app.route("/location/create")
def createLocation():
    return render_template('location_create.html')

@app.route("/location/store", methods = ['POST'])
def saveLocation():
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO `locations` (`name`, `description`) VALUES (%s, %s); ", [request.form['name'], request.form['description']])
    mysql.connection.commit()
    return redirect("/location")

@app.route("/location/delete/<location_id>")
def deleteLocation(location_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE from `locations` where `location_id`=%s;", [location_id])
    mysql.connection.commit()
    cursor.close()
    return redirect("/location")

@app.route("/location/edit/<location_id>")
def editLocationDetails(location_id):
    return render_template('location_edit.html', location = getLocationDetails(location_id))

@app.route("/location/update", methods = ['POST'])
def updateLocationDetails():
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE `locations` SET `name`=%s, `description`=%s where `location_id`=%s; ", [request.form['name'], request.form['description'], request.form['location_id']])
    mysql.connection.commit()
    return redirect("/location")

def getLocations():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT `location_id`, `name`, `description` from `locations`;")
    locations = cursor.fetchall()
    cursor.close()
    return locations;

def getLocationDetails(location_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT `location_id`, `name`, `description` from `locations` where `location_id`=%s;", location_id)
    location_details = cursor.fetchone()
    cursor.close()
    return location_details;

if __name__	 == '__main__':
	app.run(debug=True)