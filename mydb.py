import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS expense_record (item_name text, item_price float, purchase_date date, budget_price float)")
        self.conn.commit()

    def fetchRecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insertRecord(self, item_name, item_price, purchase_date, budget_price):
        self.cur.execute("INSERT INTO expense_record VALUES (?, ?, ?, ?)",
                         (item_name, item_price, purchase_date, budget_price))
        self.conn.commit()

    def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid,))
        self.conn.commit()

    def updateRecord(self, item_name, item_price, purchase_date, budget_price, rid):
        self.cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ?, budget_price = ? WHERE rowid = ?",
                        (item_name, item_price, purchase_date, budget_price, rid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
