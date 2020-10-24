import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int( os.getenv( 'PORT', 5000 ) )

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = port)
    
    