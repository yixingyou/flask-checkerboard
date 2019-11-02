from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
#def hello_world():
 #   return render_template('index.html')
@app.route('/<x>')
@app.route('/<x>/<y>')
def h_expand(x=8,y=8):
    return render_template("index.html", x_count=int(x), y_count=int(y))
#	return 'Dojo'
#@app.route('/say/<name>')
#def say(name):
#	return "Hello, "+name
#@app.route('/repeat/<int:num>/<str>')
#def repeat(num, str):
#   return str*int(num)
#@app.route('/play')
#def play():
#	return render_template('play.html')
#@app.route('/play/<times>')
#def displaytimes(times):
#	return render_template('play.html', num_times=int(times))
#@app.route('/play')
#@app.route('/play/<num>')
#@app.route('/play/<num>/<color>')
#def displaycolor(num=3, color='blue'):
#	return render_template('play.html', num=int(num),color=color)#}
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.Git
