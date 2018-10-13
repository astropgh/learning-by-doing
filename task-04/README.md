# Task 4: [database]  Preparing for data scraping: design a data model for top baby names

## Background

Before we start to scrape the top baby names from the webpage, we need to design
a data model that we will use to store the data.

The term "data model" has different meanings in different contexts.
We can ask what kind of object the data will be stored in.
A python list? A python dictionary? A pandas data frame?
For a given type, we can further ask how the data is stored.
For example, if we store the data in a pandas data frame, we can ask what
are the columns and rows.

Let's look at some examples.
The original webpage store the names as a table, with columns being
`year`, `female_rank1`, `female_rank2`, `male_rank1`, `male_rank2`..., and
each row corresponds to one single year.

A more extreme example would be storing the names as a sequence (say a python list),
the content of the sequence will be the names, while the indices of the sequence encode
year, ranking, and gender altogether. A possible way to encode the information is
```python
year = 2017 - index // 10
rank = index % 5 + 1
gender = 'female' if index % 10 < 5 else 'male'
```
While this data model preserves all the information, it is unlikely that this
model will be very convenient when it comes to data exploration.

Yet another totally different data model is to group the data by names.
Let's say we'll store the data in a python dictionary. A possible way is:
```python
{
    'Emma':{
        'gender': 'female',
        'years_ranked_1': [2017, 2016, 2015, 2014, ...],
        'years_ranked_2': [2013, 2012, 2009, ...],
        'years_ranked_3': [...],
    },
    'Noah':{
        ...,
    },
    ...,
}
```

Note that the form (object) that the data is stored and how the data is structured
are two different things. (*Food for thoughts: why? can you give an example?*)

Clearly, the choice of data model heavily depends on the questions that we would
like to answer with the data.
If the amount of data is very large, we will also need to consider the avabilable
computing resources like memory usage and I/O speed when designing the data model.
For now, we don't yet need to worry about the limitation due to computing resources.


## Task

Try to come up with a data model that is good for answering each of the following questions.
Think about the code you'll need to write to interact with the data model to answer
these questions.

1. Which years Emma is the most chosen names?
2. Which name had been the most chosen name for the longest consecutive years?
3. How many unique male names have be on top 5 between years 1980 and 2000?
4. Are there more unique male names or more unique female names that are on top 5?
5. What is the distribution of the numbers of consecutive years that a male name remains the most chosen name?
