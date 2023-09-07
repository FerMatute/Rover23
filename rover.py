# ---- LIBRERIAS ----
import Adafruit_DHT
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time
from gpiozero import LED
import vlc
import os
import uvicorn
import serial
from fastapi.staticfiles import StaticFiles 


# ---- VARIABLES ----
app = FastAPI()

ser = serial.Serial(
	port='/dev/ttyACM0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>

  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <title>0</title>
    <style>
      body {{
        background-repeat: no-repeat;
        background-size: cover;  
        font-family: Arial, sans-serif;
        background-color: rgba(47, 175, 60, 0.4);
        margin: 0;
        padding: 0;
        border: 2px solid #B6F61A;
      }}

      .container {{
        max-width: 600px;
        margin: 0 auto;
        padding: 1px;
        background-color: rgba(47, 175, 60, 0.4);
        border-radius: 1px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      }}
      
      .h1 {{
        text-align: center;
      }}

      .button-container {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 20px;
        border: 5px solid #b8f61a00;
      }}

      .button-container button {{
        margin: 5px;
        border: 2px solid #b8f61a00;
      }}

      .text-container {{
        text-align: center;
        margin-top: 10px;
        border: 5px solid 
      }}
      #Botones {{
        color: #0099CC;
        background: transparent;
        border: 2px solid #0099CC;
        border-radius: 6px;
        border: none;
        color: white;
        padding: 16px 32px;
        text-align: center;
        display: inline-block;
        font-size: 20px;
        font-family: 'Lexend Deca', sans-serif;
        margin: 4px 2px;
        -webkit-transition-duration: 0.4s;
        /* Safari */
        transition-duration: 0.4s;
        cursor: pointer;
        text-decoration: none;
        text-transform: uppercase;
      }}

      #Botones {{
        background-color: white;
        color: black;
        border: 2px solid #b8f61a00;
      }}

      #Botones:hover {{
        background-color: #B6F61A;
        color: white;
      }}
      #dato {{
        font-family: 'Lexend Deca', sans-serif;
        font-size:35px;
        color: white;
      }}
      #base {{
        border: 5px solid #B6F61A;
        border-radius: 10px;
      }}
      

    </style>
    <script>
      function sendCommand(command) {{
        {{
          fetch("/command/" + command)
            .then(response => response.json())
            .then(data => console.log(data));
        }}
      }}
    </script>
  </head>

  <body>
    <h1><center>
      </center></h1>  
    <div class="columna1">
      <div id="base"class="container">
        <div class="button-container">
        <div class="button-container">
          <button id="Botones" onclick="sendCommand('up')">↑</button>
          <button id="Botones" onclick="sendCommand('down')">↓</button>
          <button id="Botones" onclick="sendCommand('detente')">||</button>
          <button id="Botones" onclick="sendCommand('left')">←</button>
          <button id="Botones" onclick="sendCommand('right')">→</button>
        </div>
      </div>
      <br>
    </div>
    <br>
    <br>
    <br>
  </body>

</html>
    """



@app.get("/command/{command}")
async def execute_command(command: str):

    if command == "down":
      ser.write(1)
      print('lol')

    elif command == "up":
      ser.write(1)
      print('lol')

    elif command == "detente":
      ser.write(1)
      print('lol')
      
    elif command == "left":
      ser.write(1)
      print('lol')

    elif command == "right":
      ser.write(1)
      print('lol')



    return {"message": f"Executing command: {command}"}
    

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8001)