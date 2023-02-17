#Thank you anumitultrabots for helping me in this journey !
#Must Subscribe On YouTube @ajak4405 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@anumitultrabots'

if __name__ == "__main__":
    app.run()
