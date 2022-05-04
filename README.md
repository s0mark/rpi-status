# rpi-status
A simple flask web application to make basic system status info of a Raspberry Pi accessible in JSON format, through HTTP GET requests.

# Usage
The application requires the following tools to be installed to work properly: `flask`, `vcgencmd`.

To run the application, execute the `flask run` command in the root directory of the project.

# Description
The application offers the following system info about the Raspberry Pi:
| Path | Information | Format |
| --- | --- | --- |
| /temp | CPU and GPU temperature | `{"cpu": <temp>, "gpu": <temp>}` |
| /temp/cpu | CPU temperature | `{"temp": <temp>}` |
| /temp/gpu | GPU temperature | `{"temp": <temp>}` |
| /usage | CPU usage percentage, available and total memory and storage in bytes | `{"cpu": <usage>, "memory": {"total": <size>, "used": <size>}, "storage": {"total": <size>, "used": <size>}}` |
| /usage/cpu | CPU usage percentage | `{"usage": <usage>}` |
| /usage/memory | Available and total memory in bytes | `{"total": <size>, "used": <size>}` |
| /usage/storage | Available and total storage in bytes | `{"total": <size>, "used": <size>}` |
| /top | Top 5 processes and their CPU usage | `[{"pid": <PID>, "name": <name>, "usage": <usage>}, ...]` |
| /top?n=\<n\> | Top `n` processes and their CPU usage | `[{"pid": <PID>, "name": <name>, "usage": <usage>}, ...]` |
