import json
from flask import Flask, g, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/actions', methods=['GET'])
def list_actions():
    data = get_db().execute("SELECT datetime(date, 'unixepoch'), amount, datetime(delayed_until, 'unixepoch') FROM entries ORDER BY date DESC").fetchall()
    return render_template('llistat.html', dades=data)

@app.route('/settings', methods=['GET', 'POST'])
def list_settings():
    with open('../config.json', 'r') as content_file:
        content = content_file.read()
    config = json.loads(content)
    alert = ''
    if request.method == 'POST':
        config['action'] = request.form['action'];
        config['origin'] = request.form['origin'];
        config['destination'] = request.form['destination'];
        config['quantity'] = request.form['quantity'];
        config['delay'] = request.form['delay'];
        new_settings = json.dumps(config)
        with open('../config.json', 'w') as content_file:
            content_file.write(new_settings)
        alert = "Settings have been updated successfully!"
    return render_template('settings.html', settings=config, al=alert)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE).cursor()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)