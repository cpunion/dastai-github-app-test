# DastAI GitHub App testbed

This public repository is an isolated, disposable fixture for testing the
DastAI GitHub App end to end. It contains no production code or secrets.

## Current connection status

- `DastAI Local` is installed on this repository and the Local runtime has an
  exact repository-ID binding.
- A real draft `pull_request.opened` webhook has returned `200` without creating
  a Task, as intended.
- Visible GitHub replies are connected. In [PR #1](https://github.com/cpunion/dastai-github-app-test/pull/1),
  `ready_for_review` produced a `COMMENT` review and an authorized
  `@dastai-local` mention produced a conversation reply, both authored by the
  Local App bot.
- Those two webhook deliveries reused one PR-scoped Dast Task/Agent and ran as
  two independent occurrences (`run-1` and `run-2`). Both durable provider
  delivery intents reached `sent` and their Task output states reached
  `released`.
- The installation token is narrowed to this repository for each operation.
  Automatic review can only create a `COMMENT` review; it cannot approve or
  request changes.

## What to test

Use pull requests in this repository to verify these observable behaviors:

1. Opening a draft PR does not start automatic review.
2. Marking the PR ready for review routes the event to one stable Dast Task and
   Agent.
3. Commenting `@dastai-local review this PR` queues another run on the same
   PR-scoped Agent without merging the two webhook occurrences.
4. A real DastAI App reply appears in the same GitHub thread and is visibly
   authored by `dastai-local[bot]`.
5. Redelivering the same webhook does not create another Task or duplicate a
   reply.

The fixture in [`fixtures/review-target.md`](fixtures/review-target.md) is meant
to be changed on short-lived branches. Keep test changes harmless and never add
credentials, personal data, or production artifacts.

## Evidence boundary

A `200` webhook delivery proves only that GitHub reached the configured DastAI
ingress. It does not by itself prove that an Agent ran or that a reply was sent.
For a complete test, inspect both the Dast Task/Agent trace and the GitHub
comment author/body.
