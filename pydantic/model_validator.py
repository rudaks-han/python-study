from pydantic import BaseModel, root_validator, model_validator


class Order(BaseModel):
    item_count: int
    total_price: float

    # 전체 데이터에 대한 유효성 검사
    @model_validator(mode="before")
    def check_order(cls, values):
        item_count = values.get("item_count")
        total_price = values.get("total_price")
        if total_price < item_count * 10:  # 최소 단가가 10원 이상이어야 함
            raise ValueError("Total price is too low for the item count")
        return values


try:
    order = Order(item_count=5, total_price=40)
except ValueError as e:
    print(e)
