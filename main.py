import numpy as np
import pandas as pd
import re
from utils import (clean_and_convert, clean_html, create_order_month
, update_no_coupon, filter_by_amount_and_rating)
import datetime


df = pd.read_json("orders_simple.json")


df = clean_and_convert(df)
df = clean_html(df)

df = update_no_coupon(df)

df = create_order_month(df)

df['high_value_order'] = np.where(df['total_amount'] > df['total_amount'].mean(), True, False)


df = filter_by_amount_and_rating(df)

df['delivery_status'] = np.where(df['shipping_days'] > 7, "delayed", "on time")
df = df.sort_values('total_amount', ascending=False)




df.to_csv("clean_orders_314699323.csv")