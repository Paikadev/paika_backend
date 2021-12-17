from fastapi import APIRouter
import requests
from requests.auth import HTTPBasicAuth

dolby = APIRouter()


@dolby.get("/dolby/token")
def get_token():
    key = "cCtj_wIfvRnmfeUnDpskxQ=="
    secret = "s-Lo5yY_UXWc4VPVSJz0rooEwI4_AcG7OqDwP3zK7Do="
    response = requests.post("https://api.voxeet.com/v1/auth/token",
    auth = HTTPBasicAuth(key, secret),
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data= { "grant_type": "client_credentials" })
    response.raise_for_status()
    return response.json()["access_token"]


@dolby.post("/dolby/rtmp/{id}")
def stream_rtmp(id: str):
    key = "cCtj_wIfvRnmfeUnDpskxQ=="
    secret = "s-Lo5yY_UXWc4VPVSJz0rooEwI4_AcG7OqDwP3zK7Do="
    response = requests.post("https://api.voxeet.com/v1/auth/token",
    auth = HTTPBasicAuth(key, secret),
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data= { "grant_type": "client_credentials" })
    response.raise_for_status()
    token_rtmp = response.json()["access_token"]

    stream_key = stream_start_mux()

    url = "https://api.voxeet.com/v2/conferences/mix/{id}/rtmp/start"
    payload = {"uri": "rtmp://a.rtmp.youtube.com/live2/y30q-v0qy-117c-681p-80th"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer "+ token_rtmp
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return stream_key


def stream_views_mux(id: str):
    keyMux = "b1472771-6c0a-4a86-b710-89c424d1d21c"
    secretMux = "2B/ud8cT8e/YG2+8g8GLkaRwRWCP+FII8z1kj5qq0pxfxa8rPU/cGsnJvbRwnzEQnP9fea+CdWf"
    response = requests.post("https://api.mux.com/video/v1/live-streams/"+id+"/playback-ids",
    auth = HTTPBasicAuth(keyMux, secretMux),
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data= {
        "policy": "public" })
    print(response.json())
    return response.json()

def stream_start_mux():
    keyMux = "b1472771-6c0a-4a86-b710-89c424d1d21c"
    secretMux = "2B/ud8cT8e/YG2+8g8GLkaRwRWCP+FII8z1kj5qq0pxfxa8rPU/cGsnJvbRwnzEQnP9fea+CdWf"
    response = requests.post("https://api.mux.com/video/v1/live-streams",
    auth = HTTPBasicAuth(keyMux, secretMux),
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data= { "grant_type": "client_credentials"})
    response.raise_for_status()
    id_play = response.json()["data"]["id"]
    stream_views_mux(id_play)
    print(response.json()["data"])
    return response.json()["data"]["stream_key"]