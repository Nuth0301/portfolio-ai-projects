-- Example: build simple feature matrix (placeholder)
with d as (select * from {{ ref('stg_demand') }})
select *
from d
