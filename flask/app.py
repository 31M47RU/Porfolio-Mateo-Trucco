from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return redirect(url_for('bienvenido', nombre=nombre))
    return render_template('index.html')

@app.route('/bienvenido')
def bienvenido():
    nombre = request.args.get('nombre')
    return render_template('bienvenido.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
