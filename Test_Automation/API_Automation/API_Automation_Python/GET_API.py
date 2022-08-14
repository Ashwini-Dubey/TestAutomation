import requests
base_url = "https://reqres.in/"
headers = { 'Content-Type' : 'application/json'}
def test_list_users():
        print("-------------Beginning the Test for List Users API-------------")
        relative_url_list_users = "api/users?page=2"
        url_list_users = str(base_url)+str(relative_url_list_users)
        list_users_response = requests.request("GET", url=url_list_users, headers=headers)
        list_users_response = list_users_response.json()
        print(list_users_response)
        print("-------------Ending the Test for List Users API-------------")
def test_single_user():
        print("-------------Beginning the Test for Single User API-------------")
        relative_url_single_user = "api/users/2"
        url_single_users = str(base_url)+str(relative_url_single_user)
        single_user_response = requests.request("GET", url= url_single_users,headers=headers)
        single_user_response = single_user_response.json()
        print(single_user_response)
        print("-------------Ending the Test for Single User API-------------")
def  test_single_user_error():
        print("-------------Beginning the Test for Single User Error API-------------")
        relative_url_single_user_error = "api/users/23"
        url_single_users_error = str(base_url)+str(relative_url_single_user_error)
        single_user_error_response = requests.request("GET", url= url_single_users_error,headers=headers)
        single_user_error_response = single_user_error_response.json()
        print(single_user_error_response)
        print("-------------Ending the Test for Single User Error API-------------")
def  test_list_resource():
        print("-------------Beginning the Test for List Resource API-------------")
        relative_url_list_resource = "api/users/unknown"
        url_list_resource = str(base_url)+str(relative_url_list_resource)
        list_resource_response = requests.request("GET", url= url_list_resource,headers=headers)
        list_resource_response = list_resource_response.json()
        print(list_resource_response)
        print("-------------Ending the Test for List Resource API-------------")
def  test_single_resource():
        print("-------------Beginning the Test for Single Resource API-------------")
        relative_url_single_resource = "api/users/unknown/2"
        url_single_resource = str(base_url)+str(relative_url_single_resource)
        single_resource_response = requests.request("GET", url= url_single_resource,headers=headers)
        single_resource_response = single_resource_response.json()
        print(single_resource_response)
        print("-------------Ending the Test for Single Resource API-------------")
def  test_single_resource_error():
        print("-------------Beginning the Test for Single Resource Error API-------------")
        relative_url_single_resource_error = "api/users/unknown/23"
        url_single_resource_error = str(base_url)+str(relative_url_single_resource_error)
        single_resource_response_error = requests.request("GET", url= url_single_resource_error,headers=headers)
        single_resource_response_error = single_resource_response_error.json()
        print(single_resource_response_error)
        print("-------------Ending the Test for Single Resource API-------------")
def test_delay_response():
        print("-------------Beginning the Test for Delayed Response API-------------")
        relative_url_delay_response = "api/users?delay=3"
        url_delay_response = str(base_url)+str(relative_url_delay_response)
        response_delay_response = requests.request("GET", url= url_delay_response,headers=headers)
        response_delay_response = response_delay_response.json()
        print(response_delay_response)
        print("-------------Ending the Test for Delayed Response API-------------")

print("Running the tests for the GET API")
test_list_users()
test_single_user()
test_single_user_error()
test_list_resource()
test_single_resource()
test_single_resource_error()
test_delay_response()