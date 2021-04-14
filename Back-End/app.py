from flask import Flask, render_template


app = Flask(__name__)

@app.route("../Front-End/HTML")
def main():
    return render_template('/Home.html')

if __name__ == "__main__":
    app.run()
