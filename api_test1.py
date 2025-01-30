import requests
import csv

# Basic API Request (GET)
# url = "https://catfact.ninja/fact"
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")

# ------------------------------------------------
# Testing with Deskera ERP #
############################

# auth_url = "https://bifrost.deskera.com/v1/iam/auth/sign-in/web/sign-in"
#
# headers = {"Content-Type" : "application/json"}
#
# payload = {
#     "password": "test1234",
#     "userName": "kivigab691@fitzola.com"
# }
#
# response = requests.post(auth_url, json=payload, headers=headers)
#
# if response.status_code == 200:
#     access_token = response.json().get("accessToken")
#     print("Access Token: ", access_token)
# else:
#     print(f"Failed to authenticate: {response.text}")


# --------------------------------------------------------------------
# ACCESSING EXAMPLE DATA #
##########################
data_url = "https://bifrost.deskera.com/v1/contacts?includeOpeningAmounts=&includeOweAmounts=&limit=10&page=&query=&search=&sort=createdAt&sortDir=desc"
# send_url = "https://bifrost.deskera.com/v1/contacts"
access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYW1Vc2VySWQiOjQyMzI0OSwid2Vic2l0ZSI6IlVuaXZlcnNlIiwiaXNPcmdTZXQiOnRydWUsInVzZXJfbmFtZSI6IjQxNDcwNTo3MDE1MTEiLCJpc3MiOiJEZXNrZXJhIiwiZ2l2ZW5fbmFtZSI6IlRlc3QiLCJ1c2VySWQiOjQxNDcwNSwiY2xpZW50X2lkIjoid2ViLWNsaWVudCIsInRheFJlc2lkZW5jeSI6IklOIiwiY29tcGxpYW5jZUVuYWJsZWQiOmZhbHNlLCJmaXJlYmFzZVRva2VuIjoiZXlKaGJHY2lPaUpTVXpJMU5pSjkuZXlKaGRXUWlPaUpvZEhSd2N6b3ZMMmxrWlc1MGFYUjVkRzl2Ykd0cGRDNW5iMjluYkdWaGNHbHpMbU52YlM5bmIyOW5iR1V1YVdSbGJuUnBkSGt1YVdSbGJuUnBkSGwwYjI5c2EybDBMbll4TGtsa1pXNTBhWFI1Vkc5dmJHdHBkQ0lzSW1WNGNDSTZNVGN6T0RBME1USXlNQ3dpYVdGMElqb3hOek00TURNM05qSXdMQ0pwYzNNaU9pSm1hWEpsWW1GelpTMWhaRzFwYm5Oa2F5MWhNbWx1YzBCa1pYTnJiVzlpYVd4bFlYQndMWEJ5YjJRdWFXRnRMbWR6WlhKMmFXTmxZV05qYjNWdWRDNWpiMjBpTENKemRXSWlPaUptYVhKbFltRnpaUzFoWkcxcGJuTmtheTFoTW1sdWMwQmtaWE5yYlc5aWFXeGxZWEJ3TFhCeWIyUXVhV0Z0TG1kelpYSjJhV05sWVdOamIzVnVkQzVqYjIwaUxDSjFhV1FpT2lJMU1XTmlObVEwTmkxbVpUVXdMVFF4T0dVdE9XVXlZUzB3WlRReE1HSmxNV1ZoTldFaWZRLng1cG43aExGZ3ZCZ3F0YlBCTG1oLTN6ekltbmFNeWN6RnhESzhHQWdHWXg1LTBjUDAwMm1Pd3hzaHZIYXRUSGh5cVpLZ1ZabFE1N3NMc3B1cERFbWV3cFYwTHQtamwwY1k0RnRXaXJ1TlM5Tno5YnpkQjh5TDRWTjhJY0V5Sl9oVUlPN3MyN3A3VENTeS0zdEY2WkdJUGJzNHpZanRjUTFCa19haXZWVGthd3g2MTBCVHJJNWdZemxzcXIzSG5HTkZwNjh0dlFQTmMzc3Q0UnAyXzRwOVdFa3pQYnhwY3dablBOdkxvWGdwR3JUVFRmMXpHc3BKNlVRRDdaVl9yc3BHVDZXNnJ0dWJWZUZiUGJrWWtYemF4cEtwN1dxNW1Idzc0Yk9xeHdPMEVTWlZYdkd2cjRFRmNlZzl6YTNjNm4zSzJTZ3ZpMWZ6TEtlc3dFWmNNMzY4USIsImNvdW50cnlDb2RlIjpudWxsLCJzY29wZSI6W10sInRlbmFudElkIjo3MDE1MTEsIm5hbWUiOiJUZXN0IEFjY291bnQiLCJwaG9uZV9udW1iZXIiOiIiLCJjdXJyZW5jeSI6Ik1NSyIsImJvb2tfa2VlcGVyIjpmYWxzZSwiZXhwIjoxNzYzOTU3NjIwLCJpYXQiOjE3MzgwMzc2MjAsImp0aSI6IjAwMjM1OWYwLTQyNzktNGY2MC1iODE2LTJmNWVjYzA4MGE3NSIsImVtYWlsIjoia2l2aWdhYjY5MUBmaXR6b2xhLmNvbSJ9.RZ8AJ6fV9dC5PVe7Eg2sGAp6YLjqkjdsbw6n1iFQ7MnGSa8ZmhJ80MVWlLdxah2BLimsbv8rm11EKAaVKOlSlVoJn2N8GKDY8BVm2iyLtFBVCNXv2odo4XojdcMFs8ZZW2lxpNduE1baAXxr7KYhwePe8jtnZcY6kCj0hD4mohZKgNCG6FagHxK2VUdipLtStPhi7W9XleBxpXn3ae0elxRkGK4y5Y6CV4z72lFqP0o9jcKhHgXdvoOmPUQGwObhZ1cSvJ8nBDHWaqyJYBJNDbaWDc2HCig4NrKdn0E-CUXtZjamT7tQgJQJFXepjlcwkBvTN5fotIhQnMElw51z7Q"
headers = {
    "x-access-token": access_token,
    "Content-Type": "application/json"
}
response = requests.get(data_url, headers=headers)

message = {
  "attentionTo": "Peter Parker",
  "billingAddress": [
    {
      "address1": "Yangon",
      "address2": "Downtown",
      "city": "Yangon",
      "country": "Myanmar",
      "postalCode": "11211",
      "preferred": True,
      "state": "Yangon"
    }
  ],
  "businessUnit": "",
  "currencyCode": "MMK",
  "documentSequenceCode": "C-2222222",
  "emailId": "pyaephyo@anonymous.net",
  "name": "Pyae Phyo Hein",
  "payableAccountCode": "ACC40001",
  "paymentTermCode": "Net 0",
  "peppolId": "u000:11::11293",
  "receivableAccountCode": "ACC30001",
  "sequenceFormat": "1",
  "shippingAddress": [
    {
      "address1": "Yangon",
      "address2": "Downtown",
      "city": "Yangon",
      "country": "Myanmar",
      "postalCode": "11211",
      "preferred": True,
      "state": "Yangon"
    }
  ],
  "singaporeGovt": False,
  "taxExempted": False,
  "taxExemptionNo": "",
  "taxExemptionReason": "",
  "taxNumber": "",
  "uen": ""
}

# response2 = requests.post(send_url, json=message, headers=headers)

if response.status_code == 200:
    data = response.json()
    # print(data)
    contacts = data['content']
    contact_list = [] # to store structured data
    # print(contacts[0])
    for contact in contacts:
      print(contact["status"])
      contact_list.append([
        contact["documentSequenceCode"],
        contact["name"],
        contact["status"],
        contact["theyOweYou"],
        contact["youOweThem"]
      ])

    with open("contacts.csv", "w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Sequence Code", "Customer Name", "Status", "They Owe You", "You Owe Them"])
      writer.writerows(contact_list)

    print(f"{contact_list}")
    print(f"✅ Data saved to users.csv successfully!")
else:
    print(f"❌ Failed to fetch data: {response.text}")


# if response2.status_code == 200:
#     print("Added new contact")
# else:
#     print(f"Failed to fetch data: {response2.text}")

