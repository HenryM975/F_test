from flask import Flask, render_template
app = Flask(__name__)


#try:
@app.route('/')
def index():
    #return '<h1> smth <h1>'
    return render_template('index.html')

@app.route('/link1')
def link_1():
    #return '<h1> smth <h1>'
    return render_template('link_1.html')

@app.route('/link2')
def link_2():
    #return '<h1> smth <h1>'
    return render_template('link_2.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')




    #@app.route('/index')
    #def findex():
        #return render_template('index.html')
#except:
    #@app.route('/')
    #def index():
        #return '<h1> Error <h1>', 400

if __name__ == '__main__':
    app.run(debug=True)
