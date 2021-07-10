from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/download')
def download_file():
    return send_file('resume.pdf',as_attachment=True)

if __name__ == '__main__':
    app.run()
