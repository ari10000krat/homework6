from flask import Flask, request, redirect, render_template
import urllib3

app = Flask(__name__)


def parse(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return r


@app.route('/')
def index():
    statisticsArr = [
        ['Age group', 'IFR'],
        ['0–19', '0.002%–0.01%'],
        ['20–49', '0.007%–0.03%'],
        ['50–69', '0.25%–1.0%'],
        ['70+', '2.8%–9.3%'],
    ]
    return render_template('index.html', statisticsArr=statisticsArr)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/', methods=['POST', 'GET'])
def contact():  # TODO Если не получиться с БД оптимизировать код
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        comment = request.form['comment']
        with open('data.txt', 'w')as f:
            f.write(f'firstname={firstname}\n'
                    f'lastname={lastname}\n'
                    f'username={username}\n'
                    f'city={city}\n'
                    f'state={state}\n'
                    f'zip={zip}\n'
                    f'comment={comment}\n')
        return redirect('/')
    else:
        return render_template('contact.html')


@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('error500.html'), 500


if __name__ == '__main__':
    app.run()
