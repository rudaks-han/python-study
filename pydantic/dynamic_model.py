from pydantic import create_model

# 동적으로 새로운 모델 생성
DynamicModel = create_model("DynamicModel", foo=(str, ...), bar=(int, 42))

instance = DynamicModel(foo="Hello")
print(instance.model_dump())  # {'foo': 'Hello', 'bar': 42}
