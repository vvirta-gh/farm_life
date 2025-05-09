import pytest
import sys
import os
import pandas as pd
from pathlib import Path
from data_loader import load_animal_data

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

    # Test that the function can load the data
    actual_data = load_animal_data(csv_file_path)

    # Verify that the data matches the expected format and content
    pd.testing.assert_frame_equal(actual_data, expected_data)

    # Test that the function raises FileNotFoundError with non-existent file
    with pytest.raises(FileNotFoundError):
        load_animal_data("non_existent_file.csv")
