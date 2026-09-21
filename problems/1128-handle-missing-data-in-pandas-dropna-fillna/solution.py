import pandas as pd
def solution(df):
    df = df.copy()
    df = df.loc[:, df.isna().mean() <= 0.5]
    df = df.loc[df.isna().mean(axis=1) <= 0.5]
    for col in df.columns:
        if df[col].isna().any():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].mean())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
    return df.reset_index(drop=True)