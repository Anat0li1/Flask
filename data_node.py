from flask import request, Flask, make_response
app = Flask(__name__)

messages = []

@app.route('/receive')
def get_message():
    global messages
    temp = messages.pop(0)    #треба переробити щоб воно було або у файлі або на диску
    return temp
@app.post('/send')
def send_message():
    global messages 
    mes = request.data
    messages.append(mes)
    return make_response()
@app.route('/stats')
def stats():
    global messages
    return str(len(messages))

    