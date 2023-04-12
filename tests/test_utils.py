import pandas as pd

import pandas_extensions

DF = pd.DataFrame(
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


def test_isid():
    assert DF.utils.isid("Student_ID") is True
    assert DF.utils.isid("First_Name") is False
