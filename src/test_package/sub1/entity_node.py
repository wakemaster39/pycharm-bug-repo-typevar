from __future__ import annotations

from typing import Any, Generic, List, Optional, TypeVar

from anytree import NodeMixin

T = TypeVar("T")


class EntityNode(Generic[T], NodeMixin):
    obj: T

    def __init__(self, obj: T, parent: Optional[EntityNode[T]] = None, children: Optional[List[EntityNode[T]]] = None):
        self.obj = obj
        self.parent = parent
        if children:
            self.children = children

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EntityNode):
            return False
        return self.obj == other.obj and self.children == other.children
