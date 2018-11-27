# Task 10: Retrive data using GitHub API

In this task, we will learn to use [GitHub's REST API](https://developer.github.com/v3/)
to retrive some data from GitHub.

The [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API is
a very common [API](https://en.wikipedia.org/wiki/Application_programming_interface)
design. All actions are completed by accessing specific URLs, and the server will
response with data (usually in [JSON](https://en.wikipedia.org/wiki/JSON) format).

As usual, in the spirit of learning by doing, let's learn more about REST API by
trying it out directly. You'll find that this task does not involve a lot of coding,
but more manual reading, because that's how we figure out which URL
corresponds to which resources and also the data model the serve returns to us.

GitHub's REST API is very well [documented](https://developer.github.com/v3/), and that is why we will start with it.

Let's look at this very simple example which prints out all the (public) repositories
owned by the `astropgh` organization:

```python
import json
import requests

repos = json.loads(requests.get('https://api.github.com/orgs/astropgh/repos').text)
print([repo['name'] for repo in repos])
```

> **[ACTION]** Run the above code and see what you get!

The first question you might ask is how we knew that this URL would return the
information we are looking for. This is in fact documented
[here](https://developer.github.com/v3/repos/#list-organization-repositories).

> **[ACTION]** Visit the URL https://api.github.com/orgs/astropgh/repos in your browser and see what you get.

The text you see when you visit the API URL above is the data represented in the JSON format,
and `json.loads` turns them into a python object, in this case, a list of dictionaries.

> **[ACTION]** Print out the creation date/time of each repo under `astropgh`.
> How do you find out the key to use to obtain this information?

Now, let's say we want to list all the pull requests of this repo `astropgh/learning-by-doing`.

> **[ACTION]** Print out the titles of all the open pull requests in `astropgh/learning-by-doing`.
>
> *Hints*:
> - [See this page of the documentation](https://developer.github.com/v3/pulls/#list-pull-requests).
> - To supply parameters when using `requests`, you can simply do:
>   ```python
>   requests.get(url, {'param1': value1, 'param2': value2})
>   ```

OK, here are a few more actions for you to try: (Write Python code to get the answers.)

1. Find out which user has submitted the most PRs in `astropgh/learning-by-doing`.
2. Find out how many commits have been made to the master branch of `numpy/numpy` in 2018 October.
3. (cont'd after 2) Find out how many distinct users made those commits.
4. List all the branch names in `numpy/numpy`.
