import pandas as pd
from src.config import BRANCHES

def generate_branches():
    return pd.DataFrame(BRANCHES)
