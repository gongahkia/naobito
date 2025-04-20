# ----- required imports -----

import subprocess
import sys
import os
from threading import Thread
from time import sleep

# ----- helper functions -----

def run_flask():
    backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "backend"))
    flask_env = os.environ.copy()
    flask_env["FLASK_APP"] = "app.py"
    flask_env["FLASK_ENV"] = "development"
    subprocess.run(
        [sys.executable, "-m", "flask", "run", 
         "--host=0.0.0.0", "--port=5000", "--reload"],
        cwd=backend_dir,
        env=flask_env
    )

def run_react():
    react_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "naobito-app"))
    npm = "npm.cmd" if os.name == "nt" else "npm"
    subprocess.run(
        [npm, "start"],
        cwd=react_dir
    )

def main():
    flask_thread = Thread(target=run_flask)
    react_thread = Thread(target=run_react)
    flask_thread.start()
    print("🟢 Starting Flask backend...")
    sleep(3)  
    react_thread.start()
    print("🟢 Starting React frontend...")
    try:
        flask_thread.join()
        react_thread.join()
    except KeyboardInterrupt:
        print("\n🔴 Shutting down servers...")

# ----- execution code -----

if __name__ == "__main__":
    main()