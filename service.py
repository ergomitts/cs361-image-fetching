from googleapiclient.discovery import build

api_key = "AIzaSyCdA_yJKXtW7WNdJnQE9Hxu2rLEbRnkseQ"
cse_id = "114bca9babc1b4338"

def service(input):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(
        q=input,
        cx=cse_id,
        searchType="image",
        num=5
    ).execute()
    # This returns the raw JSON file
    return res

def get_links(input):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(
        q=input,
        cx=cse_id,
        searchType="image",
        num=5
    ).execute()
    # This returns the raw JSON file
    return [item["link"] for item in res.get("items", [])]