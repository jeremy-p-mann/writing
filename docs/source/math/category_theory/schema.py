import pandera as pa
from pandera.typing import Series


class FooSchema(pa.SchemaModel):
    """
    year: element of the set ${x integer | x > 2000}$
    month: element of the set ${x integer | 1 <= x <= 12}$
    day: element of the set ${x integer | 0 <= x <= 365}$
    group: element of the set ${"A", "B"}$
    """
    year: Series[int] = pa.Field(gt=2000)
    month: Series[int] = pa.Field(ge=1, le=12)
    day: Series[int] = pa.Field(ge=0, le=365)
    group: Series[str] = pa.Field(isin=["A", "B"])
