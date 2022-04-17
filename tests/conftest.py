import polars as pl
from pytest import fixture

from core.src.filter import FilterConfig


@fixture
def test_df() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "route_id": [
                145,
                78,
                166,
                9,
                193,
                77,
                61,
                32,
                70,
                179,
            ],
            "order_id": [
                254,
                274,
                246,
                296,
                425,
                256,
                388,
                140,
                122,
                34,
            ],
            "sku_id": [
                13,
                133,
                36,
                966,
                399,
                701,
                859,
                306,
                455,
                7,
            ],
            "origin_id": [
                1,
                3,
                3,
                2,
                1,
                1,
                1,
                2,
                1,
                1,
            ],
            "origin_city": [
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
                "Philadelphia",
            ],
            "origin_state": [
                "PA",
                "PA",
                "PA",
                "PA",
                "PA",
                "PA",
                "PA",
                "PA",
                "PA",
                "PA",
            ],
            "origin_zip": [
                "20134",
                "20134",
                "20134",
                "20134",
                "20134",
                "20134",
                "20134",
                "20134",
                "20134",
                "20134",
            ],
            "origin_country": [
                "US",
                "US",
                "US",
                "US",
                "US",
                "US",
                "US",
                "US",
                "US",
                "US",
            ],
            "dest_id": [
                0,
                0,
                0,
                2,
                2,
                3,
                2,
                1,
                0,
                2,
            ],
            "dest_city": [
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
                "Vancouver",
            ],
            "dest_state": [
                "BC",
                "BC",
                "BC",
                "BC",
                "BC",
                "BC",
                "BC",
                "BC",
                "BC",
                "BC",
            ],
            "dest_zip": [
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
                "ABC DFG",
            ],
            "dest_country": [
                "CA",
                "CA",
                "CA",
                "CA",
                "CA",
                "CA",
                "CA",
                "CA",
                "CA",
                "CA",
            ],
            "weight": [
                94.6725,
                295.7922,
                276.9651,
                33.8384,
                62.2545,
                281.5952,
                181.2096,
                281.6563,
                101.5503,
                38.6294,
            ],
            "weight_uom": [
                "LBS",
                "LBS",
                "LBS",
                "LBS",
                "LBS",
                "LBS",
                "LBS",
                "LBS",
                "LBS",
                "LBS",
            ],
            "quantity": [
                4.0842,
                1.7737,
                1.7101,
                7.949,
                7.4064,
                5.0239,
                5.39,
                4.8918,
                2.0493,
                0.7542,
            ],
            "quantity_uom": [
                "PLT",
                "PLT",
                "PLT",
                "PLT",
                "PLT",
                "PLT",
                "PLT",
                "PLT",
                "PLT",
                "PLT",
            ],
            "linehaul_cost": [
                516.2955,
                454.4441,
                169.8867,
                878.5464,
                138.7028,
                922.9187,
                819.2862,
                577.3692,
                -981.2893,
                -577.803,
            ],
            "linehaul_cost_uom": [
                "USD",
                "USD",
                "USD",
                "USD",
                "USD",
                "USD",
                "USD",
                "USD",
                "USD",
                "USD",
            ],
        }
    )


@fixture
def test_filter_config() -> FilterConfig:
    return [
        {
            "data": {"name": "origin", "values": {"country": "US"}},
            "type": "include",
            "operator": "equal-to",
        },
        {
            "data": {"name": "origin", "values": {"country": "CA"}},
            "type": "exclude",
            "operator": "equal-to",
        },
    ]
