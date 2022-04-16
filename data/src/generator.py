# %%
# setup
import numpy as np
import polars as pl

# save dataframe to
RES_FILEPATH = "./shipments.csv"

# number of rows
N = 1000

# number of ROUTES loads
ROUTES = 200

assert ROUTES <= N, "Cannot have more routes than rows"

# number of unique orders
ORDERS = 500

assert ORDERS <= N, "Cannot have more orders than rows"
assert ORDERS >= ROUTES, "Cannot have less orders than routes"

# number of unique skus
SKUS = N

# types of unit of measures
WEIGHT_UOMS = ["LBS"]
QUANTITY_UOMS = ["PLT"]
LINEHAUL_COST_UOMS = ["USD"]

# maximum measurables
MAX_WEIGHT = 300
MAX_QUANTITY = 10

# location data
CITIES = ["Philadelphia", "New York", "San Francisco", "Vancouver"]
STATES = ["PA", "NY", "CA", "BC"]
ZIPCODES = ["20134", "12343", "43204", "ABC DFG"]  # not real
COUNTRIES = ["US", "US", "US", "CA"]

assert (
    len(CITIES) == len(STATES) == len(ZIPCODES) == len(COUNTRIES)
), "Length of location data must match"

# %%
# IDs

route_id = np.random.randint(0, ROUTES, (N,))
order_id = np.random.randint(0, ORDERS, (N,))
sku_id = np.random.randint(0, SKUS, (N,))
origin_id = np.random.randint(0, len(CITIES), (N,))
dest_id = np.random.randint(0, len(CITIES), (N,))

# %%
# measurables

# allow bad values like 0
weight = np.random.uniform(0, MAX_WEIGHT, (N,)).round(4)
quantity = np.random.uniform(0, MAX_QUANTITY, (N,)).round(4)
linehaul_cost = np.random.uniform(-1000, 1000, (N,)).round(4)


# %%
# other data

origin_city = []
origin_state = []
origin_zip = []
origin_country = []
dest_city = []
dest_state = []
dest_zip = []
dest_country = []

# create valid and invalid data
for i in range(len(CITIES)):
    origin_city += [CITIES[i]] * (N // len(CITIES))
    origin_state += [STATES[i]] * (N // len(STATES))
    origin_zip += [ZIPCODES[i]] * (N // len(ZIPCODES))
    origin_country += [COUNTRIES[i]] * (N // len(COUNTRIES))

for i in range(len(CITIES) - 1, -1, -1):
    dest_city += [CITIES[i]] * (N // len(CITIES))
    dest_state += [STATES[i]] * (N // len(STATES))
    dest_zip += [ZIPCODES[i]] * (N // len(ZIPCODES))
    dest_country += [COUNTRIES[i]] * (N // len(COUNTRIES))

# fill any remaining rows with missing data
nulls = [None] * (N - len(origin_city))
origin_city += nulls
origin_state += nulls
origin_zip += nulls
origin_country += nulls
dest_city += nulls
dest_state += nulls
dest_zip += nulls
dest_country += nulls

weight_uom = []
for i in range(len(WEIGHT_UOMS)):
    weight_uom += [WEIGHT_UOMS[i]] * (N // len(WEIGHT_UOMS))

weight_uom += [None] * (N - len(weight_uom))

quantity_uom = []
for i in range(len(QUANTITY_UOMS)):
    quantity_uom += [QUANTITY_UOMS[i]] * (N // len(QUANTITY_UOMS))

quantity_uom += [None] * (N - len(quantity_uom))

linehaul_cost_uom = []
for i in range(len(LINEHAUL_COST_UOMS)):
    linehaul_cost_uom += [LINEHAUL_COST_UOMS[i]] * (
        N // len(LINEHAUL_COST_UOMS)
    )

linehaul_cost_uom += [None] * (N - len(linehaul_cost_uom))

# %%
# create shipments


def create_df() -> pl.DataFrame:
    df = pl.DataFrame(
        {
            "route_id": route_id,
            "order_id": order_id,
            "sku_id": sku_id,
            "origin_id": origin_id,
            "origin_city": origin_city,
            "origin_state": origin_state,
            "origin_zip": origin_zip,
            "origin_country": origin_country,
            "dest_id": dest_id,
            "dest_city": dest_city,
            "dest_state": dest_state,
            "dest_zip": dest_zip,
            "dest_country": dest_country,
            "weight": weight,
            "weight_uom": weight_uom,
            "quantity": quantity,
            "quantity_uom": quantity_uom,
            "linehaul_cost": linehaul_cost,
            "linehaul_cost_uom": linehaul_cost_uom,
        }
    )

    return df


if __name__ == "__main__":
    df = create_df()
    df.write_csv(RES_FILEPATH)
