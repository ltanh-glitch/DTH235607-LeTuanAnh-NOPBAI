import json

python_object = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1",
}

json_string = json.dumps(python_object, ensure_ascii=False)
print("Chuỗi JSON:", json_string)
