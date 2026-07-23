from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

API_KEY = "AnuragSingh"

# Original API URL
ORIGINAL_API = "https://nitin-apis-update-birthday-spacial.vercel.app/api?type=number&search={number}"

@app.route("/api", methods=["GET"])
def lookup():

    key = request.args.get("apikey")
    number = request.args.get("number")

    if key != API_KEY:
        return "INVALID API KEY"

    if not number:
        return "NUMBER REQUIRED"

    try:
        url = ORIGINAL_API.format(number)
        r = requests.get(url, timeout=20)
        text = r.text

        # Agar expected response nahi mila
        if " Name:" not in text or " Father Name:" not in text or " Address:" not in text:
            return """API ERROR CONTACT OWNER
@developer_NovaG"""

        name = re.search(r" Name:\s*(.*)", text)
        father = re.search(r" Father Name:\s*(.*)", text)
        mobile = re.search(r" Mobile:\s*(.*)", text)
        address = re.search(r" Address:\s*(.*)", text)

        name = name.group(1).strip() if name else "N/A"
        father = father.group(1).strip() if father else "N/A"
        mobile = mobile.group(1).strip() if mobile else number
        address = address.group(1).strip() if address else "N/A"

        result = f"""🔥  PREMIUM NUMBER FINDER BY ANURAG SINGH 🔥
___________________________________________

NAME :- {name}
---------------------------------------------------------------------------
FATHER NAME :- {father}
---------------------------------------------------------------------------
MOBILE :- {mobile}
---------------------------------------------------------------------------
ADDRESS :- {address}
---------------------------------------------------------------------------
Owner @Developer_NovaG"""

        return result, 200, {"Content-Type": "text/plain; charset=utf-8"}

    except:
        return """API ERROR CONTACT OWNER
@developer_NovaG"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
