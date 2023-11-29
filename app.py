from flask import Flask, jsonify, request, session, render_template
import live
import time

# live.get_languages()
app = Flask(__name__)

@app.route('/', methods=['GET']) #, methods=['POST'])
def homepage():
    return render_template("home.html")

@app.route('/login') #, methods=['POST'])
def login():
    return "Hello"

@app.route('/language') #, methods=['POST'])
def language():
    return jsonify(live.get_languages())


@app.route('/getflight') #, methods=['POST'])
def flight():
    return jsonify(live.query_flight())

@app.route('/getNearestAirport') #, methods=['POST'])
def airportsearch():
    return jsonify(live.getNearestAirport())


# @app.route('/getflightprice') #, methods=['POST'])
# def getflightprice():
#     return jsonify(live.getFlightPrice())
@app.route('/getdata')
def getdata():
    src = request.form['src']
    dst = request.form['dst']
    date = request.form['date']
    passengers = request.form['passengers']
    cabinClass = request.form['cabinClass']
    budget = request.form['budget']
    srcSkyId, srcEntityId = live.searchAirport(src)
    time.sleep(1)
    dstSkyId, dstEntityId = live.searchAirport(dst)
    # dstId, dstEntityId = live.searchAirport(dst)
    # return jsonify(src_data, 200)
    time.sleep(1)
    flight_data = live.searchFlights(srcSkyId, dstSkyId, srcEntityId, dstEntityId, date, passengers,cabinClass)
    live.process_flight_data(src, dst, flight_data, budget)
    return jsonify(flight_data)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)