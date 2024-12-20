"""
uv sync
uv run main.py
"""
from tauripy import Tauri
from pathlib import Path
import json
from mjpeg_server import run_mjpg_server
import threading


def on_command(message: bytes):
    print(f"Received: {message.decode()}")
    return json.dumps({'message': 'Hello from Python!'}).encode()

dist_path = Path(__file__).parent.joinpath('dist')
tauric = Tauri("com.tauric.dev", "tauric")
tauric.mount_frontend(dist_path)
tauric.on_command(on_command)
threading.Thread(target=run_mjpg_server).start()
tauric.run(lambda: tauric.create_window("example_window", "tauric", "fs://index.html", maximized=False, center=True, width=500, height=400))
