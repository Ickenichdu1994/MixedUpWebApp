from flask import Flask, url_for, request, render_template
import mysql.connector


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    name = ''
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')

    return 'Hello ' + name + '!'



@app.route('/uber-uns')
def uber_uns():
    return render_template('uber-uns.html')

@app.route('/button_clicked ')
def button_clicked():
    return render_template("datenbank.html")


@app.route('/datenbank', methods=["POST", "GET"])
def datenbankb():
    if request.method == "POST":
        selected_spirit = request.form["selected_spirit"]
        selected_ingredient_1 = request.form["selected_ingredient_1"]
        selected_ingredient_2 = request.form["selected_ingredient_2"]
        selected_ingredient_3 = request.form["selected_ingredient_3"]
        return print(selected_spirit,selected_ingredient_1,selected_ingredient_2,selected_ingredient_3)

    conn = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    cursor = conn.cursor()
    cursor.execute>("SELECT * FROM example_table")
    data = cursor.fetchall()
    conn.close()
    return render_template("datenbank.html", data=data)

    


if __name__== '__main__':
    app.run(port=5000, debug=True)

