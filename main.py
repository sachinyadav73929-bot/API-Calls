import requests

def get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            users = response.json()

            print("\n===== USER INFORMATION =====")

            for user in users:
                print("\n-------------------------")
                print("ID:", user["id"])
                print("Name:", user["name"])
                print("Username:", user["username"])
                print("Email:", user["email"])
                print("City:", user["address"]["city"])

        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)


get_users()