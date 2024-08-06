from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

timers = {}

def get_current_time()
    return int(time.time())

@app.route('timers', methods=['GET'])
def list_timers()
    return jsonify(timers)

@app.route('timerstimer_id', methods=['POST'])
def update_timer(timer_id)
    data = request.json
    if timer_id not in timers
        return jsonify({error Timer not found}), 404
    
    if 'action' in data
        action = data['action']
        if action == 'start'
            timers[timer_id]['start'] = get_current_time()
            timers[timer_id]['paused'] = False
        elif action == 'pause'
            timers[timer_id]['pause_time'] = get_current_time()
            timers[timer_id]['paused'] = True
        elif action == 'reset'
            timers[timer_id]['start'] = get_current_time()
            timers[timer_id]['pause_time'] = None
            timers[timer_id]['paused'] = False
        elif action == 'stop'
            timers[timer_id]['stop_time'] = get_current_time()
            timers[timer_id]['paused'] = True
        else
            return jsonify({error Invalid action}), 400
    
    return jsonify(timers[timer_id])

@app.route('timerstimer_id', methods=['DELETE'])
def delete_timer(timer_id)
    if timer_id in timers
        del timers[timer_id]
        return jsonify({status Timer deleted})
    return jsonify({error Timer not found}), 404

@app.route('timers', methods=['POST'])
def create_timer()
    timer_id = str(len(timers) + 1)
    timers[timer_id] = {
        'start' None,
        'pause_time' None,
        'stop_time' None,
        'paused' False
    }
    return jsonify({id timer_id}), 201

if __name__ == '__main__'
    app.run(host='0.0.0.0', port=5000)
