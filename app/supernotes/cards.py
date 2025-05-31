import requests


def getCards(key):
    url = "https://api.supernotes.app/v1/cards/get/select"

    payload = {
        "filter_group": {
            "type": "group",
            "op": "or",
            "filters": [
                {
                    "type": "tag",
                    "op": "contains",
                    "arg": "superpage"
                },
                {
                    "type": "tag",
                    "op": "contains",
                    "arg": "superpageme"
                }
            ]
        },
        "sort_type": 0,
        "sort_ascending": True,
    }
    headers = {
        "Api-Key": key,
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers).text
    return response