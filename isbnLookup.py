import requests,json
import base64,sys,os

api_url="https://libraries.colorado.edu/iii/sierra-api/v5"


def decode_response(req):
    return json.loads(req.content.decode(encoding='UTF-8'))


def set_request_header():
    api_key_secret=os.getenv('SIERRA_KEY_SECRET',None)
    encode= base64.b64encode(str.encode(api_key_secret))
    headers={"Content-Type":"application/json","Authorization": "Basic {0}".format(encode.decode("utf-8"))}
    req=requests.post("{0}/token".format(api_url),data=json.dumps({"grant_type":"client_credentials"}),headers=headers)
    access=decode_response(req)
    return {"Content-Type":"application/json","Authorization": "Bearer {0}".format(access['access_token'])}

def search_isbn(isbn_text):
    headers=set_request_header()
    req = requests.get("{0}/bibs/search?index=isbn&text={1}".format(api_url,isbn_text),headers=headers)
    print(json.dumps(decode_response(req),indent=4))

if __name__ == "__main__":
    isbn_text=sys.argv[1]
    search_isbn(isbn_text)
