from flask import json


class Operations:
    def __init__(self, a, b, operation, result):
        self.a = a
        self.b = b
        self.result = result
        self.operation = operation

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
