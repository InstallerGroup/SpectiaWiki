# Trunk-Based Development Strategy for Microservices (Without Release Branches)

## Overview

In our development process, we will be adopting a trunk-based development strategy without the use of a separate release branch. Trunk-based development is a version control strategy where all developers continuously integrate their changes into a single branch, known as the trunk or main branch. This approach emphasizes simplicity, fast feedback, and a high level of code quality, ensuring that the trunk is always in a deployable state.

## Objectives

- Simplify Branching: By eliminating release branches, we maintain a straightforward workflow where all development happens on the trunk.
- Enhance Continuous Integration: Regular commits to the trunk enable continuous integration and testing, identifying issues early.
- Accelerate Deployment Cycles: Ensuring the trunk is always in a deployable state allows for more frequent, reliable releases.

## Branching Model

### 1. Trunk (Main) Branch

- The trunk is the primary branch where all developers commit their code.
- The trunk should always be in a stable, deployable state with passing tests and code that meets our coding standards.
- No long-lived branches are allowed; changes should be integrated into the trunk as frequently as possible.

### 2. Short-Lived Feature Branches

- Feature branches are used for small, incremental changes, bug fixes, or experimental features.
- These branches should be short-lived, ideally lasting less than a day or two.
- Once a feature is complete and has passed testing, it should be merged back into the trunk.
- Developers should frequently rebase feature branches against the trunk to avoid merge conflicts and ensure they remain up-to-date.

## Workflow

### Daily Development

1. Start with the Trunk: Begin each day by pulling the latest changes from the trunk.
1. Create a Feature Branch (if needed): For small tasks or features, create a new branch from the trunk.
1. Implement and Test: Develop the feature or fix, ensuring all tests pass.
1. Rebase Regularly: Rebase your feature branch frequently to keep it in sync with the trunk.
1. Commit and Push: Once your work is complete, commit and push it to your feature branch.
1. Code Review: Submit a pull request (PR) for a code review.
1. Merge to Trunk: After approval, merge your changes into the trunk. Ensure that the trunk remains stable and that all tests pass after the merge.

### Continuous Integration (CI)

1. Automated Builds: Every commit to the trunk triggers an automated build process.
1. Automated Testing: All changes undergo automated testing to catch integration issues early.
1. Code Quality Checks: Automated tools check for code quality, ensuring that the trunk remains clean and maintainable.

### Release Process

1. No Separate Release Branch: Since there is no separate release branch, releases are made directly from the trunk.
1. Tagging: When a stable version is ready for deployment, the trunk is tagged with a version number.
1. Deployment: The tagged version of the trunk is deployed directly to the production environment.

### Hotfixes

1. Immediate Fixes on Trunk: In case of a critical issue in production, a hotfix can be made directly on the trunk.
1. Tagging After Fix: After the hotfix is applied and verified, a new tag is created, and the updated version is deployed.

### Best Practices

1. Commit Frequently: Avoid large, monolithic commits. Commit and push your changes regularly to the trunk.
1. Test Thoroughly: Ensure all relevant tests pass locally before committing to the trunk.
1. Rebase, Don’t Merge: For feature branches, use rebasing to keep history linear and avoid unnecessary merge commits.
1. Code Reviews: All changes must go through a peer review process before being merged into the trunk to maintain code quality.
