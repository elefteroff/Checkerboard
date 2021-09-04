from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/')
def checkerboard():
    return render_template('index.html', num1 = 4, num2 = 4)

@app.route('/<int:x>')
def checkerboardx(x):
    return render_template('index.html', num1 = x, num2 = x)

# @app.route('/<int:x>/<int:y>')
# def checkerboardxy(x,y):
#     return render_template('index.html', num1 = x, num2 = y)


@app.route('/<int:x>/<int:y>')
def checkerboardxy(x,y):
    return render_template('index.html', num1 = x, num2 = y, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboardxy_color(x,y,color1, color2):
    return render_template('index.html', num1 = x, num2 = y, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)

