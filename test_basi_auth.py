import requests
from requests.auth import HTTPBasicAuth
import json
import jsonpath


def test_o_authentications():
    # We need to use first token URL
    token_url = "https://xv24xrhpxa.execute-api.ap-south-1.amazonaws.com/v1/authToken"

    # Send values here in form of dictionary
    data = '{"username":"username","password":"password"}'

    # Post the data
    resp = requests.post(token_url, data)

    # Get  the token value
    token_value = jsonpath.jsonpath(resp.json(), 'access_token')

    # Want to access the token and create one dictionary.Whatever the token we get from above will pass here.
    # Along with the bearer so will write bearer then value.

    auth = {'Authorization': 'Bearer' + token_value[0]}

    #  Now on main URL
    url = "https://xv24xrhpxa.execute-api.ap-south-1.amazonaws.com/v1/authToken"

    #  Send request with token value
    response = requests.get(url, headers=auth)

    # Print response
    print(response.text)
