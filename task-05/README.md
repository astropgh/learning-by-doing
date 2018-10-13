# Task 5: [git] Merge and rebase

*prerequisites*: [Task 1](../task-01), [Task 2](../task-02)

We will now learn two basic operations of git branches: merge and rebase.
As always, you can find lots of information about this on the Internet,
and here we will go ahead to learn by trying them out.

## Part 1
Complete Level 1 through 4 on https://learngitbranching.js.org/

## Part 2
1. Go back to your clone of `learning-by-doing`. Make sure you've completed Tasks [1](../task-01) and [2](../task-02).
2. Do **only** Step 2 of [Task 2](../task-02) again.
3. Now the `master` branch and your `task/01` branch have diverged, and you will rebase `task/01` onto `master`.
4. Go to see your PR at https://github.com/astropgh/learning-by-doing/pulls, does it somehow change? Why?

## Part 3
*Note: Do Part 2 first!*

1. Checkout a new branch called `task/05` from `master` (*What does this mean?*)
2. Add a new file `task-05/test` and commit it to `task/05`
3. Merge `task/05` into `task/01`
4. Go to see your PR at https://github.com/astropgh/learning-by-doing/pulls, does it somehow change? Why?

## Food for thought
- What's the difference between "rebase" and "merge"?
