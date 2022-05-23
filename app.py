from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

SCRIPT_DIR = "scripts/"

def execute(command, args=None):
	arguments = ""
	if args:
		arguments = " " + " ".join(list(map(str, args)))
	return os.popen("bash " + SCRIPT_DIR + command + arguments).read()

def CPUtemp():
	return float(execute("cputemp.sh"))

def GPUtemp():
	return float(execute("gputemp.sh"))

def CPUusage():
	return float(execute("cpuusage.sh"))

def memusage():
	return list(map(int, execute("memusage.sh").split(" ")))

def storageusage():
	return list(map(int, execute("storageusage.sh").split(" ")))

def process(strtriplet):
	triplet = strtriplet.strip().split(" ")
	return (int(triplet[0]), triplet[1], float(triplet[2]))

def topprocesses(args=None):
	return list(map(process, execute("topproc.sh", args).split("#")[:-1]))

@app.route('/')
def statusOk():
	return jsonify({'status': "ok"})

@app.route('/temp')
def temp():
	return jsonify({'cpu': CPUtemp(), 'gpu': GPUtemp()})

@app.route('/temp/cpu')
def tempcpu():
	return jsonify({'temp': CPUtemp()})

@app.route('/temp/gpu')
def tempgpu():
	return jsonify({'temp': GPUtemp()})

@app.route('/usage')
def usage():
	memdata = memusage()
	storagedata = storageusage()
	return jsonify({
		'cpu': CPUusage(),
		'memory': {
			'used': memdata[0],
			'total': memdata[1]
		},
		'storage': {
			'used': storagedata[0],
			'total': storagedata[1]
		}
	})

@app.route('/usage/cpu')
def usagecpu():
	return jsonify({'usage': CPUusage()})

@app.route('/usage/memory')
def usagememory():
	data = memusage()
	return jsonify({'used': data[0], 'total': data[1]})

@app.route('/usage/storage')
def usagestorage():
	data = storageusage()
	return jsonify({'used': data[0], 'total': data[1]})

@app.route('/top')
def top():
	count = request.args.get('n')
	args = [int(count)] if count else None
	return jsonify(list(map(lambda data: {'pid': data[0], 'name': data[1], 'usage': data[2]}, topprocesses(args))))
