from auth import auth 
from pprint import pprint
import base64

user = auth().users()
messages = user.messages().list(userId="me",maxResults=10).execute()

for message in messages.get('messages'):
    response = user.messages().get(userId="me",id=f"{message.get('id')}").execute()
    # print(type(response.get("body")))
    # text = response.get("body").get("data")
    # pprint(base64.b64decode(text))


print(response)