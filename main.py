from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():

  return render_template('index.html')

@app.route('/db', methods=['POST', 'GET'])

def shish():

  if request.method == 'GET':

    msg = "Response!"

    print("SENT >>>", msg)

    return msg

  print("RECEIVED >>>",list(request.form))

  return render_template('index.html')

if __name__ == '__main__':

  app.run()
