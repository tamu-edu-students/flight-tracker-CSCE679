from flask import Flask, jsonify, request, session, render_template
import live
import time
import linegraph
import flightmap
import pandas as pd

history = []
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

@app.route('/history') #, methods=['POST'])
def history_tofind():
    ip = request.remote_addr
    print(ip)
    print(history)
    print(len(history))
    history_to_send = []
    for i in range(len(history)):
        if history[i][6] == ip:
            history_to_send.append(history[i])
            print("Added")
            if len(history_to_send) == 5:
                break
    
    return jsonify(history_to_send, 200)


# @app.route('/getflightprice') #, methods=['POST'])
# def getflightprice():
#     return jsonify(live.getFlightPrice())
@app.route('/getdata', methods=['POST'])
def getdata():
    form_data = request.form
    print(form_data)
    src = request.form["src"]
    dst = request.form['dst']
    date = request.form['date']
    passengers = request.form['passengers']
    cabinClass = request.form['cabinClass']
    budget = request.form['budget']
    tmp_history = []
    tmp_history.append(src)
    tmp_history.append(dst)
    tmp_history.append(date)
    tmp_history.append(passengers)
    tmp_history.append(cabinClass)
    tmp_history.append(budget)
    tmp_history.append(request.remote_addr)
    image_name = linegraph.generate_linegraph(src, dst)
    srcSkyId, srcEntityId = live.searchAirport(src, 1)
    time.sleep(1)
    dstSkyId, dstEntityId = live.searchAirport(dst, 2)
    # dstId, dstEntityId = live.searchAirport(dst)
    # return jsonify(src_data, 200)
    time.sleep(1)
    flight_data = live.searchFlights(srcSkyId, dstSkyId, srcEntityId, dstEntityId, date, passengers,cabinClass)
    processed_data = live.process_flight_data(src, dst, flight_data, budget)
    print(processed_data)
    if len(processed_data) == 0:
        html_path = None
        print("empty list")
    else:
        processed_data = pd.DataFrame(processed_data, columns=['city1', 'city2', 'time', 'airlines', 'fare'])
        print(processed_data)
        html_path = flightmap.generate_map_html(processed_data)

    tmp_history.append(image_name)
    tmp_history.append(html_path)
    print(tmp_history)
    history.append(tmp_history)
    print(history)
    return jsonify({"historical_file":image_name, "map_path":html_path}, 200)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)