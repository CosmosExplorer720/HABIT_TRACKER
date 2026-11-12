import pandas as pd

def save_report(data,filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index = False)