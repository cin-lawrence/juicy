from typing import TypeVar, Generic
from pydantic import BaseModel
from pydantic.generics import GenericModel


TypeX = TypeVar("TypeX")


class BaseClass(GenericModel, Generic[TypeX]):
    X: TypeX


class ChildClass(BaseClass[TypeX], Generic[TypeX]):
    pass


class Mock(BaseModel):
    foo: int
    bar: str


mock = Mock(foo=1, bar="a")


print(ChildClass[int](X=1))
print(ChildClass[Mock](X=mock))
