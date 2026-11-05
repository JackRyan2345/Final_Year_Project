from datetime import date, timedelta
from pathlib import Path
import time, io
import pandas as pd
import requests

# , "1191", "20184","30181","35271","30182","30183","30184","30185","30186","30187","30201","30202","30203","30188","30189","200713","20243","200722","200714","20205","20203"



SITES = {"20183"}
URL = ("https://data.tii.ie/Datasets/TrafficCountData/"
       "{d:%Y}/{d:%m}/{d:%d}/per-site-class-aggr-{d:%Y-%m-%d}.csv")
OUT = Path("raw/data"); OUT.mkdir(parents=True, exist_ok=True)

d, end = date(2025, 1, 1), date(2025,1, 2)
while d <= end:
    f = OUT / f"{d:%Y-%m-%d}.csv"
    if not f.exists():
        r = requests.get(URL.format(d=d), timeout=60)
        if r.status_code == 200:
            df = pd.read_csv(io.StringIO(r.text))
            df[df["Cosit"].astype(str).isin(SITES)].to_csv(f, index=False)
        else:
            print(d, "HTTP", r.status_code)
        time.sleep(0.3)
    d += timedelta(days=1)