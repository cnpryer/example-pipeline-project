from typing import Any, Dict, List, TypedDict, Union


class FilterData(TypedDict):
    # target data name or group identifier
    name: str
    # key-value pair of field types and target values
    values: Dict[
        str,
        Union[int, str, float, Any],
    ]


class FilterRule(TypedDict):
    # target data definition to filter
    data: FilterData
    # "include" vs "exclude" filter type
    type: str
    # filter operation
    operator: str


FilterConfig = List[FilterRule]
