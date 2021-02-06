# Github actions testing

## on.<push|pull_request>.paths

Experiment:

```
$ ./yes/update.sh
$ git checkout -b gat-branch
$ git commit -a -m "yes path updated"
$ git push origin gat-branch

# open PR
# two checks ran: pull & pull_request

$ ./yes/update.sh
$ git checkout -b gat-branch
$ git commit -a -m "yes path updated 2"
$ git push origin gat-branch

# check PR
# two checks ran: pull & pull_request


$ ./no/update.sh
$ git checkout -b gat-branch
$ git commit -a -m "no path updated 1"
$ git push origin gat-branch

# check PR
# ONLY one check ran: pull_request


# merge PR
# ONLY one check ran: push
```

reference: https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#git-diff-comparisons
