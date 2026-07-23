from flask import Flask, request, Response
import requests
import re

app = Flask(__name__)

API_KEY = "AnuragSingh"

@app.route("/api")
def lookup():

    if request.args.get("apikey") != API_KEY:
        return Response("INVALID API KEY", mimetype="text/plain")

    number = request.args.get("number")

    if not number:
        return Response("NUMBER REQUIRED", mimetype="text/plain")

    try:

        url = f"https://nitin-apis-update-birthday-spacial.vercel.app/api?type=number&search={number}"

        r = requests.get(url, timeout=20)
        text = r.text

        name = re.search(r"Name:\s*(.+)", text)
        father = re.search(r"Father Name:\s*(.+)", text)
        mobile = re.search(r"Mobile:\s*(.+)", text)
        address = re.search(r"Address:\s*(.+)", text)

        if not all([name, father, mobile, address]):
            raise Exception()

        result = f"""🔥 PREMIUM NUMBER FINDER BY ANURAG SINGH 🔥
___________________________________________

NAME :- {name.group(1).strip()}
---------------------------------------------------------------------------
FATHER NAME :- {father.group(1).strip()}
---------------------------------------------------------------------------
MOBILE :- {mobile.group(1).strip()}
---------------------------------------------------------------------------
ADDRESS :- {address.group(1).strip()}
---------------------------------------------------------------------------
Owner @Developer_NovaG"""

        return Response(result, mimetype="text/plain")

    except:
        return Response("""API ERROR CONTACT OWNER
@Developer_NovaG""", mimetype="text/plain")


app = app
