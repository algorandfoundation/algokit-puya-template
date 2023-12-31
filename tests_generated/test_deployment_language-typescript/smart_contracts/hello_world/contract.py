from puyapy import ARC4Contract, Bytes
from puyapy.arc4 import String, abimethod


class HelloWorld(ARC4Contract):
    @abimethod()
    def hello(self, name: String) -> String:
        return String.encode(Bytes(b"Hello ") + name.decode())
