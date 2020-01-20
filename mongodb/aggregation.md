# Aggregation
{id: mongodb-aggregation}

## Aggregation framework
{id: mongodb-aggregation-framework}

* OLTP = Online Transaction Processing (sell tickets, registreations)
* OLAP = Online Analytical Procession (which tickets make the most money, how to predict usage)



## A Processing Pipeline
{id: mongodb-processing-pipeline}

```
Limit -> Match -> Project -> Group -> Sort -> Out
```


## Pipeline Operators
{id: mongodb-pipeline-operators}

```
$match          Filter documents
$project        Reshape documents
$group          Summarize documents
$unwind         Expand arrays in documents
$sort           Order documents
$limit/$skip    Paginate documents
$redact         Restrict documents
$geoNear        Proximity sort documents
$let, $map      Define variables
$out
$lookup
```




## Example: Insert data
{id: mongodb-aggregation-example-1}

```
use demo
db.simple.insert({ "name" : "foo", "cnt" : 3 })
db.simple.insert({ "name" : "foo", "cnt" : 4 })
db.simple.insert({ "name" : "foo", "cnt" : 5 })
db.simple.insert({ "name" : "bar", "cnt" : 5 })
db.simple.insert({ "name" : "bar", "cnt" : 9 })
```


## Show data
{id: mongodb-aggregation-example-2}

```
db.simple.find()

{
  "_id": ObjectId("5988aeb33b04d96991d11159"),
  "name": "foo",
  "cnt": 3
}
{
  "_id": ObjectId("5988aeb33b04d96991d1115a"),
  "name": "foo",
  "cnt": 4
}
{
  "_id": ObjectId("5988aeb33b04d96991d1115b"),
  "name": "foo",
  "cnt": 5
}
{
  "_id": ObjectId("5988aeb33b04d96991d1115c"),
  "name": "bar",
  "cnt": 5
}
{
  "_id": ObjectId("5988aeb43b04d96991d1115d"),
  "name": "bar",
  "cnt": 9
}
Fetched 5 record(s) in 4ms
```


## Group by name and sum - $sum
{id: mongodb-aggregation-example-3}
{i: $group}
{i: $sum}

```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $sum : "$cnt" } } } ])

{
  "result": [
    {
      "_id": "bar",
      "total": 14
    },
    {
      "_id": "foo",
      "total": 12
    }
  ],
  "ok": 1
}
```



## Group by name and caluclate average $avg
{id: mongodb-aggregation-example-4}
{i: $avg}

```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $avg : "$cnt" } } } ] )

{
  "result": [
    {
      "_id": "bar",
      "total": 7
    },
    {
      "_id": "foo",
      "total": 4
    }
  ],
  "ok": 1
}
```


## Group by name $max, $min
{id: mongodb-aggregation-example-5}



## Group by name and count
{id: mongodb-aggregation-example-6}

```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $sum : 1 } } } ] )

{
  "result": [
    {
      "_id": "bar",
      "total": 2
    },
    {
      "_id": "foo",
      "total": 3
    }
  ],
  "ok": 1
}
```


## All the elements - sum
{id: mongodb-aggregation-example-7}
{i: null}

```
db.simple.aggregate( [ { $group: { _id: null, total: { $sum : "$cnt" } } } ] )

{
  "result": [
    {
      "_id": null,
      "total": 26
    }
  ],
  "ok": 1
}
```



## All the elements - sum
{id: mongodb-aggregation-example-8}

We can also use an arbitrary string instead of the **null**



```
db.simple.aggregate( [ { $group: { _id: "total", total: { $sum : "$cnt" } } } ])

{
  "result": [
    {
      "_id": "total",
      "total": 26
    }
  ],
  "ok": 1
}
```



## $match (filter)
{id: mongodb-aggregation-example-9}
{i: $match}
{i: filter}

```
db.simple.aggregate( [ { $match : { name: "foo" } } ] )

{
  "result": [
    {
      "_id": ObjectId("5988aeb33b04d96991d11159"),
      "name": "foo",
      "cnt": 3
    },
    {
      "_id": ObjectId("5988aeb33b04d96991d1115a"),
      "name": "foo",
      "cnt": 4
    },
    {
      "_id": ObjectId("5988aeb33b04d96991d1115b"),
      "name": "foo",
      "cnt": 5
    }
  ],
  "ok": 1
}
```


## $match (filter) and the total
{id: mongodb-aggregation-example-10}

```
db.simple.aggregate( [
    { $match : { name: "foo" } },
    { $group: { _id: "total", total: { $sum : "$cnt" } } }
] )

{
  "result": [
    {
      "_id": "total",
      "total": 12
    }
  ],
  "ok": 1
}
```



## $match with $gt
{id: mongodb-aggregation-example-11}

```
db.simple.aggregate( [
    { $match : { cnt: { $gt: 4 } } },
    { $group: { _id: "total", total: { $sum : "$cnt" } } }
] )

{
  "result": [
    {
      "_id": "total",
      "total": 19
    }
  ],
  "ok": 1
}
```



## $group with $push
{id: mongodb-aggregation-example-12}

```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $push : "$cnt" } } } ])

{
  "result": [
    {
      "_id": "bar",
      "total": [
        5,
        9
      ]
    },
    {
      "_id": "foo",
      "total": [
        3,
        4,
        5
      ]
    }
  ],
  "ok": 1
}
```


## New data set
{id: mongodb-aggregation-example-20}

```
db.scores.insert({ "name": "foo", "scores" : [ 2, 4, 6] })
db.scores.insert({ "name": "bar", "scores" : [ 9, 5, 3, 1] })
```


## New data set
{id: mongodb-aggregation-example-21}

```
db.scores.find()

{
  "_id": ObjectId("5988c63dd474ca272db3fb2e"),
  "name": "foo",
  "scores": [
    2,
    4,
    6
  ]
}
{
  "_id": ObjectId("5988c676d474ca272db3fb2f"),
  "name": "bar",
  "scores": [
    9,
    5,
    3,
    1
  ]
}
Fetched 2 record(s) in 21ms
```


## $unwind
{id: mongodb-aggregation-example-22}
{i: $unwind}

```
db.scores.aggregate( [ { $unwind: "$scores" } ] );

{
  "result": [
    {
      "_id": ObjectId("5988c63dd474ca272db3fb2e"),
      "name": "foo",
      "scores": 2
    },
    {
      "_id": ObjectId("5988c63dd474ca272db3fb2e"),
      "name": "foo",
      "scores": 4
    },
    {
      "_id": ObjectId("5988c63dd474ca272db3fb2e"),
      "name": "foo",
      "scores": 6
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 9
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 5
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 3
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 1
    }
  ],
  "ok": 1
}
```


## $unwind and $group
{id: mongodb-aggregation-example-23}

```
db.scores.aggregate( [
    { $unwind: "$scores" },
    { $group: { _id: "$name", score: { $sum: "$scores" } } }
] )

{
  "result": [
    {
      "_id": "bar",
      "score": 18
    },
    {
      "_id": "foo",
      "score": 12
    }
  ],
  "ok": 1
}
```


## $unwind and $group and $sort
{id: mongodb-aggregation-example-24}

```
db.scores.aggregate( [
    { $unwind: "$scores" },
    { $group: { _id: "$name", score: { $sum: "$scores" } } }, 
    { $sort: { "score" : 1 } }
] )

{
  "result": [
    {
      "_id": "foo",
      "score": 12
    },
    {
      "_id": "bar",
      "score": 18
    }
  ],
  "ok": 1
}
```



## $match
{id: mongodb-aggregation-example-25}
{i: $match}

```
db.scores.aggregate( [ { $match: { name: "bar" } } ] )

{
  "result": [
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": [
        9,
        5,
        3,
        1
      ]
    }
  ],
  "ok": 1
}
```


## $match and $unwind and $group
{id: mongodb-aggregation-example-26}

```
db.scores.aggregate( [
    { $match: { name: "bar" } },
    { $unwind: "$scores" },
    { $group: { _id: "$name", score: { $sum: "$scores" } } }
] )

{
  "result": [
    {
      "_id": "bar",
      "score": 18
    }
  ],
  "ok": 1
}
```




