import sqlite3
from tkinter import *
class UpdateTable:
    def updateEmployee(self):
        def upd(eno,salary,hotelid,workshotelid,eid):
            conn = sqlite3.connect('Hotel_Management.db')
            conn.execute("PRAGMA foreign_keys = 1")
            c = conn.cursor()
            c.execute("UPDATE employee SET ENO=(?) WHERE EID=(?)",(eno,eid))
            c.execute("UPDATE employee SET SALARY=(?) WHERE EID=(?)",(salary,eid))
            c.execute("UPDATE employee SET HOTELID=(?) WHERE EID=(?)",(hotelid,eid))
            c.execute("UPDATE employee SET WORKSHOTELID=(?) WHERE EID=(?)",(workshotelid,eid))
            conn.commit()
            conn.close()
        def ue(wE,eid):
            wE.destroy()
            win = Tk()
            win.iconbitmap(r'favicon.ico')
            Label(win,text='Enter new ENO:').pack()
            eno = Entry(win)
            eno.pack()
            Label(win,text='Enter new SALARY:').pack()
            salary = Entry(win)
            salary.pack()
            Label(win,text='Enter new HOTELID:').pack()
            hotelid = Entry(win)
            hotelid.pack()
            Label(win,text='Enter new WORKSHOTELID:').pack()
            workshotelid = Entry(win)
            workshotelid.pack()
            Button(win,text='Ok',command=lambda : upd(eno.get(),salary.get(),hotelid.get(),workshotelid.get(),eid)).pack()
            win.mainloop()
        w = Tk()
        w.iconbitmap(r'favicon.ico')
        Label(w,text='Enter EID:').pack()
        eid = Entry(w)
        eid.pack()
        Button(w,text='Ok',command=lambda:ue(w,eid.get())).pack()
        w.mainloop()

    def updateOwner(self):
        def upd(oid,ono,email):
            conn = sqlite3.connect('Hotel_Management.db')
            conn.execute("PRAGMA foreign_keys = 1")
            c = conn.cursor()
            c.execute("UPDATE owner SET MOBILENO=(?),EMAILID=(?) WHERE OID=(?)",(ono,email,oid))
            conn.commit()
            conn.close()
        win = Tk()
        win.iconbitmap(r'favicon.ico')
        Label(win,text='Enter new OID:').pack()
        oid = Entry(win)
        oid.pack()
        Label(win,text='Enter new MOBILENO:').pack()
        ono = Entry(win)
        ono.pack()
        Label(win,text='Enter new EMAILID:').pack()
        email = Entry(win)
        email.pack()
        Button(win,text='Ok',command=lambda : upd(oid.get(),ono.get(),email.get())).pack()
        win.mainloop()

    def updateRooms(self):
        def upd(hotelid,rid,rtype,rstatus):
            conn = sqlite3.connect('Hotel_Management.db')
            conn.execute("PRAGMA foreign_keys = 1")
            c = conn.cursor()
            c.execute("UPDATE rooms SET RTYPE=(?),RSTATUS=(?) WHERE HOTELID=(?) AND RID=(?)",(rtype,rstatus,hotelid,rid))
            conn.commit()
            conn.close()
        win = Tk()
        win.iconbitmap(r'favicon.ico')
        Label(win,text='Enter new HOTELID:').pack()
        hotelid = Entry(win)
        hotelid.pack()
        Label(win,text='Enter new RID:').pack()
        rid = Entry(win)
        rid.pack()
        Label(win,text='Enter new RTYPE:').pack()
        rtype = Entry(win)
        rtype.pack()
        Label(win,text='Enter new RSTATUS:').pack()
        rstatus = Entry(win)
        rstatus.pack()
        Button(win,text='Ok',command=lambda : upd(hotelid.get(),rid.get(),rtype.get(),rstatus.get())).pack()
        win.mainloop()
    
    def updateServices(self):
        def upd(sno,stype,sstatus,price):
            conn = sqlite3.connect('Hotel_Management.db')
            conn.execute("PRAGMA foreign_keys = 1")
            c = conn.cursor()
            c.execute("UPDATE services SET STYPE=(?),SSTATUS=(?),PRICE=(?) WHERE SNO=(?)",(stype,sstatus,price,sno))
            conn.commit()
            conn.close()
        win = Tk()
        win.iconbitmap(r'favicon.ico')
        Label(win,text='Enter new SNO:').pack()
        sno = Entry(win)
        sno.pack()
        Label(win,text='Enter new STYPE:').pack()
        stype = Entry(win)
        stype.pack()
        Label(win,text='Enter new SSTATUS:').pack()
        sstatus = Entry(win)
        sstatus.pack()
        Label(win,text='Enter new PRICE:').pack()
        price = Entry(win)
        price.pack()
        Button(win,text='Ok',command=lambda : upd(sno.get(),stype.get(),sstatus.get(),price.get())).pack()
        win.mainloop()