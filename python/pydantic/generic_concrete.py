from typing import Generic, TypeVar, Type, Any, Tuple

from pydantic.generics import GenericModel


DataT = TypeVar("DataT")
Params = Tuple[Type[Any], ...]


class Response(GenericModel, Generic[DataT]):
    data: DataT

    @classmethod
    def __concrete_name__(cls: Type[Any], params: Params) -> str:
        return f"{params[0].__name__.title()}Response"


resp_int = Response[int](data=1)
resp_str = Response[str](data="a")

print(resp_int.__class__.__name__)
print(resp_str.__class__.__name__)
