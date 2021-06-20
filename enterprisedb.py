import sqlite3

con = sqlite3.connect("Enp.db")

print("Database opened successfully")

#con.execute("create table Enpvendors (vendorid INTEGER PRIMARY KEY AUTOINCREMENT, vendorname Text NOT NULL, vendorgstid Text NOT NULL,  vendoraddress Text NOT NULL, vendorcontact Text NOT NULL, vendoremailid UNIQUE NOT NULL, vendorvwebsite Text NOT NULL)")

#con.execute("create table Enpclients (clientid INTEGER PRIMARY KEY AUTOINCREMENT, clientname Text NOT NULL, clientgstid Text NOT NULL, clientaddress Text NOT NULL, clientcontact Text NOT NULL, clientemailid UNIQUE NOT NULL, clientwebsite Text NOT NULL)")

con.execute("create table Vquotation (productid INTEGER PRIMARY KEY AUTOINCREMENT, productname Text NOT NULL,  quantity Text NOT Null, rate Text NOT NUll, GST Text Not Null)")

con.execute("create table Cquotation (productid INTEGER PRIMARY KEY AUTOINCREMENT, productname Text NOT NULL,  quantity Text NOT Null, rate Text NOT NUll, GST Text Not Null)")


print ("Tables created")

con.close()