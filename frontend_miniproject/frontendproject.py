from flask import Flask
from flask import render_template
import csv

app = Flask(__name__) #<= creates an instance of a Flask server

@app.route("/") #<= defines our base URL
def index(): #<= this is the function tied to the decorator above
    email_list = []
    with open("/home/student/mycode/frontend_miniproject/emails.csv") as email_csv:
        reader = csv.reader(email_csv)
        for row in reader:
            email_list.append(row)
    return render_template("front_end_template2.html", email_list=email_list) #<= this should render the NEW template we just made above.
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
