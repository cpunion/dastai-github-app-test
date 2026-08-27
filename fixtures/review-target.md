# Review target

Version: 2

This file is intentionally small. Change one or two lines in a test pull
request, describe the intended result in the PR body, and ask `@dastai-local`
to review the change.

Expected invariant: a published configuration must include an owner, a bounded
timeout, and an explicit failure policy.

The candidate configuration for this smoke test is in
[`candidate-config.yaml`](candidate-config.yaml). A reviewer should compare it
against the invariant above.
