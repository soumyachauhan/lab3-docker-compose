from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def log_request():
    with open("app.log", "a") as log_file:
        log_file.write(f"Request received at {datetime.datetime.now()}\n")
    return "Logged request!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
