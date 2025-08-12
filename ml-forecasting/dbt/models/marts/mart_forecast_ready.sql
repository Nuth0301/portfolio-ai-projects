-- Example mart: ready for BI consumption
select * from {{ ref('int_feature_matrix') }}
