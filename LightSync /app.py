from flask import Flask, render_template

app = Flask(__name__, static_folder='Static')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')  # This will load the HTML template from the templates folder

if __name__ == "__main__":
    app.run(debug=True)
