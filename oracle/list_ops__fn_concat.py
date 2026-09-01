"""list-ops-fn-concat-conformance-oracle -- deterministic CONFORMANCE oracle for `list-ops` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 3 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PROVENANCE: the reference body comes from the Exercism reference solution for `list-ops` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=344e5b0c6787cc4a) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "list-ops"
CWE = "list-ops"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


def concat(lists: list) -> list:
    return [element for list in lists for element in list]

REFERENCE = concat
