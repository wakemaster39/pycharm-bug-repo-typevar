from __future__ import annotations  # type: ignore

from itertools import groupby
from typing import Callable, List, TypeVar, cast
from test_package.sub1.entity_node import EntityNode
from test_package.sub1.types import IPNetwork

T = TypeVar("T")


def default_network_tree_callable(x: T) -> IPNetwork:
    return cast(IPNetwork, x)


def get_network_tree_branches(
    objs: List[T], key_func: Callable[[T], IPNetwork] = default_network_tree_callable
) -> List[EntityNode[T]]:

    def plen_key_func(x: T) -> int:
        return key_func(x).prefixlen

    grouped_networks = sorted(
        [(k, [make_node(x) for x in v]) for k, v in groupby(sorted(objs, key=plen_key_func), key=plen_key_func)],
        key=lambda x: x[0],
        reverse=True,
    )

