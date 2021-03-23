import sqlite3

def add_people() :
    conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
    c = conn.cursor()
    try :
        Team = input('กรุณากรอกชื่อทีม :')
        Name = input('กรุณากรอกชื่อ :')
        Type = input('ประเภท\nOpen\nStandard\nModify\nStandard manual\nกรุณาเลือกประเภท :')
        sql = '''INSERT INTO table_data (id,Name_people,Type_people,Class_people,Team) VALUES (NULL,?,?,?,?)'''
        data = (Name,Type,"U",Team)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()

def delete_people() :
    conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
    c = conn.cursor()
    x = input('กรอกรหัสที่ต้องการลบ : ')
    try :
        c.execute('DELETE FROM table_data WHERE id = {}'.format(x))
        conn.commit()
        c.close()
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

def newmath() :
    conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
    c = conn.cursor()
    math = str(input('ป้อนชื่อแมทซ์ :'))
    try :
        c.execute ('''CREATE TABLE {}(
        id INTEGER,
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
        stage_percent10 REAL NULL)'''.format('Stage_'+math))
        conn.commit()

        # c.execute ('''INSERT INTO {} (id, name, type, team, class)
        # SELECT id, Name_people, Type_people, Team, Class_people
        # FROM table_data'''.format('Stage_'+math))

        # conn.commit()
        conn.close()
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

# def add_point() :
#     conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
#     c = conn.cursor()
#     try :
#         selete_math = input('เลือกแมทซ์ :')
#         #มาทำต่อเด้อออออออออ ไอ้ต้าว

if __name__ == "__main__":
    newmath()
    #add_people()