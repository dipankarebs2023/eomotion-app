from flask import Flask
import subprocess

app = Flask(__name__)

# Route for the Streamlit app
@app.route('/')
def run_streamlit():
    # Run the Streamlit app as a subprocess
    subprocess.run(["streamlit", "run", "music.py"])
    return "Streamlit app is running"

if __name__ == '__main__':
    app.run()