# ----- required imports -----

import subprocess
import sys
import os
import signal
from threading import Thread
from time import sleep

# ----- helper functions -----

def run_flask():
    flask_env = os.environ.copy()
    flask_env['FLASK_ENV'] = 'development'
    flask_env['FLASK_APP'] = 'app.py'
    flask_command = [
        sys.executable, '-m', 'flask', 'run',
        '--host=0.0.0.0',
        '--port=5000',
        '--reload'
    ]
    subprocess.run(flask_command, env=flask_env)

def run_react():
    react_dir = os.path.join(os.getcwd(), 'naobito-app')
    os.chdir(react_dir)
    if os.name == 'nt':
        subprocess.run(['npm.cmd', 'start'], shell=True)
    else:
        subprocess.run(['npm', 'start'], shell=True)

def main():
    flask_process = Thread(target=run_flask)
    react_process = Thread(target=run_react)
    flask_process.start()
    print('Starting Flask backend...')
    sleep(5)  
    react_process.start()
    print('Starting React frontend...')
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print('\nShutting down servers...')

# ----- execution code -----

if __name__ == '__main__':
    main()