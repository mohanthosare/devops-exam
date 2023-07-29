from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
     return "<h1>welcome to ITIL exam</h1>"
     return "<h1>PRN number = 230344223028</h1>"
     return "<h1>Name = Mohan Thosare</h1>"
     return "<h1>phone number = 8855989893</h1>"
app.run(host="0.0.0.0", port=4000, debug=True)
