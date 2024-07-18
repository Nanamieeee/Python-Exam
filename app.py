from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        volume = float(request.form['radius'])
        volume1 = round(volume / 2.64, 2)
        volume2 = round(volume / 1.10, 2)
        volume3 = round(volume / 2.63, 2)
        volume4 = round(volume * 2.44, 2)
        volume5 = round(volume * 1.06, 2)
        volume6 = round(volume / 1.103, 2)
        volume7 = round(volume * 1.133, 2)
        return render_template('index.html', volume=volume, volume1=volume1, volume2=volume2,
                               volume3=volume3, volume4=volume4, volume5=volume5, volume6=volume6, volume7=volume7)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
