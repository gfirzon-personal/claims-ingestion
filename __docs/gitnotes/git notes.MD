To delete a remote branch in Git, you can use the following command:

```sh
git push origin --delete <branch-name>
```

### Steps
1. Open your terminal or command prompt.
2. Navigate to your Git repository.
3. Run the command, replacing `<branch-name>` with the name of the branch you want to delete.

### Example
If you want to delete a remote branch named `feature-branch`, you would run:

```sh
git push origin --delete feature-branch
```

This command tells Git to delete the `feature-branch` from the remote repository named `origin`.

List remote branches
```sh
git branch -r
```

List local branches
```sh
git branch -l
```

Delete local branch
```sh
git branch -D <local-branch-name>
```