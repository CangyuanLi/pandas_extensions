from collections.abc import Iterable
from typing import Any, Optional, Union

import pandas as pd

PandasObj = Union[pd.DataFrame, pd.Series]
Keys = Union[list[str], tuple[str], set[str], str]


@pd.api.extensions.register_dataframe_accessor("utils")
@pd.api.extensions.register_series_accessor("utils")
class CustomUtilsAccessor:
    def __init__(self, obj: PandasObj) -> None:
        self._obj = obj

    def _get_names(self) -> list[str]:
        if isinstance(self._obj, pd.DataFrame):
            return list(self._obj.columns)

        return [self._obj.name]

    def _set_keys(self, keys: Optional[Keys]) -> list[str]:
        if keys is None:
            return self._get_names()

        if isinstance(keys, str):
            keys = [keys]
        else:
            keys = list(keys)

        return keys

    def isid(self, keys: Optional[Keys] = None) -> bool:
        """Check if the specified columns uniquely identify the dataset.

        Args:
            keys (Optional[Keys], optional): columns. Defaults to None.

        Returns:
            bool: ID or not
        """
        keys = self._set_keys(keys)

        return self._obj.set_index(keys).index.is_unique

    def levelsof(
        self,
        keys: Optional[Keys] = None,
        named_tuples: bool = True,
    ) -> Iterable[tuple[Any, ...]]:
        """This is a generalization of Stata's levelsof function, which returns the
        unique instances of a variable. In this case, we are able to return unique
        instances of multiple variables.

        Args:
            keys (Optional[Keys], optional): Columns. Defaults to None.
            named_tuples (bool, optional): Named or Regular. Defaults to True.

        Returns:
            Iterable[tuple[Any, ...]]: A list of tuples
        """
        keys = self._set_keys(keys)

        # If name is None, Pandas will fall back to regular tuples
        if not named_tuples:
            name = None
        else:
            name = "Pandas"

        df = pd.DataFrame(self._obj)
        levels = (
            df.drop_duplicates(subset=keys)
            .dropna()
            .loc[:, keys]
            .itertuples(index=False, name=name)
        )

        return levels

    def duplicates(self, keys: Optional[Keys] = None) -> PandasObj:
        keys = self._set_keys(keys)

        obj = self._obj.loc[self._obj.duplicated(subset=keys, keep=False)].sort_values(
            keys
        )

        return obj
