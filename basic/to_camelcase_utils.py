import json

from pydantic.alias_generators import to_camel

def to_camelcase(data: dict) -> dict:
    return to_camel(json.dumps(data))

json_data = {
    "user_id": "gdhong",
}

result = to_camelcase(json_data)
print(result)


