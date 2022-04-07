import pandas as pd

def present(filename):
    dataframe = pd.read_csv(filename)[:10]
    dataset = dataframe.to_html()
    return dataset