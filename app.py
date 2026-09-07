from flask import Flask, render_template, request
from detector import analyze_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    user_text = ""
    if request.method == "POST":
        user_text = request.form.get("message", "")
        if user_text:
            result = analyze_message(user_text)
            
    return render_template("index.html", result=result, text=user_text)

if __name__ == "__main__":
    app.run(debug=True)