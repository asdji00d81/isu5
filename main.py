# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Congratulations,it's a web app!"
@app.route("/hi")
def who():
    return"Congratulations, this is another way to show HIII!!!!!"

if __name__=="__main__":
    app.run()
