from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/data/<path:path>')
def data(path):
    return send_from_directory('/Users/mikko/Documents/GitHub/talos/test_latest', path)

if __name__ == "__main__":
    app.run()