from promptflow import tool

@tool
def zpracuj_uzavirani_kodu(data):
    kod_priciny = ["1", "2", "3", "4", "5", "6"]
    kod_technologie = [
        "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", 
        "13", "14", "15", "16", "17", "18", "19", "20", "21", "99"
    ]
    
    if isinstance(data, str) and "Příčina:" in data and "Technologická oblast:" in data:
        try:
            pricina = data.split("Příčina:")[1].split("\n")[0].strip()
            technologie = data.split("Technologická oblast:")[1].strip()
        except IndexError:
            raise ValueError("Neplatný formát")
    else:
        raise ValueError("Neplatný formát")

    return {
        "kod_priciny": pricina,
        "kod_oblasti": technologie
    }


