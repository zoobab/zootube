# ZooTube, a web server to play Youtube in Audio only

## Screenshots

## Dependencies

* youtube-dl
* flask

## Run

```
soft/zootube $ ./run.sh
 * Serving Flask app "zootube.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
[youtube] k6s1-caKRtQ: Downloading webpage
[info] Writing video description metadata as JSON to: k6s1-caKRtQ.mp3.info.json
[youtube] k6s1-caKRtQ: Downloading thumbnail ...
[youtube] k6s1-caKRtQ: Writing thumbnail to: k6s1-caKRtQ.jpg
[download] Destination: k6s1-caKRtQ.mp3
[download] 100% of 2.88MiB in 00:00
[ffmpeg] Post-process file k6s1-caKRtQ.mp3 exists, skipping
[INFO] Serving file...
127.0.0.1 - - [29/Dec/2020 19:38:01] "GET /api?yid=k6s1-caKRtQ HTTP/1.1" 200 -
[youtube] k6s1-caKRtQ: Downloading webpage
[info] Writing video description metadata as JSON to: k6s1-caKRtQ.mp3.info.json
[youtube] k6s1-caKRtQ: Downloading thumbnail ...
[youtube] k6s1-caKRtQ: Writing thumbnail to: k6s1-caKRtQ.jpg
[download] k6s1-caKRtQ.mp3 has already been downloaded
[download] 100% of 2.88MiB
[ffmpeg] Post-process file k6s1-caKRtQ.mp3 exists, skipping
[INFO] Serving file...
127.0.0.1 - - [29/Dec/2020 19:38:03] "GET /api?yid=k6s1-caKRtQ HTTP/1.1" 200 -
127.0.0.1 - - [29/Dec/2020 19:38:04] "GET /favicon.ico HTTP/1.1" 404 -

```
