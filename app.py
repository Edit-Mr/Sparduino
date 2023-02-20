import serial
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import serial.tools.list_ports

print("╦ 歡迎使用 Sparduino")
available_ports = serial.tools.list_ports.comports()
print("║")
# Print the list of available COM ports
print("╠ 目前可用接口:")
for port in available_ports:
    print("╠═ " + str(port))
print("║")
chosen_port = input("╚ 輸入數字: ")
ser = serial.Serial('COM' + chosen_port, 9600)

# Set up the Spotify API
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='',
                     client_secret='', redirect_uri='http://localhost:8888/callback', scope=scope))

while True:
    # Get the artist and title of the currently playing song on Spotify
    artist = ""
    title = ""
    try:
        current_track = sp.current_playback()
        if current_track is not None and current_track['is_playing']:
            artist = current_track['item']['artists'][0]['name']
            title = current_track['item']['name']
    except:
        artist = ""
        title = ""

    # Send the artist and title to the Arduino Uno over the serial port
    if artist and title:
        print("╔ "+artist + "\n╚ " + title)
        ser.write(("<"+artist + ">/" + title).encode())
    # Pause the loop for one second
    time.sleep(3)
