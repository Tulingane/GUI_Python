import sqlite3


# Call the database class
# Using the Class database is much more organize and it more easy
class Database:
    # We need a construct an initializer
    # the method self is going to take init which like .this in java or other languages
    def __init__(self, db):
        #let now create to a database
        self.conn = sqlite3.connect(db)
        #We are taking cursor to execute queries
        self.cur = self.conn.cursor()
        # Executing queries
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, parts text, customer text,retailer text, price text)"
        )
        # we have to commit this by
        self.conn.commit()

# crowd operation to fetch data

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        # let have a variable call have all the rows
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        # let do some protection to protect to sql injections
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?,?)",
                         (part, customer, retailer, price))
        # let commit
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id, ))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute(
            "UPDATE parts SET parts = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
            (part, customer, retailer, price, id))
        self.conn.commit()


# We have to have a distruct to

    def __del__(self):
        self.conn.close()

        # populate the database with some data
        # Let initiate the database
        #db = Database('store.db')
        #db.insert("Hard Drive", "Eric Omondi", "Apple", "240")
        #db.insert("Laptop", "Michael Olwindja", "Apple", "870")
        #db.insert("Phone", "Kevin Shabani", "Apple", "750")
        #db.insert("AirDrop", "Axellia Shabani", "Apple", "150")
        #db.insert("Apple Tv", "Thierry Ntab", "Apple", "400")
        #db.insert("Apple Watch", "Gorges Baf", "Apple", "450")
        #db.insert("Portable Projector", "Junior Liula", "Apple", "300")
