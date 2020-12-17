import requests
import json
url = "https://teleduce.corefactors.in/send-email-json-otom/a224db72-cafb-4cce-93ab-3d7f950c92e2/1009/"

to_list=[{"email_id":"samiransarkar513@gmail.com","name":"samiran sarkar"}, {"email_id":"zaakir338@gmail.com"}]
message = {
"html_content":"<html><head><title></title></head><body><p><a href='http://www.corefactors.in'>Testing Link</a></p></body></html>",
"subject":"testing doctor-plus",
"from_mail":"bstejas@doctor-plus.in",
"from_name":"doctor Plus",
"reply_to":"bstejas@doctor-plus.in",
"to_recipients":to_list
}
payload = {"message" :message}
single_content = {"mail_datas":payload}
# print(single_content)
reqdata = requests.post(url, data=json.dumps(single_content), headers={'Content-Type': 'application/json'})
print (reqdata.content)
print (reqdata.url)
