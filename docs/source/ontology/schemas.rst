Schema For Jeremy's Ontology
----------------------------

Sorry but also not sorry.

Write Optimized Table:
======================

Concept
~~~~~~~

Concepts appear in data. Their types determine where they can be in the cdm.

id: int
name: varchar
concept_type: varchar

Relationship
~~~~~~~~~~~~

Relationships are used to transform data.

For example, in queries:

```sql
select * from <table>.<column_name> 
where concept_id in (
    select concept_relationship_2 
    where relationship_type = "<relationship_type>"
    and concept_id_1 = <concept>
);
```

relationship_id: int
concept_id_1: int
concept_id_0: int
relationship_type: int


Question:

Does the relationship_type determine the types of the concepts?

Concept Type
~~~~~~~~~~~~

Type primarily determines where you can find them in the data. As columns in 
relational databases have specified types (float, int, etc.), a concept's 
'type' determines it's type.

type: str
table_name: str
column_name: str

Relationship Type
~~~~~~~~~~~~~~~~~

Relationship types impose contracts on the relationships between the tables.

relationship_type: int
concept_id_1_type: int
concept_id_1_type: int

These ensure consistency of data types in join statements.

Read Optimized Tables
---------------------

Vertex
~~~~~~

Join of the concept and type tables

name: varchar
id: int
type: varchar
table_name: str
column_name: str

Edge
~~~~

Join of the vertex, relationship and relationship type tables

concept_id_1: int
concept_name_1: varchar
type_1: varchar
table_name_1: str
column_name_1: str

concept_id_2: int
concept_name_2: varchar
type_2: varchar
table_name_2: str
column_name_2: str

relationship_id: int
relationship_type: str


Example Denormalization Scripts
-------------------------------
