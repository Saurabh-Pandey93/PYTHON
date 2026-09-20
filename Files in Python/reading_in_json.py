import json 

with open("data.json", "r") as f:
    py_obj = json.loads(f)
    print(py_obj)