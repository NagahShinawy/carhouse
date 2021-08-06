"""
created by Nagaj at 02/08/2021
"""
import socket
from .base import *

DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": "",
}
INTERNAL_IPS = [
    "127.0.0.1",
    socket.gethostbyname(socket.gethostname())[:-1] + "1",  # machine ip
]
