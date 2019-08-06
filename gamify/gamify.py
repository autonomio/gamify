from flask import Flask, render_template, request, send_from_directory

import os
import glob
import json

app = Flask(__name__)


def get_experiment_info():

	experiment_path = app.config.get('experiment_path')
	list_of_files = glob.glob(experiment_path + '/*.csv')
	experiment_ids = [i.split('/')[-1].replace('.csv', '') for i in list_of_files]

	return experiment_ids, experiment_path


@app.route("/", methods=['GET'])
@app.route("/overview", methods=['GET'])
def overview():
	return render_template('overview.html',
						   experiment_ids=json.dumps(get_experiment_info()[0]))

@app.route("/analyze", methods=['GET'])
def analyze():
	return render_template('analyze.html',
						   experiment_ids=json.dumps(get_experiment_info()[0]))

@app.route("/experiment_log", methods=['GET'])
def experiment_log():
	return render_template('experiment_log.html',
						   experiment_ids=json.dumps(get_experiment_info()[0]))

@app.route("/live_monitoring", methods=['GET'])
def live_monitoring():
	return render_template('live_monitoring.html',
						   experiment_ids=json.dumps(get_experiment_info()[0]))

@app.route('/data/<path:path>')
def data(path):
    return send_from_directory(get_experiment_info()[1], path)

@app.after_request
def add_header(r):

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'

    return r

if __name__ == "__main__":

	import sys

	try:
		app.config['experiment_path'] = sys.argv[1]
	except IndexError:
		app.config['experiment_path'] = '.'

	app.config.update(TEMPLATES_AUTO_RELOAD = True)
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	app.run(debug=True)
