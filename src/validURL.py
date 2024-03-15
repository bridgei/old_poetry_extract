
import requests
import validators.url


def is_ValidUrl(argURL):
    msg = ""
    result = False
    if validators.url(argURL):
        conn = requests.get(argURL, timeout=5)
        # conn.time
        msg = msg + str(conn.status_code)
        result = conn.status_code == 200
    else:
        msg = "Invalid URL"
    return (result, msg)