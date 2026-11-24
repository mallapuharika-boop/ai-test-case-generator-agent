
import pandas as pd

def export_to_csv(test_cases):
    df = pd.DataFrame(test_cases)
    return df.to_csv(index=False).encode("utf-8")
