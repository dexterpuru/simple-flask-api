from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import fetchDataset

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:puru2000@localhost:5432/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Categories(db.Model):
    CategoryID = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(), nullable=False)
    Description = db.Column(db.String(), nullable=False)

    def __init__(self, CategoryID, CategoryName, Description):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.Description = Description

    def __repr__(self):
        return '%r %r %r' % self.CategoryName, self.CategoryName, self.Description


class Customers(db.Model):
    CustomerID = db.Column(db.String(), primary_key=True)
    CustomerName = db.Column(db.String(), nullable=False)
    ContactName = db.Column(db.String(), nullable=False)
    ContactTitle = db.Column(db.String(), nullable=False)
    Address = db.Column(db.String(), nullable=False)
    City = db.Column(db.String(), nullable=False)
    Region = db.Column(db.String(), nullable=True)
    Pincode = db.Column(db.String(), nullable=False)
    Country = db.Column(db.String(), nullable=False)
    Phone = db.Column(db.String(), nullable=False)
    Fax = db.Column(db.String(), nullable=True)

    def __init__(self, CustomerID, CustomerName, ContactName, ContactTitle, Address, City, Region, Pincode, Country, Phone, Fax):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.Pincode = Pincode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax

    def __repr__(self):
        return '<Customer Id %r, Customer Name %r, Address %r>' % self.CustomerID, self.CustomerName, self.Address


class Employees(db.Model):
    EmployeeId = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(db.String(), nullable=False)
    FirstName = db.Column(db.String(), nullable=False)
    Title = db.Column(db.String(), nullable=False)
    TitleOfCourtsy = db.Column(db.String(), nullable=False)
    BirthDate = db.Column(db.String(), nullable=False)
    HireDate = db.Column(db.String(), nullable=True)
    Address = db.Column(db.String(), nullable=False)
    City = db.Column(db.String(), nullable=False)
    Region = db.Column(db.String(), nullable=True)
    PostralCode = db.Column(db.String(), nullable=False)
    Country = db.Column(db.String(), nullable=False)
    HomePhone = db.Column(db.String(), nullable=False)
    Extention = db.Column(db.String(), nullable=False)
    Notes = db.Column(db.String(), nullable=False)
    ReportsTo = db.Column(db.String(), nullable=True)
    PhotoPath = db.Column(db.String(), nullable=False)
    Salary = db.Column(db.Integer, nullable=False)

    def __init__(self, EmployeeId, LastName, FirstName, Title, TitleOfCourtsy, BirthDate, HireDate, Address, City, Region, PostralCode, Country, HomePhone, Extention, Notes, ReportsTo, PhotoPath, Salary):
        self.EmployeeId = EmployeeId
        self.LastName = LastName
        self.FirstName = FirstName
        self.Title = Title
        self.TitleOfCourtsy = TitleOfCourtsy
        self.BirthDate = BirthDate
        self.HireDate = HireDate
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostralCode = PostralCode
        self.Country = Country
        self.HomePhone = HomePhone
        self.Extention = Extention
        self.Notes = Notes
        self.ReportsTo = ReportsTo
        self.PhotoPath = PhotoPath
        self.Salary = Salary

    def __repr__(self):
        return '<Employee Id %r, First Name %r>' % self.EmployeeId, self.FirstName


class EmployeeTerritories(db.Model):
    TerritoryId = db.Column(db.Integer, nullable=False, primary_key=True)
    EmployeeId = db.Column(db.Integer, nullable=False)

    def __init__(self, EmployeeId, TerritoryId):
        self.TerritoryId = TerritoryId
        self.EmployeeId = EmployeeId

    def __repr__(self):
        return '<Territory Id %r>' % self.TerritoryId


class Order(db.Model):
    OrderId = db.Column(db.Integer, primary_key=True)
    CustomerId = db.Column(db.String(), nullable=False)
    EmployeeId = db.Column(db.Integer, nullable=False)
    OrderDate = db.Column(db.String(), nullable=False)
    RequiredDate = db.Column(db.String(), nullable=False)
    ShippedDate = db.Column(db.String(), nullable=False)
    ShipVia = db.Column(db.Integer, nullable=False)
    Fright = db.Column(db.Float, nullable=False)
    ShipName = db.Column(db.String(), nullable=False)
    ShipAddress = db.Column(db.String(), nullable=False)
    ShipCity = db.Column(db.String(), nullable=False)
    ShipRegion = db.Column(db.String(), nullable=True)
    ShipPostalCode = db.Column(db.String(), nullable=False)
    ShipCountry = db.Column(db.String(), nullable=False)

    def __init__(self, OrderId, CustomerId, EmployeeId, OrderDate, RequiredDate, ShippedDate, ShipVia, Fright, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry):
        self.OrderId = OrderId
        self.CustomerId = CustomerId
        self.EmployeeId = EmployeeId
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShippedDate = ShippedDate
        self.ShipVia = ShipVia
        self.Fright = Fright
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.ShipPostalCode = ShipPostalCode
        self.ShipCountry = ShipCountry

    def __repr__(self):
        return '<Order Id %r>' % self.OrderId


class OrderDetails(db.Model):
    OrderId = db.Column(db.Integer, db.ForeignKey(
        'order.OrderId'), nullable=False, primary_key=True)
    ProductId = db.Column(db.Integer, db.ForeignKey(
        'products.ProductId'), nullable=False, primary_key=True)
    UnitPrice = db.Column(db.Integer, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Discount = db.Column(db.Integer, nullable=False)

    def __init__(self, OrderId, ProductId, UnitPrice, Quantity, Discount):
        self.OrderId = OrderId
        self.ProductId = ProductId
        self.UnitPrice = UnitPrice
        self.Quantity = Quantity
        self.Discount = Discount

    def __repr__(self):
        return '<Order Id %r>' % self.OrderId


class Products(db.Model):
    ProductId = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(), nullable=False)
    SupplierId = db.Column(db.Integer, nullable=False)
    CategoryId = db.Column(db.Integer, nullable=False)
    QuantityPerUnit = db.Column(db.String(), nullable=False)
    UnitPrice = db.Column(db.Float, nullable=False)
    UnitsInStock = db.Column(db.Integer, nullable=False)
    UnitsOnOrder = db.Column(db.Integer, nullable=False)
    ReorderLevel = db.Column(db.Integer, nullable=False)
    Discontinued = db.Column(db.Integer, nullable=False)

    def __init__(self, ProductId, ProductName, SupplierId, CategoryId, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued):
        self.ProductId = ProductId
        self.ProductName = ProductName
        self.SupplierId = SupplierId
        self.CategoryId = CategoryId
        self.QuantityPerUnit = QuantityPerUnit
        self.UnitPrice = UnitPrice
        self.UnitsInStock = UnitsInStock
        self.UnitsOnOrder = UnitsOnOrder
        self.ReorderLevel = ReorderLevel
        self.Discontinued = Discontinued

    def __repr__(self):
        return '<Product Id %r, Product Name %r>' % self.ProductId, self.ProductName


class Regions(db.Model):
    RegionID = db.Column(db.Integer, primary_key=True)
    RegionDescription = db.Column(db.String(), nullable=False)

    def __init__(self, RegionID, RegionDescription):
        self.RegionID = RegionID
        self.RegionDescription = RegionDescription

    def __repr__(self):
        return '<Region Name %r>' % self.RegionDescription


class Shippers(db.Model):
    ShipperId = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(), nullable=False)
    Phone = db.Column(db.String(), nullable=False)

    def __init__(self, ShipperId, CompanyName, Phone):
        self.ShipperId = ShipperId
        self.CompanyName = CompanyName
        self.Phone = Phone

    def __repr__(self):
        return '<Company Name %r>' % self.CompanyName


class Suppliers(db.Model):
    SupplierId = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(), nullable=False)
    ContactName = db.Column(db.String(), nullable=False)
    ContactTitle = db.Column(db.String(), nullable=False)
    Address = db.Column(db.String(), nullable=False)
    City = db.Column(db.String(), nullable=False)
    Region = db.Column(db.String(), nullable=True)
    PostalCode = db.Column(db.String(), nullable=False)
    Country = db.Column(db.String(), nullable=False)
    Phone = db.Column(db.String(), nullable=False)
    Fax = db.Column(db.String(), nullable=True)
    HomePage = db.Column(db.String(), nullable=True)

    def __init__(self, SupplierId, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, HomePage):
        self.SupplierId = SupplierId
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax
        self.HomePage = HomePage

    def __repr__(self):
        return '<Supplier Id %r>' % self.SupplierId


class Territories(db.Model):
    TerritoryId = db.Column(db.Integer, primary_key=True)
    TerritoryDescription = db.Column(db.String(), nullable=False)
    RegionId = db.Column(db.Integer, nullable=False)

    def __init__(self, TerritoryId, TerritoryDescription, RegionId):
        self.TerritoryId = TerritoryId
        self.TerritoryDescription = TerritoryDescription
        self.RegionId = RegionId

    def __repr__(self):
        return '<Territory Id %r>' % self.TerritoryId


db.create_all()

# fetchDataset('./Northwind_database_csv/order-details.csv',
#             OrderDetails, db)


@app.route('/insertCustomer', methods=['POST'])
def insertCustomer():

    try:
        id = request.get_json()["id"]
    except:
        return jsonify({"message": "id field is missing from the request body"})

    try:
        CustomerName = request.get_json()["CustomerName"]
    except:
        return jsonify({"message": "CustomerName field is missing from the request body"})

    try:
        ContactName = request.get_json()["ContactName"]
    except:
        return jsonify({"message": "ContactName field is missing from the request body"})

    try:
        ContactTitle = request.get_json()["ContactTitle"]
    except:
        return jsonify({"message": "ContactTitle field is missing from the request body"})

    try:
        address = request.get_json()["address"]
    except:
        return jsonify({"message": "address field is missing from the request body"})

    try:
        city = request.get_json()["city"]
    except:
        return jsonify({"message": "city field is missing from the request body"})

    try:
        region = request.get_json()["region"]
    except:
        return jsonify({"message": "region field is missing from the request body"})

    try:
        pincode = request.get_json()["pincode"]
    except:
        return jsonify({"message": "pincode field is missing from the request body"})

    try:
        country = request.get_json()["country"]
    except:
        return jsonify({"message": "country field is missing from the request body"})

    try:
        phone = request.get_json()["phone"]
    except:
        return jsonify({"message": "phone field is missing from the request body"})

    try:
        fax = request.get_json()["fax"]
    except:
        return jsonify({"message": "fax field is missing from the request body"})

    db.session.add(Customers(id, CustomerName, ContactName, ContactTitle,
                             address, city, region, pincode, country, phone, fax))
    db.session.commit()
    db.session.close()

    return "done"


@app.route('/updateCustomer', methods=['PUT'])
def updateCustomer():
    id = request.get_json().get("id")
    customerObj = Customers.query.filter_by(CustomerID=id).with_entities(Customers.CustomerID, Customers.CustomerName, Customers.ContactName,
                                                                         Customers.ContactTitle, Customers.Address, Customers.City, Customers.Region, Customers.Pincode, Customers.Country, Customers.Phone, Customers.Fax)
    # print(customerObj)
    if request.get_json().get("CustomerName"):
        customerObj.CustomerName = request.get_json().get("CustomerName")
    if request.get_json().get("ContactName"):
        customerObj.ContactName = request.get_json().get("ContactName")
    if request.get_json().get("ContactTitle"):
        customerObj.ContactTitle = request.get_json().get("ContactTitle")
    if request.get_json().get("address"):
        customerObj.Address = request.get_json().get("address")
    if request.get_json().get("city"):
        customerObj.City = request.get_json().get("city")
    if request.get_json().get("region"):
        customerObj.Region = request.get_json().get("region")
    if request.get_json().get("pincode"):
        customerObj.Pincode = request.get_json().get("pincode")
    if request.get_json().get("country"):
        customerObj.Country = request.get_json().get("country")
    if request.get_json().get("phone"):
        customerObj.Phone = request.get_json().get("phone")
    if request.get_json().get("fax"):
        customerObj.Fax = request.get_json().get("fax")
    db.session.commit()
    db.session.close()
    return "done"


@app.route('/selectCustomer', methods=['GET'])
def selectCustomer():
    customersData = []
    print(request.get_json())
    if request.get_json().get("type") == "all":
        customersData = [{
            "id": i.CustomerID, "CustomerName": i.CustomerName,
            "ContactName": i.ContactName, "ContactTitle": i.ContactTitle,
            "address": i.Address, "city": i.City, "region": i.Region,
            "pincode": i.Pincode, "country": i.Country, "phone": i.Phone, "fax": i.Fax}
            for i in Customers.query.all()]

    elif request.get_json().get("type") == "id":
        customersData = [{
            "id": i.CustomerID, "CustomerName": i.CustomerName,
            "ContactName": i.ContactName, "ContactTitle": i.ContactTitle,
            "address": i.Address, "city": i.City, "region": i.Region,
            "pincode": i.Pincode, "country": i.Country, "phone": i.Phone, "fax": i.Fax}
            for i in Customers.query.filter_by(CustomerID=request.get_json().get("id")).all()]

    return jsonify(customersData)


@app.route('/deleteCategory', methods=['DELETE'])
def deletingCategory():
    categoryId = request.get_json()["id"]
    resulyCategory = Categories.query.filter_by(CategoryID=categoryId).first()
    db.session.delete(resulyCategory)
    db.session.commit()
    return "done"


@app.route('/orderHistory', methods=['GET'])
def orderHistory():
    customerID = request.get_json()["id"]
    data = [{"id": i.OrderId, "CustomerId": i.CustomerId, "EmployeeId": i.EmployeeId, "OrderDate": i.OrderDate, "RequiredDate": i.RequiredDate, "ShippedDate": i.ShippedDate, "ShipVia": i.ShipVia, "Fright": i.Fright, "ShipName": i.ShipName, "ShipAddress": i.ShipAddress, "ShipCity": i.ShipCity, "ShipRegion": i.ShipRegion, "ShipPostalCode": i.ShipPostalCode, "ShipCountry": i.ShipCountry}
            for i in Order.query.filter_by(CustomerId=customerID).all()]
    return jsonify(data)
