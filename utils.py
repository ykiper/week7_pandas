import pandas as pd
import re
def clean_and_convert(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['total_amount'].str.replace("$", "")
    df['total_amount'] = df['total_amount'].apply(pd.to_numeric)
    return df

def clean_html(df):
    df['items_html'] = df['items_html'].apply(lambda x: re.sub(r"<.*?>", " ", x))
    return df

def update_no_coupon(df):
    df['coupon_used'] = df['coupon_used'].replace({"":"no coupon"})
    return df


def create_order_month(df):
    df['order_month'] = df['order_date'].dt.month
    return df

def total_amoumt_map(df):
    if df['total_amount'] > df['total_amount'].mean():
        return True
    else:
        return False


def filter_by_amount_and_rating(df):
    df = df[(df['total_amount'] > 1000) & (df['rating'] > 4.5)]
    return df
