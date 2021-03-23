from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from datetime import date
import datetime


matchVar= ['']
########หน้าแรก########
def mainwindow() :
    root = Tk()
    root.title("GUN SHOOTING")
    root.geometry("600x500")
    icon = PhotoImage(file = 'logo.png')
    root.iconphoto(False, icon)
    root.minsize(width=600, height=500)
    root.maxsize(width=600, height=500)

    canvas = Canvas(root, width=600, height=500)
    canvas.place(height=500, width=600)

    bg = PhotoImage(file = 'pa.png')
    canvas.create_image(0, 0, image = bg, anchor=NW)

    def tick():
        curtime = datetime.datetime.now()
        ftime = curtime.strftime('%G-%m-%d %H:%M:%S')
        lb_clock = Label(font='consolas 14',text = ftime)
        lb_clock.place(width=200, x=30,y=460)
        lb_clock.after(1000, tick)

    def infobox():
        messagebox.showinfo( "Information", "version beta 1.1.1")

    iconhome = PhotoImage(file='house.gif')
    homebt = Button(root ,image= iconhome,height=70, width=70 ,bd=3, cursor='hand2')
    homebt.grid(column=0, row=0)

    iconuser = PhotoImage(file='user.gif')
    userbt = Button(root ,image= iconuser, height=70, width=70 ,bd=3, cursor='hand2',command= user )
    userbt.grid(column=1, row=0)

    iconrange = PhotoImage(file='range.gif')
    matchbt = Button(root ,image= iconrange, height=70, width=70 ,bd=3, cursor='hand2' )
    matchbt.grid(column=2, row=0)
    matchbt.bind("<Button-1>", match)

    iconscore = PhotoImage(file='score.gif')
    scorebt = Button(root ,image= iconscore, height=70, width=70 ,bd=3, cursor='hand2', command= score )
    scorebt.grid(column=3, row=0)

    iconprint = PhotoImage(file='printer.gif')
    printbt = Button(root ,image= iconprint, height=70, width=70 ,bd=3 , cursor='hand2', command= report)
    printbt.grid(column=4, row=0)

    iconinfo = PhotoImage(file='info.gif')
    infobt = Button(root ,image= iconinfo, height=70, width=70 ,bd=3, cursor='hand2', command=infobox)
    infobt.grid(column=5, row=0)

    tick()
    root.mainloop()

########เพิ่มแมทซ์##########
def match(e) :
    root1 = Toplevel()
    root1.title("GUN SHOOTING")
    root1.geometry("600x300")
    icon = PhotoImage(file = 'logo.png')
    root1.iconphoto(False, icon)
    root1.minsize(width=600, height=300)
    root1.maxsize(width=600, height=300)
    root1.option_add("*Font", "Dungeon 12")

    global matchVar
    
    canvas = Canvas(root1, width=600, height=300)
    canvas.pack()

    bg = PhotoImage(file = 'match.png')
    canvas.create_image(0, 0, image = bg, anchor=NW)  

    def on_click(a):
        matchVar.append(nm_et.get())
        print(matchVar)

    def infobox():
        messagebox.showinfo( "message", "บันทึกการแข่งขันแล้ว")     

    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

    nm_lb = Label(root1, text = 'Match Name',bg='black',fg= 'white')
    nm_lb.place(x=50, y= 60)

    nm_et = Entry(root1, bd=3, width=30)
    nm_et.place(x=180, y= 60)

    lm_lb = Label(root1, text = 'Location',bg='black',fg= 'white')
    lm_lb.place(x=50, y= 100)

    lm_et = Entry(root1, bd=3, width=30)
    lm_et.place(x=180, y= 100)

    dm_lb = Label(root1, text = 'Date',bg='black',fg= 'white')
    dm_lb.place(x=50, y= 140)

    cbo_day = ttk.Combobox(root1, values=list(range(1, 32)), width=3, state="readonly")
    cbo_day.current(0)
    cbo_day.place(x=180, y= 140)

    cbo_month = ttk.Combobox(root1, values=month_list, width=4, state="readonly")
    cbo_month.current(1)
    cbo_month.place(x=250, y= 140)

    cbo_year = ttk.Combobox(root1, values=list(range(2000, 2022)), width=5, state="readonly")
    cbo_year.current(1)
    cbo_year.place(x=330, y= 140)

    ok = Button(root1, text="CREATE",bd=3, cursor='hand2', width= 13, height=1, command= infobox)
    ok.place(x=300, y= 220)
    ok.bind("<Button-1>",on_click)
    



    root1.mainloop()

########เพิ่มผู้เข้าแข่งขัน########
def user() :
    root = Toplevel()
    root.title("GUN SHOOTING")
    root.geometry("600x500")
    icon = PhotoImage(file = 'logo.png')
    root.iconphoto(False, icon)
    root.minsize(width=600, height=500)
    root.maxsize(width=600, height=500)
    root.option_add("*Font", "Dungeon 12")

#ฟังก์ชันแสดงรายชื่อที่เพิ่มเข้า
    def show_name() :
        a = name_et.get()+'                  '+team_cb.get()+'                       ' +ty_cb.get()

        for i in range(1):
            listbox.insert(END, a)

        name_et.delete(0,END)

    frame1 = Frame(root,  bd = 3, height = 260, width = 600, relief= GROOVE, highlightthickness= 20 )
    frame1.pack()

    name_frame = Label(root, text = 'Add contestants')     #ชื่อเฟรมที่1
    name_frame.place(x=80, y= 10)

    frame2 = Frame(root, height = 260, width = 600, relief= GROOVE, highlightthickness= 20)   #ฟังก์ชันแสดงรายชื่อที่เพิ่มเข้า
    frame2.pack(fill= BOTH, expand=1)

    head = Label(frame2, text= 'NAME                            TEAM                            TYPE')
    head.pack()

    scrollbar = Scrollbar(frame2)        #ฟังก์ชันแสดงรายชื่อที่เพิ่มเข้า
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(frame2)
    listbox.pack(fill=BOTH, expand=1)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
  
    type_list = ['Open', 'Standard', 'Modify', 'Standard manual']
    team_list = ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7', 'SQ8', 'SQ9', 'SQ10', 'SQ11', 'SQ12', 'SQ13',
         'SQ14', 'SQ15', 'SQ16', 'SQ17', 'SQ18', 'SQ19', 'SQ20']

    name_lb = Label(frame1, text = 'Name')
    name_lb.place(x=40, y= 40)

    name_et = Entry(frame1, bd=3, width=21)
    name_et.place(x=200, y= 40)

    team_lb = Label(frame1, text = 'Team (SQ)')
    team_lb.place(x=40, y= 80)

    team_cb = ttk.Combobox(frame1, values=team_list, width=20, state="readonly")
    team_cb.current(0)
    team_cb.place(x=200, y= 80)

    ty_lb = Label(frame1, text = 'Type')
    ty_lb.place(x=40, y= 120)

    ty_cb = ttk.Combobox(frame1, values=type_list, width=20, state="readonly")
    ty_cb.current(0)
    ty_cb.place(x=200, y= 120)

    ok = Button(frame1, text="OK",bd=3, cursor='hand2', width= 13, height=1, command= show_name)
    ok.place(x=290, y= 170)

    root.mainloop()

def score():
    root = Toplevel()
    root.title("GUN SHOOTING")
    root.geometry("700x350")
    icon = PhotoImage(file = 'logo.png')
    root.iconphoto(False, icon)
    root.minsize(width=700, height=350)
    root.maxsize(width=700, height=350)
    root.option_add("*Font", "Dungeon 12")

    canvas = Canvas(root, width=700, height=350)
    canvas.pack()

    bg = PhotoImage(file = 'scoree.png')
    canvas.create_image(0, 0, image = bg, anchor=NW)

    name_frame2 = Label(root, text = 'Select',bg='black',fg= 'white')
    name_frame2.place(x=180, y= 70)

    name_frame = Label(root, text = 'Input',bg='black',fg= 'white')
    name_frame.place(x=510, y= 70)

    addscore_lb = Label(root, text = 'Score :',bg='black',fg= 'white')
    addscore_lb.place(x=450, y= 100)
    
    addscore_en = Entry(root,bd = 3, width = 10)
    addscore_en.place(x=480, y= 130)

    addtime_lb = Label(root, text = 'Time :',bg='black',fg= 'white')
    addtime_lb.place(x=450, y= 180)

    addtime_en = Entry(root, bd = 3, width = 10)
    addtime_en.place(x=480, y= 210)

    semat_lb = Label(root, text = 'Match :',bg='black',fg= 'white')
    semat_lb.place(x=100, y= 100)

    seteam_lb = Label(root, text = 'Stage :',bg='black',fg= 'white')
    seteam_lb.place(x=100, y= 140)

    sestat_lb = Label(root, text = 'Team :',bg='black',fg= 'white')
    sestat_lb.place(x=100, y= 180)

    sepeople_lb = Label(root, text = 'Name :',bg='black',fg= 'white')
    sepeople_lb.place(x=100, y= 220)

    semat_cb = ttk.Combobox(root, values=list(range(1, 32)), width=15, state="readonly")
    semat_cb.current(0)
    semat_cb.place(x=200, y= 100)

    seteam_cb = ttk.Combobox(root, values=list(range(1, 32)), width=15, state="readonly")
    seteam_cb.current(0)
    seteam_cb.place(x=200, y= 140)

    sestat_cb = ttk.Combobox(root, values=list(range(1, 32)), width=15, state="readonly")
    sestat_cb.current(0)
    sestat_cb.place(x=200, y= 180)

    sepeople_cb = ttk.Combobox(root, values=list(range(1, 32)), width=15, state="readonly")
    sepeople_cb.current(0)
    sepeople_cb.place(x=200, y= 220)

    ok_bt = Button(root, text="OK",bd=3, cursor='hand2', width= 10, height=1)
    ok_bt.place(x=520, y= 280)

    root.mainloop()

def report():
    global matchVar

    root = Toplevel()
    root.title("GUN SHOOTING")
    root.geometry("500x300")
    icon = PhotoImage(file = 'logo.png')
    root.iconphoto(False, icon)
    root.minsize(width=500, height=300)
    root.maxsize(width=500, height=300)
    root.option_add("*Font", "Dungeon 12")

    canvas = Canvas(root, width=500, height=300)
    canvas.pack()

    bg = PhotoImage(file = 'print.png')
    canvas.create_image(0, 0, image = bg, anchor=NW)  


    list_typeprint = ['All contestants','Split stage, unordered','Split stage, split type','Classified, all stage included']

    select_name = Label(root, text= 'Select a match',bg='#1e0f3e',fg= 'white')
    select_name.place(x=100, y=70)

    select_match = ttk.Combobox(root, values=matchVar, width=20, state="readonly")
    select_match.current(0)
    select_match.place(x=140, y= 100)

    select_type = Label(root, text= 'Select a report type',bg='#1c0e3c',fg= 'white')
    select_type.place(x=100, y=150)

    select_type = ttk.Combobox(root, values=list_typeprint, width=20, state="readonly")
    select_type.current(0)
    select_type.place(x=140, y= 180)

    ok_bt = Button(root, text = 'OK', width= 10)
    ok_bt.place(x=280, y=220)

    root.mainloop()

if __name__ == "__main__" :
    mainwindow()
