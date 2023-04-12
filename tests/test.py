import pandas as pd
from collections.abc import Collection, Iterable, Sequence

import pandas_extensions

df = pd.DataFrame(
    {
        "First_Name": [
            "Tom",
            "Nick",
            "Tom",
            "Jerry",
            "Samantha",
            "Samantha",
            "Samantha",
        ],
        "Last_Name": ["Bean", "Manning", "Bean", "Nurse", "Depp", "Depp", "Hardy"],
        "Student_ID": [1, 2, 3, 4, 5, 6, 7],
        "Score": [100, 90, 100, 65, 100, 100, 100],
    }
)

for a in df["First_Name"].utils.levelsof():
    print(a)

for a in df.utils.levelsof(["First_Name", "Last_Name"], named_tuples=False):
    print(a)
