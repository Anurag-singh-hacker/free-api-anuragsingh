try:
    url = f"https://nitin-apis-update-birthday-spacial.vercel.app/api?type=number&search={number}"

    r = requests.get(url, timeout=20)
    text = r.text

    def get_value(start, end_list):
        try:
            s = text.index(start) + len(start)
            e = len(text)

            for end in end_list:
                pos = text.find(end, s)
                if pos != -1 and pos < e:
                    e = pos

            return text[s:e].strip()
        except:
            return None

    name = get_value("Name:", ["Father Name:"])
    father = get_value("Father Name:", ["Mobile:"])
    mobile = get_value("Mobile:", ["Address:"])
    address = get_value("Address:", ["Circle:", "Owner:"])

    # Agar Name hi nahi mila to Error
    if not name:
        return Response(
            "API ERROR CONTACT OWNER\n@Developer_NovaG",
            mimetype="text/plain"
        )

    result = f"""🔥 PREMIUM NUMBER FINDER BY ANURAG SINGH 🔥
___________________________________________

NAME :- {name}
---------------------------------------------------------------------------
FATHER NAME :- {father if father else "N/A"}
---------------------------------------------------------------------------
MOBILE :- {mobile if mobile else number}
---------------------------------------------------------------------------
ADDRESS :- {address if address else "N/A"}
---------------------------------------------------------------------------
Owner @Developer_NovaG"""

    return Response(result, mimetype="text/plain; charset=utf-8")

except:
    return Response(
        "API ERROR CONTACT OWNER\n@Developer_NovaG",
        mimetype="text/plain"
    )
