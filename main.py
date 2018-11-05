from flask import Flask, render_template, request
import liveapi
app = Flask(__name__)

elemental_ip = '3.2.1.4'

@app.route("/")
@app.route("/index/")
def index():
	stage = 'index'
	return render_template('index.html', stage=stage)
    #return render_template('PageWithButton.html')

@app.route("/command_center/", methods=['GET', 'POST'])
def command_center():
	global elemental_ip
	if request.method == 'POST':
		if 'ip_button' in request.form: 			# If form for IP is pressed from index page
			stage = 'ip_in'
			elemental_ip = request.form['elemental_ip']
			return render_template('command_center.html', stage=stage, el_ip = elemental_ip)
		
@app.route("/cue_command/", methods=['GET', 'POST'])
def cue_command():
	global elemental_ip
	if request.method == 'POST':
			print(request.form)
			if 'start_cue_button' in request.form: 
				command = 'start_cue'
				print(command)
			if 'stop_cue_button' in request.form:
				command = 'stop_cue'
				print(command)
			
			response = liveapi.cue_command(elemental_ip, '17', command)
			#response = liveapi.stop_cue_point(elemental_ip, '17')
			return response
			
	
if __name__ == "__main__":
    app.run()