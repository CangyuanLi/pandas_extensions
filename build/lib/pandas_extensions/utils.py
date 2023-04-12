from typing import Optional, Union

import pandas as pd


Keys = list[str] | tuple[str] | set[str] | str


@pd.api.extensions.register_dataframe_accessor("utils")
@pd.api.extensions.register_series_accessor("utils")
class CustomUtilsAccessor:
    def __init__(self, obj: pd.DataFrame | pd.Series) -> None:
        self._obj = obj

    def _get_names(self):
        if isinstance(self._obj, pd.DataFrame):
            return list(self._obj.columns)
        elif isinstance(self._obj, pd.Series):
            return [self._obj.name]

    def _set_keys(self, keys: Optional[Keys]):
        if keys is None:
            keys = self._get_names()

        if isinstance(keys, str):
            keys = [keys]

        return keys

    def isid(self, keys: Optional[Keys] = None) -> bool:
        keys = self._set_keys(keys)

        return self._obj.set_index(keys).index.is_unique

    def levelsof(
        self,
        keys: Optional[Keys] = None,
        named_tuples: bool = True,
    ) -> list[tuple]:
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
