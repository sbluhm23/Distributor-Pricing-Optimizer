import pandas as pd
from pathlib import Path 
import pulp 

"""
Overall needs :
sku, units, buy_price, sell_price, ship_unit
A Dictionary of Skus with sell price/item name
Later we may also time and fixed shipping cost
we also could have a min order or max order
current stock
lead time

Current Goal:
Generate objective function solver with test data

Next Steps: 
Create a way to parse data into compatiable dicitonary format
Create a way to pull data from websites using requests or API
Generate simple solutions within console 
Create user GUI to input other date
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
    
# Example data structure for distributors
# This is a dictionary of dictionaries, where each distributor has its own products
# Each product is represented by a dictionary with its attributes

# one mega dictionary will hold all distributor data 
distributors = dict({
    "DistributorTestA": {
        "a": {
            "sku": "394319391828",
            "name": "Product A",
            "buy_price": 2.99,
            "sell_price": 5.99,
            "ship_unit": 0.50,
            "current_stock": 100
        },
        "b": {
            "sku": "351239569180",
            "name": "Product B",
            "buy_price": 3.99,
            "sell_price": 5.28,
            "ship_unit": 0.75,
            "current_stock": 150
        }
    },
    "DistributorTestB": {
        "a": {
            "sku": "394319391828",
            "name": "Product A",
            "buy_price": 1.99,
            "sell_price": 4.99,
            "ship_unit": 0.60,
            "current_stock": 200
        },
        "b": {
            "sku": "351239569180",
            "name": "Product B",
            "buy_price": 4.99,
            "sell_price": 6.28,
            "ship_unit": 0.80,
            "current_stock": 250
        }
    }
})
test_budget = 3000.00

items = [(d,t) for d in distributors for t in distributors[d]]

buy = {(d,t): distributors[d][t]["buy_price"] for d,t in items} #pulls buy price out of items
sell = {(d,t): distributors[d][t]["sell_price"] for d,t in items} #pulls sell price out of items
ship = {(d,t): distributors[d][t]["ship_unit"] for d,t in items}#pulls shipping cost out of items
stock = {(d,t): distributors[d][t]["current_stock"] for d,t in items}#pulls current stock

margin = {(d,t): sell[d,t] - buy[d,t] - ship[d,t] for d,t in items}# Grabs the margin for each 



#Objective function maximize profits
# 4 products so 4 variables, w,x,y,z In the final problem we may stucture this differently
##for multiple products we can use indices 

model = pulp.LpProblem("profit_max", pulp.LpMaximize) #create model to maximize profits
#make decisions variables

#makes it so only whole units can be bought
q = pulp.LpVariable.dicts("q", items, lowBound=0, cat="Integer") 

#objective function 
model += pulp.lpSum(margin[d,t] * q[(d,t)] for d,t in items), "TotalProfit"

# Budget constraint: spend = (buy+ship) * q
model += pulp.lpSum((buy[d,t] + ship[d,t]) * q[(d,t)] for d,t in items) <= test_budget, "Budget"

# Availability / stock caps
for d,t in items:
    model += q[(d,t)] <= stock[(d,t)], f"StockCap_{d}_{t}"

model.solve(pulp.PULP_CBC_CMD(msg=False))

solution = { (d,t): int(q[(d,t)].value()) for d,t in items if q[(d,t)].value() and q[(d,t)].value() > 1e-6 }
profit = pulp.value(model.objective)
print("Buy plan:", solution)
print("Profit: $", round(profit, 2))