from flask import Flask, request, render_template
import psycopg2
import json

app = Flask(__name__)

conn = psycopg2.connect(database='kvmilos')

@app.route("/pokaz")
def pokaz():
    cur = conn.cursor()
    cur.execute("SELECT liczba FROM liczby")
    result = [row[0] for row in cur.fetchall()]
    return render_template('przyklad.html', x=result)

@app.route("/przyklad")
def przyklad():
    return render_template('przyklad.html', x=42)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/formularz")
def formularz():
    return """<HTML>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
<BODY>
Dzien dobry.<P>

<FORM action="sumuj" method=GET>
<P>Jak masz na imie <Input TYPE=Text Name="imie">

<P>Wpisz liczby do zsumowania: <Input TYPE=Text Name="x">
<Input TYPE=Text Name="y"><BR>
<Input TYPE=SUBMIT name="enter" value="Gotowe">
</FORM>
</BODY>
</HTML>"""

@app.route("/sumuj")
def sumuj():
    return "<p>Twoja suma wynosi: " + str((int(request.args.get('x')) + int(request.args.get('y'))))
