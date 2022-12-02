import sqlite3
class CreateTable:

    def createEmployee(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS employee(
                        EID TEXT PRIMARY KEY,
                        EFIRSTNAME TEXT NOT NULL,
                        ELASTNAME TEXT NOT NULL,
                        ENO INTEGER UNIQUE,
                        SALARY INTEGER NOT NULL,
                        HOTELID TEXT NOT NULL, 
                        WORKSHOTELID TEXT,
                        CONSTRAINT FK_HOTELID FOREIGN KEY(HOTELID) REFERENCES hotel(HOTELID) ON DELETE CASCADE,
                        CONSTRAINT FK_WORKSHOTELID FOREIGN KEY(WORKSHOTELID) REFERENCES hotel(HOTELID) ON DELETE CASCADE    
                    );""")
        conn.commit()
        conn.close()
        

    def createHotel(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS hotel(
                        HOTELID TEXT PRIMARY KEY,
                        HNAME TEXT NOT NULL,
                        LOCATION TEXT NOT NULL,
                        OID TEXT,
                        CONSTRAINT FK_OID FOREIGN KEY(OID) REFERENCES owner(OID) ON DELETE CASCADE    
                    );""")
        conn.commit()
        conn.close()




    def createCustomer(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS customer(
                        CID TEXT PRIMARY KEY,
                        MOBILENO INTEGER UNIQUE,
                        EMAILID TEXT,
                        FNAME TEXT NOT NULL,
                        LNAME TEXT NOT NULL
                    );""")
        conn.commit()
        conn.close()
        
    
    def createServices(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS services(
                        SNO TEXT PRIMARY KEY,
                        STYPE TEXT NOT NULL,
                        PRICE INTEGER NOT NULL,
                        SSTATUS TEXT NOT NULL,
                        CONSTRAIT CH1 CHECK(STYPE IN ['gym','restaurant']),
                        CONSTRAIT CH2 CHECK(SSTATUS IN ['available','not-available'])
                    );""")
        conn.commit()
        conn.close()

    def createOwner(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS owner(
                        OID TEXT PRIMARY KEY,
                        MOBILENO INTEGER UNIQUE,
                        EMAILID TEXT,
                        FNAME TEXT NOT NULL,
                        LNAME TEXT NOT NULL
                    );""")
        conn.commit()
        conn.close()


    def createRooms(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS rooms(
                        RID TEXT,
                        HOTELID TEXT,
                        RTYPE TEXT NOT NULL,
                        RSTATUS TEXT NOT NULL,
                        CONSTRAIT CH1 CHECK(RTYPE IN ['ac','non-ac']),
                        CONSTRAIT CH2 CHECK(RSTATUS IN ['available','not-available']),
                        CONSTRAINT FK_HOTELID FOREIGN KEY(HOTELID) REFERENCES hotel(HOTELID) ON DELETE CASCADE,
                        CONSTRAINT PK_rooms PRIMARY KEY(RID,HOTELID)
                    );""")
    
        conn.commit()
        conn.close()
        
    def createProvides(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS provides(HOTELID TEXT,
                        SNO TEXT,
                        CONSTRAINT FK_HOTELID FOREIGN KEY(HOTELID) REFERENCES hotel(HOTELID) ON DELETE CASCADE,
                        CONSTRAINT FK_SNO FOREIGN KEY(SNO) REFERENCES services(SNO) ON DELETE CASCADE,
                        CONSTRAINT PK_provides PRIMARY KEY(HOTELID,SNO)
                    );""")
        conn.commit()
        conn.close()
    
    def createBooking(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS booking(
                        HOTELID TEXT,
                        CID TEXT,
                        CONSTRAINT FK_HOTELID FOREIGN KEY(HOTELID) REFERENCES hotel(HOTELID) ON DELETE CASCADE,
                        CONSTRAINT FK_CID FOREIGN KEY(CID) REFERENCES customer(CID) ON DELETE CASCADE,
                        CONSTRAINT PK_booking PRIMARY KEY(HOTELID,CID)
                    );""")
        conn.commit()
        conn.close()
        
    def createBill(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS bill(
                        BILLID TEXT,
                        CID TEXT,
                        AMOUNT INTEGER NOT NULL,
                        MODE TEXT NOT NULL,
                        CONSTRAIT CH CHECK(MODE IN ['cash','card']),
                        CONSTRAINT FK_CID FOREIGN KEY(CID) REFERENCES customer(CID) ON DELETE CASCADE,
                        CONSTRAINT PK_bill PRIMARY KEY(BILLID,CID)
                    );""")
        conn.commit()
        conn.close() 

    def login(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS login(
                        USERNAME TEXT PRIMARY KEY,
                        PASSWORD TEXT NOT NULL,
                        MODE TEXT NOT NULL
                    );""")
        conn.commit()
        conn.close()   