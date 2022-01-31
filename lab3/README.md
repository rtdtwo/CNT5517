# Lab 3 - Metronome Thing Implementation Using Raspberry Pi

## Server setup
1. In the folder part1, there is a file called `app.py`. This is the HTTP REST server. This also holds a `bl.py`.
file which holds the logic of our server.
2. Install the following dependencies using pip : `pip install Flask Flask_CORS`.
3. Run the `app.py` file using `python3 app.py`. On single terminal interfaces (like the Rpi), you can use `nohup python3 app.py &` which will not block the ongoing terminal session and allow you to run the RPi code as well.
4. Make sure `db.json` file is not empty. This holds the values of BPM. The default state is:
`{"current": 0, "min": 0, "max": 0}`
5. Copy the server URL, which should show up in the terminal window.
6. Paste this URL in the `BASE_SERVER_URL` of the Raspberry Pi code as well as the webpage code.

## Webpage setup
1. Simply open the HTML file in a browser.
2. Make sure the base server URL is updated from the process above.

## RPi setup
1. Install the following dependencies using pip
`pip install requests`
2. Run the file raspi.py in the Raspberry Pi console.
3. Make sure the base server URL is updated from the process above.

## Connections
![Connections](https://i.postimg.cc/gcRRGQxv/image.png)
