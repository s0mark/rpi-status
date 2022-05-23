from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import random

app = Flask(__name__)
CORS(app)

def rand(a, b, precision=2):
	return float(round(random.random() * (b - a) + a, 2))

def CPUtemp():
	return 42.0 + rand(-5.0, 5.0)

def GPUtemp():
	return 42.0 + rand(-5.0, 5.0)

def CPUusage():
	return 10.0 + rand(-8.0, 10.0)

def memusage():
	return [113401 + random.randint(-100000, 2000000), 3986748]

def storageusage():
	return [6998716, 28546725]

def topprocesses(args=None):
	names = ["alma", "korte", "banan", "eper", "szilva"]
	processes = []
	count = args[0] if args else 5
	for i in range(count):
		processes.append([i, names[i % 5], rand(0.5, 100.0 / count)])
	return processes

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
	return jsonify(list(map(lambda data: {"pid": data[0], "name": data[1], "usage": data[2]}, topprocesses(args))))
