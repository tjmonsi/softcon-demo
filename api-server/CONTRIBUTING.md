# Contributing to Senti Natter

Please take a moment to review this document in order to make the contribution
process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of
the developers managing and developing this open source project. In return,
they should reciprocate that respect in addressing your issue or assessing
patches and features.


## Using the issue tracker

The issue tracker is the preferred channel for [bug reports](#bug-reports),
[new features or enhancements](#new-feature-or-enhancements), [chores](#chores),
[submitting merge requests](#merge-requests),
but please respect the following restrictions:

* Please **do not** use the issue tracker for personal support requests (use
  [Stack Overflow](http://stackoverflow.com) or IRC).

* Please **do not** derail or troll issues. Keep the discussion on topic and
  respect the opinions of others.

## Bug reports

To create a bug report:

A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1. **Use the Gitlab issue search** &mdash; check if the issue has already been
   reported.

2. **Check if the issue has been fixed** &mdash; try to reproduce it using the
   latest `develop` or development branch in the repository.

3. **Isolate the problem** &mdash; create a [reduced test
   case](http://css-tricks.com/6263-reduced-test-cases/) and a live example.

A good bug report shouldn't leave others needing to chase you up for more
information. Please try to be as detailed as possible in your report. What is
your environment? What steps will reproduce the issue? What browser(s) and OS
experience the problem? What would you expect to be the outcome? All these
details will help people to fix any potential bugs.

Example:

```
Title: The `paper-foo` element causes the page to turn pink when clicked.

### General Info
Paper-foo element causes the page to turn pink when clicked

### Expected Behavior
The page stays the same color.

### Current Behavior
The page turns pink.

### Possible Solution / Implementation / UI Design
Turn off changing of colors in page

### Steps to Reproduce (for bugs)
1. Put a `paper-foo` element in the page.
2. Open the page in a web browser.
3. Click the `paper-foo` element.

### Criteria for Acceptability
1. When `paper-foo` is clicked, it doesn't turn the page into pink

### Your Environment
* Version used: 0.4
* Browser Name and version: Chrome 67
* Operating System and version (desktop or mobile): Windows 10 Desktop
```

If it is possible, **please provide a reduced test case that demonstrates the problem**.


## New Features or Enhancements

New features or enhancements come here.

```
### General Info
Describe the new feature or enhancements here. Please
provide as much detail and context as possible.

### Expected Behavior
Describe the expected behavior here

### Possible Solution / Implementation / UI Design
Just create the page, and follow design in issue #1

### Criteria for Acceptability
1. When path is `/`, it should load `page-home`
2. `page-home` should have tag `hello-world`
3. Documentation exists

### Issue References
- requires #1
```

## Chores

Chores are enhancements like refactoring or cleaning code or improving
CI builds.

```
### General Info
Describe the chore, refactor, build, ci, or style change that you need to do and why.

### Possible Solution / Implementation / UI Design
Just create the page, and follow design in issue #1

### Issue References
- requires #1
```


## Merge requests

Good merge requests - patches, improvements, new features - are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

**Please ask first** before embarking on any significant pull request (e.g.
implementing features, refactoring code, porting to a different language),
otherwise you risk spending a lot of time working on something that the
project's developers might not want to merge into the project.

Please adhere to the coding conventions used throughout a project (indentation,
accurate comments, etc.) and any other requirements (such as test coverage).

When submitting pull requests, please provide:

1. **A reference to the corresponding issue** or issues that will be closed by the pull request. Please refer to these issues in the pull request description using the following syntax:
```
(For a single issue)
Fixes #20

(For multiple issues)
Fixes #32, fixes #40
```

2. **A succinct description of the design** used to fix any related issues. For example:
```
This fixes #20 by removing styles that leaked which would cause the page to turn pink whenever `paper-foo` is clicked.
```

3. **At least one test for each bug fixed or feature added as part of the pull request.** We will still consider approving your pull request but if you can add a test, please add them :)

To contribute your work:

1. After cloning, get the latest changes from upstream:

   ```bash
   git checkout <dev-branch>
   git pull upstream <dev-branch>
   ```

2. Create a new topic branch (off the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

3. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

4. Locally merge (or rebase) the upstream development branch into your topic branch:

   ```bash
   git pull [--rebase] upstream <dev-branch>
   ```

5. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

6. [Open a Merge Request](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html)
    with a clear title and description.


## Contributing Rules

Adding an additional npm package without a clear detail on why it should be added and the byte impact it would add on core-shell or any other page will be disapproved immediately.

I know this is not inherent in the docs (and I think I now have to add that) but I am focusing on making this a performant site. Adding packages at whim is an anti-pattern and I discourage the use of extra libraries without a clear reason WHY it should be part of the app.


## Conventions of commit messages

Adding files on repo

```bash
git commit -m "Add filename"
```

Updating files on repo

```bash
git commit -m "Update filename, filename2, filename3"
```

Removing files on repo

```bash
git commit -m "Remove filename"
```

Renaming files on repo

```bash
git commit -m "Rename filename"
```

Fixing errors and issues on repo

```bash
git commit -m "Fix #issuenumber Message about this fix"
```

Adding features on repo

```bash
git commit -m "Add Feature: nameoffeature Message about this feature"
```

Updating features on repo

```bash
git commit -m "Update Feature: nameoffeature Message about this update"
```

Removing features on repo

```bash
git commit -m "Remove Feature: nameoffeature Message about this"
```

Ignoring Travis CI build on repo

```bash
git commit -m "Commit message here [ci-skip]"
```

**IMPORTANT**: By submitting a patch, you agree to allow the project owner to
license your work under the same license as that used by the project.