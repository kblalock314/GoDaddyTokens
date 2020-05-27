from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["response"]
        validurls = ["godaddy.com", "http://www.godaddy.com", "http://godaddy.com", "http://godaddy.com/",
                     "https://www.godaddy.com/", "https://www.godaddy.com", "www.godaddy.com", "www.godaddy.com/"]

        if url in validurls:
            return redirect(url_for("url", u="%2F"))

        for c in validurls:
            if c in url:
                link = url.split('.com/')
                path = link[1]
                append = path.replace('/', '%2F')
                return redirect(url_for("url", u=append))
        else:
            return f"Please enter a valid link"

    return render_template("index.html")

@app.route("/<u>")
def url(u):
    u = str(u)
    r = str('([@T[link:<relative path="')
    t = str('"/>]@T])')
    x = r + u + t
    token = str(x.replace('%2F','/'))

    return render_template("token.html", token=token)


if __name__ == "__main__":
    app.run(debug=True)
