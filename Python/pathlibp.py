import pandas as pd # type: ignore
from pathlib import Path


# file_path = './MeusProjetos/Python/mailing.csv'

# file_path = Path(__file__).parent / 'data' / 'mailing.csv'

# df = pd.read_csv(file_path.resolve())

# print(df)

print(Path().home() / '.ssh')