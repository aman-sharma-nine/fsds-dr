from app import app 

@app.route("/about")
def about():
        return "This is a simple flask front end to generate predictions"

