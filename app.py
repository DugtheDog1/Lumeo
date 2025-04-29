from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This will render the 'index.html' file located in the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    # Set host to '0.0.0.0' to allow access via a custom IP address or external interface
    app.run(host='0.0.0.0', port=5000, debug=True)
