# tauripy-rtsp

Show rtsp stream in the webview with tauripy

Videos from https://gist.github.com/jsturgis/3b19447b304616f18657

```console
# Start media rtsp server
docker run --rm -it -p 8554:8554 bluenviron/mediamtx:latest
# Stream from video.mp4 to media rtsp server
wget http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4 -O video.mp4
ffmpeg -re -stream_loop -1 -i video.mp4 -c copy -f rtsp -rtsp_transport tcp rtsp://127.0.0.1:8554/stream
# Play
uv sync
uv run src/main.py
```

Also you can play with 

```console
ffplay -rtsp_transport tcp rtsp://localhost:8554/stream
```