import json

json_string = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

data_object = json.loads(json_string)
print(data_object)
print("Mã=", data_object["ma"])
print("Tên=", data_object["ten"])
print("Tuổi=", data_object["age"])
