import pytest
import sys
import os
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))


def test_load_animal_data_from_csv():
    """
    Tests to download the animal data from CSV-file
    """
    csv_file_path = PROJECT_ROOT / "data" / "test_animals.csv"

    expected_data = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Vili", "Miki", "Lili"],
            "species": ["Dog", "Cat", "Dog"],
            "birth_date": ["2020-01-01", "2019-05-15", "2021-03-10"],
        }
    )
