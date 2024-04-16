from flask import Flask, render_template, request, jsonify
from flask_caching import Cache




app = Flask(__name__)
cache = Cache(app,config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 30000
} )



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update_settings', methods=['POST'])
def update_settings():
    device = int(request.form.get('device'))
    drain = int(request.form.get('drain'))
    humidity = int(request.form.get('humidity'))
    cache.set("humidity" , humidity)
    cache.set("drain", drain)
    cache.set("device", device)
    #humidity = cache.get("humidity")

    print(humidity)
    return 'Settings updated successfully' 


@app.route('/get_value', methods=['GET'])
def get_value():
    humidity_from_cache = cache.get("humidity")
    device_from_cache = cache.get("device")
    drain_from_cache = cache.get("drain")
    print(humidity_from_cache)
    return jsonify({'value': humidity_from_cache, 'value2': device_from_cache, 'value3': drain_from_cache}  )