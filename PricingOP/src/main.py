import pandas as pd
from pathlib import Path 

"""
Overall needs :
sku, units, buy_price, sell_price, ship_unit
A Dictionary of Skus with sell price/item name
Later we may also time and fixed shipping cost
we also could have a min order or max order
current stock
lead time


"""




def load_demand(path: Path) -> pd.DataFrame:
    """Read an excel or csv demand file and return
    a tidy DF with columns: sku, units, month, year"""
    df = pd.read_excel(path) if path.suffix in (".xls", ".xlsx") else pd.read_csv(path)
    df.columns = df.columns.str.lower().str.strip()
    return df[["sku", "units", "month", "year", "price"]]

def test_load_demand(tmp_path):
    tmp_file = tmp_path / "demo.csv"
    tmp_file.write_text("sku,units,month,year,price\nA1,100,8,2025,50.00")
    df = load_demand(tmp_file)
    assert df.shape == (1,5) #1 row, 4 columns
    
tester1 = [394319391828, 15, 8, 2025, 5.99] # 12 digit sku, 15 units, August 2025, 5.99 price
tester2 = [351239569180, 20, 9, 2025, 5.28] # 12 digit sku, 20 units, September 2025, 5.28 price




