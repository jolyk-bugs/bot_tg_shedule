import sqlite3
def get_lessons(bot, message, cls, day):
    if cls == 0:
        bot.send_message(message.chat.id, "ОшибОчка, попробуй заново, "
                                          "написав команду /menu")
    else:
        conn = sqlite3.connect("schedule2.db")
        cur = conn.cursor()
        cur.execute("select lessons from schedule where class=? and day=?", (cls, day))
        rows = cur.fetchall()
        if rows == []:
            bot.send_message(message.chat.id, "Занятий нет")
        else:
            bot.send_message(message.chat.id, rows)
        conn.close()
