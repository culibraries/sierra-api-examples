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

def search_api(search_text,index='isbn'):
    headers=set_request_header()
    req = requests.get("{0}/bibs/search?index={1}&text={2}".format(api_url,index,search_text),headers=headers)
    return req.json()

if __name__ == "__main__":
    index=sys.argv[1]
    search_text=sys.argv[2]
    data=search_api(search_text,index)
    print(json.dumps(data,indent=4))
