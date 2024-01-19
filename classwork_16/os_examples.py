import os
import signal

while True:
    process_list = os.popen('tasklist').read()
    all_process_list = process_list.splitlines()
    for process in all_process_list:
        process_info = process.split()
        if process_info and process_info[0].lower() == "spotify.exe":
            print(process_info[1])
            os.kill(int(process_info[1]), signal.SIGTERM)

