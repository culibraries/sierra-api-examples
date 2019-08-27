import requests,json
import base64,sys,os
import pyjq as jq

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

def search_api(search_text,index='isbn',fields="varFields,id,author,updatedDate,createdDate,available,lang,materialType,bibLevel,catalogDate,normTitle,normAuthor,title,author,publishYear"):
    headers=set_request_header()
    req = requests.get("{0}/bibs/search?index={1}&text={2}&fields={3}".format(api_url,index,search_text,fields),headers=headers)
    return req.json()

if __name__ == "__main__":
    index=sys.argv[1]
    search_text=sys.argv[2]
    #data=search_api(search_text,index)
    try:
        fields=sys.argv[3]
    except:
        fields="varFields,id,author,updatedDate,createdDate,available,lang,materialType,bibLevel,catalogDate,normTitle,normAuthor,title,author,publishYear"
    data=search_api(search_text,index=index,fields=fields)
    for itm in data['entries']:
        #print(itm)
        itm['record_url']="https://libraries.colorado.edu/record=b{0}".format(itm['bib']['id'])
        try: 
            itm['isbn']=jq.all('.bib.varFields[]  | select(.marcTag == "020") | .subfields[] | select(.tag =="a") | .content ',itm)
        except:
            pass
        #print (filter(lambda x: x.get('tag') == 'a',filter(lambda x: x.get('marcTag') == '020',itm['bib']['varFields']).subfields).content)
        #data['entries']['bib']['record_url']="https://libraries.colorado.edu/record=b{0}".format(itm['bib']['id'])
    print(json.dumps(data,indent=4))
