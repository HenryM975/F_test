from flask import Flask, render_template
app = Flask(__name__)



#try:
@app.route('/')
def index():
    #return '<h1> smth <h1>'
    return render_template('index.html')


    #@app.route('/index')
    #def findex():
        #return render_template('index.html')
#except:
    #@app.route('/')
    #def index():
        #return '<h1> Error <h1>', 400

if __name__ == '__main__':
    app.run(debug=True)