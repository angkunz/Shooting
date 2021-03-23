import sqlite3
conn = sqlite3.connect(r"C:\Users\qqx99\Documents\Python_project\Shooting_range2\main.db")
c = conn.cursor() #create a cursor object 
#c.execute ('''INSERT INTO data2(id, name, type) SELECT id, Name_people, Type_people FROM table_data WHERE Class_people = "U"''')
# c.execute ('''CREATE TABLE name1(id integer PRIMARY KEY AUTOINCREMENT,
#     Name_people varchar(40) NOT NULL,
#     Type_people varchar(10) NOT NULL,
#     Class_people varchar(1) NOT NULL)''')

c.execute('''INSERT INTO PP123(id,name,type,team,class,sum_point,percen,PTS1,time1,hit_factor1,stage_point1,stage_percent1,PTS2,time2,hit_factor2,stage_point2,stage_percent2,PTS3,time3,hit_factor3,stage_point3,stage_percent3,PTS4,time4,hit_factor4,stage_point4,stage_percent4,PTS5,time5,hit_factor5,stage_point5,stage_percent5,PTS6,time6,hit_factor6,stage_point6,stage_percent6,PTS7,time7,hit_factor7,stage_point7,stage_percent7,PTS8,time8,hit_factor8,stage_point8,stage_percent8,PTS9,time9,hit_factor9,stage_point9,stage_percent9,PTS10,time10,hit_factor10,stage_point10,stage_percent10) SELECT (NULL,name,type,team,class,sum_point,percen,PTS1,time1,hit_factor1,stage_point1,stage_percent1,PTS2,time2,hit_factor2,stage_point2,stage_percent2,PTS3,time3,hit_factor3,stage_point3,stage_percent3,PTS4,time4,hit_factor4,stage_point4,stage_percent4,PTS5,time5,hit_factor5,stage_point5,stage_percent5,PTS6,time6,hit_factor6,stage_point6,stage_percent6,PTS7,time7,hit_factor7,stage_point7,stage_percent7,PTS8,time8,hit_factor8,stage_point8,stage_percent8,PTS9,time9,hit_factor9,stage_point9,stage_percent9,PTS10,time10,hit_factor10,stage_point10,stage_percent10) FROM test1 ''') 


# c.execute('''INSERT INTO name(id,Name_people,Type_people,Class_people) VALUES (NULL,"Akaradech","open","U")''')
#c.execute('''INSERT INTO users VALUES (NULL,"dodd","dukdik","dodikza")''')
conn.commit() #save (commit) the change
conn.close() #close the connecton when done

