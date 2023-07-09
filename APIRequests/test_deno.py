import requests
import pytest

def test_post_validation():
    header={
        'Content-Type':'application/json'
    }
    url='https://reqres.in/'
    response=requests.post(url=str(url + 'api/users/2'),headers=header,timeout=100)
    assert 201 == response.status_code
    print(response.text)
    print(response.json())


