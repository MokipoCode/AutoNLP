import pandas as pd
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def clean_data(df) :
    df = df.drop(columns=['county', "url", "image_url", "VIN"])
    df = df.dropna(subset=['manufacturer', 'title_status', "lat", 'long', 'model', 'odometer', 'fuel', 'transmission', 'year', 'id', 'region_url', 'region', 'price', 'description', 'state', 'posting_date'])
    df['year'] = pd.to_numeric(df['year'], errors="coerce").astype('Int64')
    df['odometer'] = pd.to_numeric(df['odometer'], errors="coerce").astype('Int64')
    df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce', utc=True)
    df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce')
    df['post_day'] = df['posting_date'].dt.day.astype('Int64')
    df['post_month'] = df['posting_date'].dt.month.astype('Int64')
    df['post_year'] = df['posting_date'].dt.year.astype('Int64')
    return df

df = pd.read_csv('data/vehicles.csv', encoding="utf-8")

total_rows = df.shape[0]
logging.info(f"Number of lines as input: {df.shape[0]} / Number of columns as input: {df.shape[1]}")

df = clean_data(df)

logging.info(f"Number of lines as output: {df.shape[0]} / Number of columns as output: {df.shape[1]}")
logging.info(f"Number of lines deleted: {round(((total_rows-df.shape[0]) / total_rows) * 100,1)}%")

to_pickle = "data/cleaned_data.pkl"
df.to_pickle(to_pickle)
logging.info(f'{to_pickle} created.')

to_csv = 'data/cleaned_data.csv'
df.to_csv(to_csv, index=False)
logging.info(f'{to_csv} created.') 