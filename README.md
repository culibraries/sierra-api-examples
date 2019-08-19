# Sierra API Examples
This repository provides Python 3 code examples for pulling data from CU Libraries Sierra API.

## Sierra API Setup

After receiving Sierra API Key and Secret. Set and ENVIRONMENTAL Variable.

        SIERRA_KEY_SECRET="<Sierra Key>:<Sierra Secret>"

## Python Setup
Script use Requests Library

        $ pip install requests


## Run Script

        $ python isbnLookup.py 067944453x
        
        {
            "count": 1,
            "total": 1,
            "start": 0,
            "entries": [
                {
                    "relevance": 2.4000000953674316,
                    "bib": {
                        "id": "2614489",
                        "updatedDate": "2014-11-23T13:39:12Z",
                        "createdDate": "1996-10-09T14:42:21Z",
                        "deleted": false,
                        "suppressed": false,
                        "lang": {
                            "code": "eng",
                            "name": "English"
                        },
                        "title": "Trout : an illustrated history",
                        "author": "Prosek, James, 1975-",
                        "materialType": {
                            "code": "m  ",
                            "value": "Books"
                        },
                        "bibLevel": {
                            "code": "d",
                            "value": "DLC"
                        },
                        "publishYear": 1996,
                        "catalogDate": "1997-05-09",
                        "country": {
                            "code": "nyu",
                            "name": "New York"
                        }
                    }
                }
            ]
        }
