from collections.abc import Container
import string

import pandas as pd

@pd.api.extensions.register_series_accessor("str_exts")
class CustomStringExtensionsAccessor:
    
    def __init__(self, series: pd.Series):
        self._validate(series)
        self._series = series

    @staticmethod
    def _validate(series: pd.Series):
        if not pd.api.types.is_string_dtype(series):
            raise TypeError(f"Column {series.name} must be of string type.")

    def remove_puncs(self, exclude: Container[str]=None) -> pd.Series:
        if exclude is None:
            exclude = []

        puncs = "".join(punc for punc in string.punctuation if punc not in exclude)

        return self._series.replace(f"[{puncs}]", "", regex=True)

    def remove_nums(self) -> pd.Series:
        return self._series.str.replace("\d+", "", regex=True)

    def sanitize(self) -> pd.Series:
        col = self._series
        col = (
            col.str.encode("ascii", "ignore").str.decode("ascii")
               .str.upper()
               .str.strip()
               .str_exts.remove_puncs()
               .str.replace(r"\s+", " ", regex=True)
        )

        return col
