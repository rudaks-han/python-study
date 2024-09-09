from pydantic import BaseModel, validator, field_validator


class Product(BaseModel):
    name: str
    price: float

    # 가격이 0보다 커야 한다는 조건 추가
    @field_validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v


try:
    product = Product(name="Laptop", price=-1000)
except ValueError as e:
    print(e)
