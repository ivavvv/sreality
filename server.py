from flask import Flask, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect(host='db', dbname='srealitydb', user='postgres', password='12345') 
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM sreality_data")
    estates = cur.fetchall()
    return render_template('index.html', estates=estates)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
