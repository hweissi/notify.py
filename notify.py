#!/bin/python3

import requests
import subprocess
import sys
TOPIC = "[REDACTED]"
URL = f"https://ntfy.sh/{TOPIC}"
DEFAULT_RET_MAP = {0: "Command finished successfully"}
DEFAULT_RET = "Command failed"

def wrapCommand(cmd, ret_map = {}, default_ret = "Unknown return value"):


    res = subprocess.run(cmd, shell=True)
    data = default_ret
    print(res.returncode)
    if res.returncode in ret_map:
        data = ret_map[res.returncode]
    requests.post(URL,
        data=data.encode(encoding='utf-8'))
    return res.returncode


if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("No command provided")
        sys.exit(-1)
    ret = wrapCommand(" ".join(sys.argv[1:]), DEFAULT_RET_MAP, DEFAULT_RET)
    sys.exit(ret)
