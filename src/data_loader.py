import pandas as pd


def load_animal_data(file_path):
    data = pd.read_csv(file_path)

    return data


if __name__ == "__main__":
    # Example usage
    file_path = "/home/vivaldev/farm_life/data/test_animals.csv"
    animal_data = load_animal_data(file_path)
    print(animal_data.head())
