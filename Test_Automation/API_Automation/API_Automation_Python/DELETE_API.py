import requests
base_url = "https://reqres.in/"
headers = { 'Content-Type' : 'application/json'}
def test_delete_user():
        print("-------------Beginning the Test for Delete User API-------------")
        relative_url_delete_user = "api/users/2"
        url_delete_user = str(base_url)+str(relative_url_delete_user)
        delete_user_response = requests.request("GET", url=url_delete_user, headers=headers)
        delete_user_response_status = delete_user_response.status_code
        delete_user_response = delete_user_response.json()
        print(delete_user_response_status)
        print(delete_user_response)
        assert (delete_user_response_status == 200)
        print("-------------Ending the Test for Delete User API-------------")

test_delete_user()