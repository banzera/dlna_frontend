from flask import render_template
from dlna_frontend import dlna_frontend

@dlna_frontend.route('/')
def index():
	return render_template('index.html')
