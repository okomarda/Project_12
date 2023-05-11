import json
from datetime import datetime

file_json = "../operations.json"

def load_data(file_json) :
    '''Передача данных файла json в список'''
    with open (file_json, 'r', encoding='utf-8') as file :
        data = json.load (file)
        list_date = []
        for d in data:
            if "date" in d and "from" in d and d["state"]== "EXECUTED":
                list_date.append(d)
                list_date.sort(key = lambda x: x["date"], reverse = True)
                five_list_date = list_date[0:5]

                final_list = []
                for five in five_list_date:
                    date = "".join(list(five["date"])[8:10]) + "." + "".join(list(five["date"])[5:7]) + "." + "".join(list(five["date"])[0:4])
                    description = five["description"]
                    from_ = "".join(list(five["from"]))
                    if "Счет" in from_:
                        from_ = "".join (list (five["from"]))[:-20] + "**" + "".join (list (five["from"]))[-4:]
                    else:
                        from_ = "".join (list (five["from"]))[:-17] + "".join (list (five["from"]))[-17:-12] + " " + "".join (list (five["from"]))[-12:-10] + "** **** " + "".join (list (five["from"]))[-4:]
                    to_ = "".join(list(five["to"]))[:-20] + "**" + "".join(list(five["to"]))[-4:]
                    amount = five["operationAmount"]["amount"]
                    currency = five["operationAmount"]["currency"]["name"]
                    final_list.append(f"{date} {description}\n{from_}->{to_}\n{amount} {currency}\n\n")
        return ("".join(final_list))




print(load_data(file_json))






