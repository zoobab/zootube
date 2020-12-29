from flask import Flask, request, send_file
import os
app = Flask(__name__)

@app.route('/')
def index():
    return '<meta name="viewport" content="width=device-width, initial-scale=1.0"><center><h1>Welcome to Zootube!</h1>\n<i>Youtube audio only</i><br>Example: <a href="/api?yid=k6s1-caKRtQ">k6s1-caKRtQ</a></center>'

@app.route('/api')
def myimage():
    yid = request.args.get('yid', type = str)
    ext = 'mp3'
    filename = yid + '.' + ext
    if os.path.isfile(filename):
        print ("[INFO] File " + filename + " already exist, not redownloading...")
    else:
        os.system('youtube-dl --write-info-json --write-thumbnail --audio-format ' + ext + ' -x -o ' + filename + ' ' + yid)
    print '[INFO] Serving file...'
    return send_file(filename, mimetype='audio/mp3', as_attachment=False)
