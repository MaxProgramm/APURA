from flask import Flask, render_template, request, jsonify, send_file
import subprocess
from live import ProtokollLine, Case2
import json
from datetime import datetime
pythonScript = "main.py"

app = Flask(__name__)

message = ""

with open("config.json") as config_file:
    json_data = json.load(config_file)

ip = json_data["server_ip"]

# c1 = Case1(1)
c2 = Case2(1)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = subprocess.run(['python', pythonScript], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        return render_template('index.html', output=output)
    return render_template('index.html')


@app.route('/data')
def send_data():
    global message
    # with open("tempData.txt") as tempData:
        # message = tempData.read()
    result = c2.live_check()
    if result[0]:
        data = {'message': f"{result[1]}"}
    else:
        data = {"message": f"{message}"}

    # data = {'message': f"{message}"}
    return jsonify(data)


@app.route('/message', methods=['POST'])
def receive_data():
    global message
    # message = request.get_json().get('message')
    message = request.get_data(as_text=True)
    message = message.replace("\n", "")
    message = message.split(" ")
    message.__delitem__(0)
    message.__delitem__(0)
    message = " ".join(message)
    message = f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S')} {message}"

    print([message])
    c2.check(ProtokollLine(message))
    if message:
        return f"Received message: {message}"
    else:
        return "No message received."


@app.route("/live")
def live():
    return render_template("live.html", server_address=ip)


@app.route("/files/<string:filename>")
def get_src(filename):
    return send_file(f"files/{filename}")




if __name__ == '__main__':
    app.run(debug=True, host=ip)
