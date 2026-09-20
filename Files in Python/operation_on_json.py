#json.loads()--it converts json string to python object
#json.dumps()-- it converts python object to json string
import json

json_str = '{"name": "Saurabh", "isTeacher": null}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)