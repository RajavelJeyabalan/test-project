from flask import *
import sqlite3

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("Homepage.html")


@app.route("/saveVendorDetails", methods=["POST", "GET"])
def savevdetails():
    msg = "msg"
    if request.method == "POST":
        try:
            vendorid = request.form["vendorid"]
            vendorname = request.form["vendorname"]
            vendorgstid = request.form["vendorgstid"]
            vendoraddress = request.form["vendoraddress"]
            vendorcontact = request.form["vendorcontact"]
            vendoremailID = request.form["vendoremailid"]
            vendorwebsite = request.form["vendorwebsite"]
            with sqlite3.connect("Enp.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT into Enpvendors (vendorid, vendorname, vendorgstid, vendoraddress, vendorcontact, vendoremailid, vendorwebsite) values (?,?,?,?,?,?,?)",
                    (vendorid, vendorname, vendorgstid, vendoraddress, vendorcontact, vendoremailid, vendorwebsite))
                con.commit()
                msg = "Vendors details successfully Added"
        except:
            con.rollback()
            msg = "Vendors details not added"
        finally:
            return render_template("vdsuccess.html", msg=msg)
            con.close()


@app.route("/saveClientDetails", methods=["POST", "GET"])
def savecdetails():
    msg = "msg"
    if request.method == "POST":
        try:
            clientid = request.form["clientid"]
            clientname = request.form["clientname"]
            clientgstid = request.form["clientgstid"]
            clientaddress = request.form["clientaddress"]
            clientcontact = request.form["clientcontact"]
            clientemailID = request.form["clientemailid"]
            clientwebsite = request.form["clientwebsite"]
            with sqlite3.connect("Enp.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT into Enpclients (clientid, clientname, clientgstid, clientaddress, clientcontact, clientemailid, clientwebsite) values (?,?,?,?,?,?,?)",
                    (clientid, clientname, clientgstid, clientaddress, clientcontact, clientemailid, clientwebsite))
                con.commit()
                msg = "Client details successfully Added"
        except:
            con.rollback()
            msg = "Client details not added"
        finally:
            return render_template("cdsuccess.html", msg=msg)
            con.close()


@app.route("/vdetailsview")
def viewvendor():
    con = sqlite3.connect("Enp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Enpvendors")
    rows = cur.fetchall()
    return render_template("Vview.html", rows=rows)


@app.route("/cdetailsview")
def viewclient():
    con = sqlite3.connect("Enp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("Select * from Enpclients")
    rows = cur.fetchall()
    return render_template("cview.html", rows=rows)


@app.route("/vendordelete")
def vdelete():
    id = request.form["id"]
    with sqlite3.connect("Enp.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Enpvendors where id =?", id)
            msg = "record deleted sucessfully"
        except:
            msg = "cant be deleted"
        finally:
            return render_template("vdelete.html", msg=msg)


@app.route("/clientdelete")
def cdelete():
    id = request.form["id"]
    with sqlite3.connect("Enp.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Enpclients where id =?", id)
            msg = "record deleted sucessfully"
        except:
            msg = "cant be deleted"
        finally:
            return render_template("cdelete.html", msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
