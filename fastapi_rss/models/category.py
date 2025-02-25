from typing import Optional

from pydantic import BaseModel


class CategoryAttrs(BaseModel):
    """
    A string that identifies a categorization taxonomy.
    It's a forward-slash separated string which identifies
    a hierarchic location in the indicated taxonomy.

    Processors may establish conventions for the interpretation of categories
    """

    domain: Optional[str]


class Category(BaseModel):
    """
    An optional sub-element of a channel or an item
    """

    content: Optional[str]
    attrs: Optional[CategoryAttrs]
