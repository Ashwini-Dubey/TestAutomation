import json
import requests
base_url = "https://reqres.in/"
headers = { 'Content-Type' : 'application/json'}
def test_update_user():
        print("-------------Beginning the Test for Update User API-------------")
        relative_url_update_user = "api/users/2"
        url_update_user = str(base_url)+str(relative_url_update_user)
        payload = json.dumps({"name":"morpheus","job":"zion resident"})
        update_user_response = requests.request("GET", url=url_update_user, headers=headers , data=payload)
        update_user_response = update_user_response.json()
        print(update_user_response)
        print("-------------Ending the Test for Update User API-------------")

test_update_user()
    