from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from datetime import date
import datetime
import sqlite3


matchVar= ['']

def select_namematch():
    conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
    c = conn.cursor()   
    c.execute("SELECT name FROM sqlite_sequence")
    rows = c.fetchall()
    for row in rows:
        matchVar.append(row)

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
    def newmath(a) :
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()
        math = nm_et.get()
        try :
            c.execute ('''CREATE TABLE {}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            team TEXT,
            class TEXT,
            sum_point REAL,
            percen REAL,
            PTS1 REAL NULL,
            time1 REAL NULL,
            hit_factor1 REAL NULL,
            stage_point1 REAL NULL,
            stage_percent1 REAL NULL,
            PTS2 REAL NULL,
            time2 REAL NULL,
            hit_factor2 REAL NULL,
            stage_point2 REAL NULL,
            stage_percent2 REAL NULL,
            PTS3 REAL NULL,
            time3 REAL NULL,
            hit_factor3 REAL NULL,
            stage_point3 REAL NULL,
            stage_percent3 REAL NULL,
            PTS4 REAL NULL,
            time4 REAL NULL,
            hit_factor4 REAL NULL,
            stage_point4 REAL NULL,
            stage_percent4 REAL NULL,
            PTS5 REAL NULL,
            time5 REAL NULL,
            hit_factor5 REAL NULL,
            stage_point5 REAL NULL,
            stage_percent5 REAL NULL,
            PTS6 REAL NULL,
            time6 REAL NULL,
            hit_factor6 REAL NULL,
            stage_point6 REAL NULL,
            stage_percent6 REAL NULL,
            PTS7 REAL NULL,
            time7 REAL NULL,
            hit_factor7 REAL NULL,
            stage_point7 REAL NULL,
            stage_percent7 REAL NULL,
            PTS8 REAL NULL,
            time8 REAL NULL,
            hit_factor8 REAL NULL,
            stage_point8 REAL NULL,
            stage_percent8 REAL NULL,
            PTS9 REAL NULL,
            time9 REAL NULL,
            hit_factor9 REAL NULL,
            stage_point9 REAL NULL,
            stage_percent9 REAL NULL,
            PTS10 REAL NULL,
            time10 REAL NULL,
            hit_factor10 REAL NULL,
            stage_point10 REAL NULL,
            stage_percent10 REAL NULL)'''.format(math))
            conn.commit()

            c.execute('''INSERT INTO {}(id,name,type,team,class,sum_point,percen,PTS1,time1,hit_factor1,stage_point1,stage_percent1,PTS2,time2,hit_factor2,stage_point2,stage_percent2,PTS3,time3,hit_factor3,stage_point3,stage_percent3,PTS4,time4,hit_factor4,stage_point4,stage_percent4,PTS5,time5,hit_factor5,stage_point5,stage_percent5,PTS6,time6,hit_factor6,stage_point6,stage_percent6,PTS7,time7,hit_factor7,stage_point7,stage_percent7,PTS8,time8,hit_factor8,stage_point8,stage_percent8,PTS9,time9,hit_factor9,stage_point9,stage_percent9,PTS10,time10,hit_factor10,stage_point10,stage_percent10) VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)'''.format(math))
            conn.commit()
            conn.close()

        except sqlite3.Error as e :
            print(e)
        finally :
            nm_et.delete(0,END)
            lm_et.delete(0,END)
            messagebox.showinfo( "message", "บันทึกการแข่งขันแล้ว")
            select_namematch()
            if conn :
                conn.close()

    #GUI ########เพิ่มแมทซ์##########
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

    ok = Button(root1, text="CREATE",bd=3, cursor='hand2', width= 13, height=1)
    ok.place(x=300, y= 220)
    ok.bind("<Button-1>",newmath)
    
    root1.mainloop()

########เพิ่มผู้เข้าแข่งขัน########
def user() :
    #โค้ดการทำงานของหน้าเพิ่มผู้เข้าแข่งขัน
    def notnum(S):
        if S.isalpha():
            return True
        root.bell()
        return False

    #ฟังก์ชันเพิ่มชื่อผู้เข้าแข่งขันเข้าในฐานข้อมูล
    def add_people(e) :
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()
        try :
            Team = team_cb.get()
            Name = name_et.get()
            Type = ty_cb.get()
            sql = '''INSERT INTO {} (id,name,type,team,class) VALUES (NULL,?,?,?,?)'''.format(match_cb.get())
            data = (Name,Type,Team,"U")
            c.execute(sql,data)
            conn.commit()
            c.close()

        except sqlite3.Error as e:
            print("Failed to insert : ",e)
        finally :
            if conn :
                conn.close()

    #ฟังก์ชันแสดงรายชื่อที่เพิ่มเข้า ในGUI
    def show_name() :
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()

        for record in my_tree.get_children():
            my_tree.delete(record)

        sql_cmd = """select id,name,type,team,class from {}""".format(match_cb.get())
        c.execute(sql_cmd)

        result = c.fetchall()
        for x in result : 
            my_tree.insert('', 'end',values=x)

        name_et.delete(0,END)

    def show_name2(e) :
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()

        for record in my_tree.get_children():
            my_tree.delete(record)

        sql_cmd = """select id,name,type,team,class from {}""".format(match_cb.get())
        c.execute(sql_cmd)

        result = c.fetchall()
        for x in result : 
            my_tree.insert('', 'end',values=x)

        name_et.delete(0,END)


    def delete_name():
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()
        x = name_et.get()
        print(x)
        try :
            sql = '''DELETE FROM {} WHERE name = '{}' '''.format(match_cb.get(),x)
            c.execute(sql)
            conn.commit()
            c.close()

        except sqlite3.Error as e:
            print("Failed to insert : ",e)
        finally :
            name_et.delete(0,END)
            show_name()
            if conn :
                conn.close()

        

    #GUI
    root = Toplevel()
    root.title("GUN SHOOTING")
    root.geometry("600x500")
    icon = PhotoImage(file = 'logo.png')
    root.iconphoto(False, icon)
    root.minsize(width=600, height=500)
    root.maxsize(width=600, height=500)
    root.option_add("*Font", "Dungeon 12")

    frame1 = Frame(root,  bd = 3, height = 280, width = 600, relief= GROOVE, highlightthickness= 20 )
    frame1.pack()

    name_frame = Label(root, text = 'Add contestants')     #ชื่อเฟรมที่1
    name_frame.place(x=80, y= 10)

    tree_frame =Frame(root)
    tree_frame.pack(pady=20 ,fill=BOTH, expand=1)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
    my_tree.pack(fill=BOTH, expand=1)
    my_tree['columns'] = (1,2,3,4,5)

    my_tree.column('#0', width=0)
    my_tree.column(1, width=10)
    my_tree.column(2, width=150)
    my_tree.column(3, anchor=CENTER, width=50)
    my_tree.column(4, anchor=W, width=50)
    my_tree.column(5, anchor=W, width=50)

    my_tree.heading(1, text="ID")
    my_tree.heading(2, text="Name")
    my_tree.heading(3, text="TYPE")
    my_tree.heading(4, text="TEAM")
    my_tree.heading(5, text="CLASS")

    tree_scroll.config(command=my_tree.yview)
  
    type_list = ['Open', 'Standard', 'Modify', 'Standard manual']
    team_list = ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7', 'SQ8', 'SQ9', 'SQ10', 'SQ11', 'SQ12', 'SQ13',
         'SQ14', 'SQ15', 'SQ16', 'SQ17', 'SQ18', 'SQ19', 'SQ20']

    match_lb = Label(frame1, text = 'Match')
    match_lb.place(x=40, y= 20)

    match_cb = ttk.Combobox(frame1, values=matchVar, width=20, state="readonly")
    match_cb.current(0)
    match_cb.place(x=200, y= 20)
    match_cb.bind("<<ComboboxSelected>>", show_name2)

    name_lb = Label(frame1, text = 'Name')
    name_lb.place(x=40, y= 60)

    vcmd = (root.register(notnum), '%S')
    name_et = Entry(frame1, bd=3, width=21,validate='key', vcmd= vcmd)
    name_et.place(x=200, y= 60)

    team_lb = Label(frame1, text = 'Team (SQ)')
    team_lb.place(x=40, y= 100)

    team_cb = ttk.Combobox(frame1, values=team_list, width=20, state="readonly")
    team_cb.current(0)
    team_cb.place(x=200, y= 100)

    ty_lb = Label(frame1, text = 'Type')
    ty_lb.place(x=40, y= 140)

    ty_cb = ttk.Combobox(frame1, values=type_list, width=20, state="readonly")
    ty_cb.current(0)
    ty_cb.place(x=200, y= 140)

    ok = Button(frame1, text="OK",bd=3, cursor='hand2', width= 13, height=1, command= show_name)
    ok.place(x=350, y= 190)
    ok.bind("<Button-1>",add_people)

    remove = Button(frame1, text="REMOVE",bd=3, cursor='hand2', width= 13, height=1, command= delete_name)
    remove.place(x=180, y= 190)

    root.mainloop()


###########เพิ่มคะแนน##########
def score():
    people_list = [''] #เก็บชื่อผู้เข้าแข่งขันมาแสดงในคอมโบบ้อก

    def infobox():
        messagebox.showerror( "ERROR", "กรอกข้อมูลไม่ถูกต้อง")

    def notstr(S):
        if S.isdigit():
            return True
        root.bell()
        return False

    def people_on_sq(e):
        ###########เพิ่มคะแนนเข้าในฐานข้อมูล##########
        def insert() :
            conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
            c = conn.cursor()
            try :
                match = semat_cb.get()
                scrore = addscore_en.get()
                stage = sestat_cb.get()
                name = sepeople_cb.get()
                time = addtime_en.get()
                sql = '''UPDATE {} SET PTS{}={},time{}={},hit_factor{}=ROUND({}/{},4) WHERE name = '{}' '''.format(match,stage,scrore,stage,time,stage,scrore,time,name)
                c.execute(sql)
                conn.commit()
                c.close()
            except sqlite3.Error as e:
                print("Failed to insert : ",e)
                infobox()
            finally :
                addtime_en.delete(0,END)
                addscore_en.delete(0,END)
                if conn :
                    conn.close()

        del people_list[:]
        try :
            conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
            c = conn.cursor()   
            c.execute("SELECT name FROM {} WHERE team= '{}' ".format(semat_cb.get(),seteam_cb.get()))
            rows = c.fetchall()
            for row in rows:
                people_list.append(row)
        except :
            people_list.append('null')
        finally :
            sepeople_cb = ttk.Combobox(root, values=people_list, width=15, state="readonly")
            sepeople_cb.current()
            sepeople_cb.place(x=200, y= 220)

            ok_bt = Button(root, text="OK",bd=3, cursor='hand2', width= 10, height=1,command= insert)
            ok_bt.place(x=520, y= 280)


    #GUI #############เพิ่มคะแนน##########
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

    addtime_lb = Label(root, text = 'Time :',bg='black',fg= 'white')
    addtime_lb.place(x=450, y= 180)
    
    semat_lb = Label(root, text = 'Match :',bg='black',fg= 'white')
    semat_lb.place(x=100, y= 100)

    seteam_lb = Label(root, text = 'Stage :',bg='black',fg= 'white')
    seteam_lb.place(x=100, y= 140)

    sestat_lb = Label(root, text = 'Team :',bg='black',fg= 'white')
    sestat_lb.place(x=100, y= 180)

    sepeople_lb = Label(root, text = 'Name :',bg='black',fg= 'white')
    sepeople_lb.place(x=100, y= 220)

    semat_cb = ttk.Combobox(root, values=matchVar, width=15, state="readonly")
    semat_cb.current()
    semat_cb.place(x=200, y= 100)
    semat_cb.bind("<<ComboboxSelected>>", people_on_sq)
 
    team_list = ['SQ1', 'SQ2', 'SQ3', 'SQ4', 'SQ5', 'SQ6', 'SQ7', 'SQ8', 'SQ9', 'SQ10', 'SQ11', 'SQ12', 'SQ13',
         'SQ14', 'SQ15', 'SQ16', 'SQ17', 'SQ18', 'SQ19', 'SQ20']

    sestat_cb = ttk.Combobox(root, values=list(range(1, 11)), width=15, state="readonly")
    sestat_cb.current()
    sestat_cb.place(x=200, y= 140)

    seteam_cb = ttk.Combobox(root, values=team_list, width=15, state="readonly")
    seteam_cb.current()
    seteam_cb.place(x=200, y= 180)
    seteam_cb.bind("<<ComboboxSelected>>", people_on_sq)

    vcmd = (root.register(notstr), '%S')
    addtime_en = Entry(root, bd = 3, width = 10,validate='key', vcmd= vcmd)
    addtime_en.place(x=480, y= 210)

    addscore_en = Entry(root,bd = 3, width = 10,validate='key', vcmd= vcmd)
    addscore_en.place(x=480, y= 130)

    root.mainloop()

###########แสดงผลการแข่งขัน#############
def report():
    #GUI
    global matchVar

    def funsion():
        s = select_type.get()
        if s == 'All contestants' :
            report1()
        elif s == 'Split stage, unordered' :
            report2()
        elif s == 'Split stage, split type' :
            report3()
        elif s == 'Classified, all stage included' :
            report4()

    def process(e):
        for i in range(10):
            conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
            c = conn.cursor()
            sql = '''SELECT hit_factor{} FROM {} ORDER BY hit_factor{} DESC LIMIT 1'''.format(i+1,select_match.get(),i+1)
            c.execute(sql)
            conn.commit()
            result = c.fetchall()
            for x in result:
                hitfac = x

            sql = '''UPDATE {} SET stage_point{}= ROUND((hit_factor{}/{})*50,4) '''.format(select_match.get(),i+1,i+1,hitfac[0])
            c.execute(sql)
            conn.commit()

            sql = '''SELECT stage_point{} FROM {} ORDER BY stage_point{} DESC LIMIT 1'''.format(i+1,select_match.get(),i+1)
            c.execute(sql)
            conn.commit()
            result = c.fetchall() 
            for x in result:
                point = x

            sql = '''UPDATE {} SET stage_percent{}= ROUND((stage_point{}/{})*100,2) '''.format(select_match.get(),i+1,i+1,point[0])
            c.execute(sql)
            conn.commit()

            sql = '''UPDATE {} SET sum_point= ROUND(stage_point1+stage_point2+stage_point3+stage_point4+stage_point5+stage_point6+stage_point7+stage_point8+stage_point9+stage_point10,4)'''.format(select_match.get())
            c.execute(sql)
            conn.commit()

            sql = '''SELECT sum_point FROM {} ORDER BY sum_point DESC LIMIT 1'''.format(select_match.get())
            c.execute(sql)
            conn.commit()
            result = c.fetchall() 
            for x in result:
                sumpoint = x

            sql = '''UPDATE {} SET percen = ROUND((sum_point/{})*100,2) '''.format(select_match.get(),sumpoint[0])
            c.execute(sql)
            conn.commit()

            c.close()

    def report1():
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()

        def update(result):
            #my_tree.insert('', 'end',values='Competitor-Listing-By-Competitor-Number')
            for x in result : 
                my_tree.insert('', 'end',values=x)
            
        root = Toplevel()
        root.title('Competitor Listing By Competitor Number')
        icon = PhotoImage(file = 'logo.png')
        root.iconphoto(False, icon)
        root.geometry("800x500")

        tree_frame =Frame(root)
        tree_frame.pack(pady=20 ,fill=BOTH, expand=1)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
        my_tree.pack(fill=BOTH, expand=1)
        my_tree['columns'] = (1,2,3,4)

        my_tree.column('#0', width=0)
        my_tree.column(1, width=10)
        my_tree.column(2, width=150)
        my_tree.column(3, anchor=CENTER, width=50)
        my_tree.column(4, anchor=W, width=50)

        my_tree.heading(1, text="ID")
        my_tree.heading(2, text="Name")
        my_tree.heading(3, text="Div")
        my_tree.heading(4, text="Sqd")

        sql_cmd = """select id,name,type,team from {}""".format(select_match.get())
        c.execute(sql_cmd)
        result = c.fetchall()
        update(result)

        tree_scroll.config(command=my_tree.yview)

        root.mainloop()

    def report2():
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()

        root = Toplevel()
        root.title('Score Verification By Stage')
        icon = PhotoImage(file = 'logo.png')
        root.iconphoto(False, icon)
        root.geometry("800x500")

        tree_frame =Frame(root)
        tree_frame.pack(pady=20 ,fill=BOTH, expand=1)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
        my_tree.pack(fill=BOTH, expand=1)
        my_tree['columns'] = (1,2,3,4)

        my_tree.column('#0', width=0)
        my_tree.column(1, width=10)
        my_tree.column(2, width=150)
        my_tree.column(3, anchor=CENTER, width=50)
        my_tree.column(4, anchor=W, width=50)

        my_tree.heading(1, text="ID")
        my_tree.heading(2, text="Name")
        my_tree.heading(3, text="PTS")
        my_tree.heading(4, text="Time")

        for i in range(10): 
            sql_cmd = """select id,name,PTS{},time{} from {}""".format(i+1,i+1,select_match.get())
            c.execute(sql_cmd)

            result = c.fetchall()
            my_tree.insert('', 'end',values='- Scores-For-Stage-{}'.format(i+1))
            for x in result : 
                my_tree.insert('', 'end',values=x)

        tree_scroll.config(command=my_tree.yview)

        root.mainloop()

    def report3():
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()

        root = Toplevel()
        root.title('Overall Stage Results ')
        icon = PhotoImage(file = 'logo.png')
        root.iconphoto(False, icon)
        root.geometry("800x500")

        tree_frame =Frame(root)
        tree_frame.pack(pady=20 ,fill=BOTH, expand=1)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
        my_tree.pack(fill=BOTH, expand=1)
        my_tree['columns'] = (1,2,3,4,5,6,7)

        my_tree.column('#0', width=0)
        my_tree.column(1, width=10)
        my_tree.column(2, width=15)
        my_tree.column(3, anchor=CENTER, width=20)
        my_tree.column(4, anchor=CENTER, width=20)
        my_tree.column(5, anchor=CENTER, width=20)
        my_tree.column(6, anchor=CENTER, width=10)
        my_tree.column(7, anchor=CENTER, width=100)

        my_tree.heading(1, text="PTS")
        my_tree.heading(2, text="TIME")
        my_tree.heading(3, text="HIS FACTOR")
        my_tree.heading(4, text="STAGE POINTS")
        my_tree.heading(5, text="STAGE PERCENT")
        my_tree.heading(6, text="#")
        my_tree.heading(7, text="COMPETITOR Name")

        for i in range(10): 
            sql_open = """select PTS{},time{},hit_factor{},stage_point{},stage_percent{},id,name from {} WHERE type='Open' ORDER BY stage_percent{} DESC """.format(i+1,i+1,i+1,i+1,i+1,select_match.get(),i+1)
            c.execute(sql_open)
            result = c.fetchall()

            my_tree.insert('', 'end',values='OPEN Stage-{} '.format(i+1))
            for x in result : 
                my_tree.insert('', 'end',values=x)

        for i in range(10) :
            sql_modify = """select PTS{},time{},hit_factor{},stage_point{},stage_percent{},id,name from {} WHERE type='Standard' ORDER BY stage_percent{} DESC """.format(i+1,i+1,i+1,i+1,i+1,select_match.get(),i+1)
            c.execute(sql_modify)
            result = c.fetchall()

            my_tree.insert('', 'end',values='STANDARD Stage-{} '.format(i+1))
            for x in result : 
                my_tree.insert('', 'end',values=x)

        for i in range(10) :
            sql_modify = """select PTS{},time{},hit_factor{},stage_point{},stage_percent{},id,name from {} WHERE type='Modify' ORDER BY stage_percent{} DESC """.format(i+1,i+1,i+1,i+1,i+1,select_match.get(),i+1)
            c.execute(sql_modify)
            result = c.fetchall()

            my_tree.insert('', 'end',values='MODIFY Stage-{} '.format(i+1))
            for x in result : 
                my_tree.insert('', 'end',values=x)

        for i in range(10) :
            sql_modify = """select PTS{},time{},hit_factor{},stage_point{},stage_percent{},id,name from {} WHERE type='Standard manual' ORDER BY stage_percent{} DESC """.format(i+1,i+1,i+1,i+1,i+1,select_match.get(),i+1)
            c.execute(sql_modify)
            result = c.fetchall()

            my_tree.insert('', 'end',values='STANDARD-MANUAL Stage-{} '.format(i+1))
            for x in result : 
                my_tree.insert('', 'end',values=x)

        tree_scroll.config(command=my_tree.yview)

        root.mainloop()

    def report4():
        conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
        c = conn.cursor()

        root = Toplevel()
        root.title('Overall Match Results')
        icon = PhotoImage(file = 'logo.png')
        root.iconphoto(False, icon)
        root.geometry("800x500")

        tree_frame =Frame(root)
        tree_frame.pack(pady=20 ,fill=BOTH, expand=1)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
        my_tree.pack(fill=BOTH, expand=1)
        my_tree['columns'] = (1,2,3,4)

        my_tree.column('#0', width=0)
        my_tree.column(1, width=20)
        my_tree.column(2, width=20)
        my_tree.column(3, anchor=CENTER, width=20)
        my_tree.column(4, anchor=CENTER, width=150)

        my_tree.heading(1, text="%")
        my_tree.heading(2, text="POINT")
        my_tree.heading(3, text="#")
        my_tree.heading(4, text="Competitor Name")

        def overall_match() :
            sql_open = """select percen,sum_point,id,name from {} WHERE type='Open' """.format(select_match.get())
            c.execute(sql_open)
            result = c.fetchall()

            my_tree.insert('', 'end',values='OPEN')
            for x in result : 
                my_tree.insert('', 'end',values=x)

            sql_standard = """select percen,sum_point,id,name from {} WHERE type='Standard' """.format(select_match.get())
            c.execute(sql_standard)
            result = c.fetchall()

            my_tree.insert('', 'end',values='STANDARD')
            for x in result : 
                my_tree.insert('', 'end',values=x)

            sql_modify = """select percen,sum_point,id,name from {} WHERE type='Modify' """.format(select_match.get())
            c.execute(sql_modify)
            result = c.fetchall()

            my_tree.insert('', 'end',values='MODIFY')
            for x in result : 
                my_tree.insert('', 'end',values=x)

            sql_sm = """select percen,sum_point,id,name from {} WHERE type='Standard manual' """.format(select_match.get())
            c.execute(sql_sm)
            result = c.fetchall()

            my_tree.insert('', 'end',values='STANDARD-MANUAL')
            for x in result : 
                my_tree.insert('', 'end',values=x)
        
        overall_match()

        tree_scroll.config(command=my_tree.yview)

        root.mainloop()

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

    ok_bt = Button(root, text = 'OK', width= 10,command=funsion)
    ok_bt.place(x=280, y=220)
    ok_bt.bind('<Button-1>',process)

    root.mainloop()


if __name__ == "__main__" :
    select_namematch()
    mainwindow()
    
