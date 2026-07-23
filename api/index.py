try: 
    url = f"https://nitin-apis-update-birthday-spacial.vercel.app/api?type=number&search={number}"

    r = requests.get(url, timeout=20)
    text = r.text

    # Agar Name nahi mila to Error
    if "Name:" not in text:
        return Response(
            "API ERROR CONTACT OWNER\n@Developer_NovaG",
            mimetype="text/plain"
        )

    # Upar ka heading replace karo
    text = text.replace(
        "🔍 NUMBER LOOKUP RESULT",
        "🔥 PREMIUM NUMBER FINDER BY ANURAG SINGH 🔥"
    )

    # Agar bina space wala ho
    text = text.replace(
        "🔍NUMBER LOOKUP RESULT",
        "🔥 PREMIUM NUMBER FINDER BY ANURAG SINGH 🔥"
    )

    # Original Owner replace karo
    text = re.sub(
        r"Owner:.*",
        "Owner @Developer_NovaG",
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    return Response(text, mimetype="text/plain; charset=utf-8")

except:
    return Response(
        "API ERROR CONTACT OWNER\n@Developer_NovaG",
        mimetype="text/plain"
    )
