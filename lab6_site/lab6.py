import cherrypy as cherrypy
from peewee import *


DB_INSTANCE = SqliteDatabase("lab6_site/lab_data.db")
CP_CFG = {      
            '/':{
                'tools.staticdir.on': True,
                'tools.staticdir.dir': '/home/hexumee/Документы/Code Projects/AppDevLabs/lab6_site'
            }
         }

class BaseModel(Model):
    class Meta:
        database = DB_INSTANCE


class Lab(BaseModel):
    class Meta:
        db_table = "posts"

    idx = PrimaryKeyField(unique=True)
    name = TextField()
    text = TextField()
    likes = IntegerField()

    def get_columns(self):
        cursor = DB_INSTANCE.cursor()
        cursor.execute('PRAGMA table_info("posts")')
        
        return [i[1] for i in cursor.fetchall()]

    def get_rows(self):
        cursor = DB_INSTANCE.cursor()
        cursor.execute("SELECT * from posts")
        records = cursor.fetchall()

        return records
    
    def _update(self, indx, nname, ntext, nlikes):
        lab = Lab.get(idx=indx)
        lab.name = nname
        lab.text = ntext
        lab.likes = nlikes
        lab.save()

    def _add(self, nname, ntext):
        Lab(name=nname, text=ntext, likes=0).save()

class Page(object):
    columns = ""
    rows = ""

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows

    @cherrypy.expose
    def index(self):
        return f'''
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Lab6</title>
                        <link href="style.css" rel="stylesheet"/>
                    </head>
                        <body>
                            <h1>Лабораторная работа №6</h1>
                            <table>
                                <tr>
                                    {self.columns}
                                </tr>   
                                    {self.rows}
                            </table>
                        </body>
                </html>
                '''


if __name__ == '__main__':
    DB_INSTANCE.create_tables([Lab])
    app = Lab()
    # app._add("qwertyuiop", "Example Message")
    # app._update(4, "helloworld", "HeHeHe", 12345)

    columns = app.get_columns()
    rows = app.get_rows()

    columns_html = "".join([f"<th>{i}</th>" for i in columns])
    rows_html = ""

    for row in rows:
        rows_html += "<tr>"
        for item in row:
            rows_html += "<td>"
            rows_html += str(item)
            rows_html += "</td>"
        rows_html += "</tr>"

    cherrypy.quickstart(Page(columns_html, rows_html), "/", config=CP_CFG)
    
    DB_INSTANCE.close()

