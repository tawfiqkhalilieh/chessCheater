from typing import List
# import pandas as pd


class QueryFormatter:

    results = []
    columns = []

    def __init__(self, records: List[tuple], columns: list):
        self.results = records
        self.columns = columns

    def json(self) -> List[dict]:
        return_list = []
        for record in self.results:
            return_list.append(dict(zip(self.columns, record)))
        return return_list

    # def dataframe(self) -> pd.DataFrame:
    #     return pd.DataFrame(columns=self.columns, data=self.results)