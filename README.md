# example-pipeline

Example data pipeline project to experiment with products.

## Subject

- CSV file for simplicity
- Invalid data needing corrections
- Target format requirement data manipulation
- Task failure due to unexpected data

## Goals

- Evaluate frameworks for centralizing visibility
  - Design
  - Failures
  - Logging
  - Metrics
- Evaluate `DataFrame` libraries (specifically `polars`)
- Evaluate scale from both design and implementation perspectives
- Evaluate system flexibility and infrastructure requirements

## The Data

This project processes shipment data from a denormalized, queried format.

|route_id|order_id                     |sku_id|origin_id                                    |origin_city |origin_state|origin_zip|origin_country|dest_id|dest_city|dest_state|dest_zip|dest_country|weight            |weight_uom|quantity         |quantity_uom|linehaul_cost      |linehaul_cost_uom|
|--------|-----------------------------|------|---------------------------------------------|------------|------------|----------|--------------|-------|---------|----------|--------|------------|------------------|----------|-----------------|------------|-------------------|-----------------|
|72      |465                          |292   |1                                            |Philadelphia|PA          |20134     |US            |2      |Vancouver|BC        |ABC DFG |CA          |279.429           |LBS       |3.2372           |PLT         |-344.4967          |USD              |

## Usage

### Run Jobs

```shell
make run
```

### Help

```shell
make help
```
