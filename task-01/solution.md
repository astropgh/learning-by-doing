# Solution to Task 1: [git] Fork a repo and submit a pull request

## Steps

1. Fork `astropgh/learning-by-doing` repository

> Click the "fork" button on the upper right corner on GitHub.

2. Clone your fork

```bash
git clone git@github.com:yourusername/learning-by-doing.git
```

3. Checkout a new branch called `task/01`

```bash
cd learning-by-doing
git checkout -b task/01
```

4. Add your GitHub username to `task-01/completed.md`

```bash
echo "yourusername" >> task-01/completed.md
```

5. Commit your change to `task/01`

```bash
git add task-01/completed.md
git commit -m "add my username to complete task 01"
```

6. Push `task/01` to your fork

```bash
git push origin task/01
```

7. Submit a pull request

> Click "Create pull request" button on GitHub
