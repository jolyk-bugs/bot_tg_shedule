import sqlite3
conn = sqlite3.connect("schedule2.db")
cur = conn.cursor()
cur.execute("drop table if exists schedule")
# создаем таблицу
cur.execute("create table if not exists schedule (id INT PRIMARY KEY, class INT, "
            "day CHAR, lessons CHAR)")
# вставляем данные
schedule = (
    (1, 9, 'ПН', '1. Математика\n2. Русский язык'),
    (2, 9, 'ВТ', '1. Литература\n2. Русский язык'),
    (3, 9, 'СР', '1. Физкультура\n2. Английский язык'),
    (4, 9, 'ЧТ', 'Это четверг'),
    (5, 9, 'ПТ', '1. Физкультура\n2. Английский язык')
)

for i in schedule:
    cur.execute("insert into schedule values (?, ?, ?, ?)", i)

# выбераем данные
# cur.execute("select * from schedule")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

conn.commit()
conn.close()
