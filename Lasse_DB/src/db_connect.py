import psycopg as pg

CONN = pg.connect(
    dbname = 'lasses_media',
    user = 'postgres',
    password = 'postgres'
)

class Insert:
    def __init__(self):
        self.conn = CONN
        self.cursor = CONN.cursor()
        self.media = "INSERT INTO media VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;"
        self.genre = "INSERT INTO genre VALUES (DEFAULT, %s, %s) RETURNING *;"
        self.type = "INSERT INTO media_type VALUES (DEFAULT, %s) RETURNING *;"
        self.platform = "INSERT INTO platform VALUES (%s,%s,%s) RETURNING *;"

    def media_in(self, data):
        self.cursor.execute(self.media, data)
        result = self.cursor.fetchone()
        self.conn.commit()
        return result
    
    def genre_in(self, data):
        self.cursor.execute(self.genre, data)
        result = self.cursor.fetchone()
        self.conn.commit()
        return result
    
    def type_in(self, data):
        self.cursor.execute(self.type, data)
        result = self.cursor.fetchone()
        self.conn.commit()
        return result
    
    def platform_in(self, data):
        self.cursor.execute(self.platform, data)
        result = self.cursor.fetchone()
        self.conn.commit()
        return result
    
class SelectAll:

    def __init__(self):
        self.cursor = CONN.cursor()
        self.select = "SELECT * FROM "

    def sel_from(self, where):
        self.cursor.execute(self.select+where)
        return self.cursor.fetchall()
    
class SelectByKey:

    def __init__(self):
        self.cursor = CONN.cursor()

    def id_sel(self, data):
        where = "id = %s;"
        self.cursor.execute(self.select+where, data)
        return self.cursor.fetchall()
    
    def genre_sel(self, data):
        query = """
        SELECT m.name, m.publisher, m.fsk, m.carrier_type, m.platform 
        FROM media AS m
        JOIN genre AS g ON m.genre_id = g.genre_id
        WHERE m.genre_id = %s;
"""
        self.cursor.execute(query, (data,))
        return self.cursor.fetchall()
    
    def type_sel(self, data):
        where = "type_id = %s;"
        self.cursor.execute(self.select+where, data)
        return self.cursor.fetchall()
    
    def platform_def(self, data):
        query ="""
        SELECT p.input_hardware, p.output_hardware
        FROM platform AS p
        WHERE p.platform = %s;
"""
        self.cursor.execute(query, (data,))
        return self.cursor.fetchall()
    
    def platform_sel(self, data):
        query = """
        SELECT m.name, m.publisher, m.fsk, m.carrier_type, g.genre_name 
        FROM genre AS g
        JOIN media AS m ON g.genre_id = m.genre_id
        JOIN platform AS p ON m.platform = p.platform
        WHERE m.platform = %s;
"""
        self.cursor.execute(query, (data,))
        return self.cursor.fetchall()
    
class MakeVisible:

    def __init__(self):
        self.cursor = CONN.cursor()

    def show_genre(self):
        query = "SELECT genre_id,genre_name FROM genre;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def show_type(self):
        query = "SELECT * FROM media_type;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def show_platform(self):
        query = "SELECT platform FROM platform;"
        self.cursor.execute(query)
        return self.cursor.fetchall()