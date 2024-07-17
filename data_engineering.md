# DBT

"dbt’s only function is to take code, compile it to SQL, and then run against your database" - [documentation](https://www.getdbt.com/blog/what-exactly-is-dbt/)

* Every model (model: a data transformation, expressed as a single `SELECT` statement)

# Data Warehousing

Data warehouse vs data warehouse server

## Kimball Dimensional Modeling

* The end use case should define the grain

```SQL
SELECT 
         <Column_1>,
         <Column_2>,
         <Column_3>,
         <Column_4>,
    SUM( <Column_5> ),
FROM <table_A>
WHERE
    <<Column_1> condition> AND
    <<Column_2> condition>
GROUP BY
    <Column_3>,
    <Column_4>;



```



### Questions

* ( 2022-08-26 ): Should the grain be consistent across all fact tables? Is there value in having different grain levels
  depending on the use case?


