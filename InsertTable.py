import sqlite3

class InsertTable:
    def insertEmployee(self,eid,efirstname,elastname,eno,salary,hotelid,workshotelid):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?);",(eid,efirstname,elastname,eno,salary,hotelid,workshotelid))
        conn.commit()
        conn.close()
        

    def insertHotel(self,hotelid,location,hname,oid):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO hotel VALUES(?,?,?,?);",(hotelid,location,hname,oid))
        conn.commit()
        conn.close()




    def insertCustomer(self,cid,mobileno,emailid,fname,lname):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO customer VALUES(?,?,?,?,?);",(cid,mobileno,emailid,fname,lname))
        conn.commit()
        conn.close()
        
    
    def insertServices(self,sno,stype,price,sstatus):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO services VALUES(?,?,?,?);",(sno,stype,price,sstatus))
        conn.commit()
        conn.close()

    def insertOwner(self,oid,mobileno,emailid,fname,lname):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO owner VALUES(?,?,?,?,?);",(oid,mobileno,emailid,fname,lname))
        conn.commit()
        conn.close()


    def insertRooms(self,rid,hotelid,rtype,rstatus):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO rooms VALUES(?,?,?,?);",(rid,hotelid,rtype,rstatus))
        conn.commit()
        conn.close()
        
    def insertProvides(self,hotelid,sno):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO provides VALUES(?,?);",(hotelid,sno))
        conn.commit()
        conn.close()
    
    def insertBooking(self,hotelid,cid):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO Booking values(?,?);",(hotelid,cid))
        conn.commit()
        conn.close()
        
    def insertBill(self,billid,cid,amount,mode):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("INSERT INTO bill values(?,?,?,?);",(billid,cid,amount,mode))
        conn.commit()
        conn.close()