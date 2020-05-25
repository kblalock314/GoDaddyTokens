from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["response"]
        link = str(url.replace('https://www.', ''))
        path = link.replace('/','%2F')
        return redirect(url_for("url", u=path))
    else:
        return render_template("index.html")


@app.route("/<u>")
def url(u):
    u = str(u)
    r = str('([@T[link:&lt;relative path="')
    t = str('"/&gt;]@T])')
    x = r + u + t
    d = str(x.replace('%2F','/'))
    return f"<h1>Your token is:</h1>{d}"


if __name__ == "__main__":
    app.run(debug=True)
