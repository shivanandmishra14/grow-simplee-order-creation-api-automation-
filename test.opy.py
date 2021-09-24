import jsonpath
import requests
import json
import sys
import parse
import json
from test_basi_auth import test_o_authentications
from jsonpath_ng import jsonpath, parse
import api_helper
from api_helper import api_response
import pytest

put_req = api_helper.order_api
token = test_o_authentications()


def order_creation_api():
    post_order_values = put_req['url']
    post_body = post_order_values['POST']
    post_hit = api_helper.api_response(post_order_values, 'POST', post_body)
    assert post_hit.status_code == 201
    assert post_hit.headers["status"] == "success"
    # return  order_creation_api()


order_creation_api()
