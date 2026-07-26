import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Innovation and hallucination: six exact claims

    ![Evidence headline](https://raw.githubusercontent.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/main/reports/claim-by-claim/images/headline.svg)

    This tutorial explains the already-produced evidence. It does not ask
    Molab to rerun the formal reproduction.
    """)
    return


@app.cell
def _():
    results = [
        ("1", "Observation 3.2", "g(H)>0 → g(U)>0", "2,736,552", "VERIFIED"),
        ("2", "Theorem 3.3", "Pr[g(H)>0|X] ≥ 1-K/|U|", "3,662", "VERIFIED"),
        ("3", "Proposition 3.4", "calibration + p(U)>0 → g(U)>0", "56,105", "VERIFIED"),
        ("4", "Theorem 4.1", "strict-delta Markov bound", "4,508", "VERIFIED"),
        ("5", "Theorem 4.2", "g(U)/(K+1) high-confidence bound", "5,862", "VERIFIED"),
        ("6", "Proposition 4.3", "missing mass minus TV", "44,390", "VERIFIED"),
    ]
    return (results,)


@app.cell
def _(mo, results):
    mo.md(
        "| Claim | Source | Exact contract | Complete finite checks | Evidence verdict |\n"
        "|---:|---|---|---:|---|\n"
        + "\n".join("| " + " | ".join(row) + " |" for row in results)
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The one correction to remember

    Theorem 3.3 bounds a **posterior event probability**:

    \[
    \Pr[g(H)>0\mid X] \ge 1-\frac{K}{|U|}.
    \]

    It does not lower-bound the number \(g(H)\) by \(1-K/|U|\).
    Under Regular Facts, every unseen statement has the same factual
    probability \(q\), while K-sparsity gives \(|U|q\le K\).
    Any unseen point with positive model mass is therefore hallucinated
    with probability at least \(1-K/|U|\).
    """)
    return


@app.cell
def _(mo):
    k = mo.ui.slider(1, 20, value=3, label="K (illustrative only)")
    u = mo.ui.slider(21, 100, value=40, label="|U| (illustrative only)")
    return k, u


@app.cell
def _(k, mo, u):
    bound = 1 - k.value / u.value
    mo.md(
        f"""
        ## Bounded illustration—not formal evidence

        {k} {u}

        For these inputs, Theorem 3.3's event-probability lower bound is
        **{bound:.3f}**. The formal evidence uses exact arithmetic and committed
        proof certificates; this slider is only intuition.
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Why the controls matter

    Each verifier includes a control that removes a required assumption or
    strengthens a sharp constant. Every control fails for the predicted
    reason. That distinguishes the new checks from the historical verifier,
    which could pass with a zero bound or hand-assigned masses.

    See the [full illustrated report](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/blob/main/reports/claim-by-claim/report.md)
    and [raw evidence](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/main/.openresearch/artifacts).
    """)
    return


if __name__ == "__main__":
    app.run()
