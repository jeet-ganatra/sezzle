import inspect
import random
import string
from typing import List, Dict

from src.Operations import Operations


class Util:

    @staticmethod
    def generate_unique_key():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    @staticmethod
    def renderHtml(response: [Operations]):
        table_row = ""
        for res in response:
            table_row +="<tr><td>"+res.a+" "+res.result+" "+res.b+" = "+res.operation+"</td></tr>"
        return "<table>"+table_row+"</table>"