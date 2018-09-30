# SQL (Structured Query Language)

"An RDBMS (Relational Database Management System) is a database management system based on the relational model..., which in turn is based on two mathematical branches: set theory and predicate logic" - *T-SQL Fundamentals | Itzik Ben-Gan*

## Overview

[Entity-Relationship (ER) Diagram visualization tool](https://erdplus.com/#/)

ER diagrams allows one to visualize how a concept might map into a  RDBMS layout, or visualize an existing RDBMS layout.

**SQL is case and whitespace insensitive**

## Querying

Basic structure:

```SQL
SELECT ...
FROM ...
JOIN ...
ON ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...;
```

Logical processing order of a SQL query:

```SQL
FROM ...
ON ...
WHERE ...
GROUP BY ...
HAVING ...
SELECT ...
DISTINCT ...
ORDER BY ...
TOP(LIMIT, OFFSET, FETCH, etc) ...
```

### Strings

To return rows that match a certain string/character sequence:

```SQL
WHERE <COLUMN> LIKE '%b'
# return all observations that end with a 'b' (can have any
# characters preceding the 'b')
```
```SQL
WHERE <COLUMN> LIKE 'b%'
# return all observations that start with a 'b' (can have any
# characters following the 'b')
```
```SQL
WHERE <COLUMN> LIKE '%b%'
# return all observations that contain a 'b' (can have any
# characters before or after the 'b')
```

## Database Management
