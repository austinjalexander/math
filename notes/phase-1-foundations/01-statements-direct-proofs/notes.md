# Statements and direct proofs

Prerequisites: signed integers, substitution, and expansion. Use [the module overview](README.md) to check readiness and objectives.

## 1. State a proposition and its domain

A proposition is a statement with a definite truth value, even if we do not yet know that value. “$7$ is odd” is a proposition. “$x$ is odd” is an open sentence until the variable is specified or quantified over an appropriate domain.

The integers are $\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}$. The domain tells us which inputs a claim covers. “For every integer $n$” makes a universal claim. “There exists an integer $k$” makes an existence claim.

**Worked example.** Interpret “For every integer $n$, if $n$ is a multiple of $4$, then $n$ is even.” The domain is $\mathbb Z$, the hypothesis is “$n$ is a multiple of $4$,” and the conclusion is “$n$ is even.” In a direct proof, choose an arbitrary integer satisfying the hypothesis, rather than selecting one convenient value.

**Check.** An input such as $n=3$ does not refute the implication: its hypothesis is false. An implication fails when its hypothesis holds and its conclusion fails.

## 2. Definitions provide witnesses

An integer $n$ is **even** when there is an integer $k$ with $n=2k$. It is **odd** when there is an integer $k$ with $n=2k+1$. The integer $k$ is a witness to that representation; it need not be positive.

For integers $d,n$, with $d\ne0$ in this lesson, $d\mid n$ means that $n=dk$ for some integer $k$. We say $d$ divides $n$. Closure of the integers under addition and multiplication lets us construct new integer witnesses.

**Worked example.** Show that the sum of two odd integers is even. Let $a=2r+1$ and $b=2s+1$ for arbitrary integers $r,s$. Then

$$
a+b=2r+1+2s+1=2(r+s+1).
$$

Since $r+s+1\in\mathbb Z$, it witnesses that $a+b$ is even.

**Check.** Use independent witnesses $r,s$: they may be equal, but the two odd inputs need not be equal. For negative inputs, $-3+1=-2$ gives witness $-1$, consistent with the argument.

## 3. Build a direct proof

Begin with arbitrary allowed inputs. Assume the hypothesis, use definitions, transform the expression, and identify the required conclusion and witness. Do not assume what you are trying to prove.

**Worked example.** Prove: for every integer $n$, if $n$ is even, then $n^2+4$ is even. Let $n=2k$ for some integer $k$. Then

$$
n^2+4=4k^2+4=2(2k^2+2).
$$

The witness $2k^2+2$ is an integer, so the expression is even.

**Check.** Substitution verifies the algebra; integrality verifies the witness. The arbitrary $k$ covers all even integers, including zero and negative values. Trying $n=2$ alone would cover just one input.

## 4. Counterexamples and converses

A universal claim says every permitted input works. One permitted input with a true hypothesis and false conclusion disproves it. The converse of “if $P$, then $Q$” is “if $Q$, then $P$”; it needs its own argument.

**Worked example.** The claim “every multiple of $4$ is even” has converse “every even integer is a multiple of $4$.” The integer $6$ is even, since $6=2\cdot3$, but $6$ is not a multiple of $4$. The converse is false.

**Check.** A negative multiple such as $-8$ would confirm one case, not refute the universal converse. The counterexample must satisfy the hypothesis and fail the conclusion.

Finite example checks can help find a conjecture, detect a mistake, or discover a counterexample. They cannot prove an unrestricted claim about infinitely many integers. A finite domain can be proved by truly exhaustive case checking if every allowed case is covered and the checking argument is justified; that is a different situation.

## Common mistakes

- Leaving the domain unstated: an integer witness must actually lie in $\mathbb Z$.
- Writing “clearly even” without exhibiting a factor of $2$ and an integer witness.
- Giving several values instead of proving the statement for arbitrary inputs.
- Using the same witness for two independent inputs without justification.
- Treating a converse as automatic, or presenting a false-hypothesis case as a counterexample.
- Treating the number $0$ as neither even nor odd: $0=2\cdot0$ is even.

## Connections and sources

These skills support later induction/counting (**1c/1d**), rigorous limits (**4a**), groups (**5b**), and algorithm correctness (**6d**). They also help applied work: a derived formula needs its assumptions, and a simulation needs an honest statement of its scope.

Primary reference: [MIT 6.042J, Spring 2015](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/), open textbook sections on propositions and proofs. This lesson's wording, examples, exercises, and exit assessment are original. See [resources](../../../RESOURCES.md); no textbook page or exercise numbers are assigned yet.

## Exit test — 15 minutes, unaided

For every integer $n$, if $n$ is odd, then $5n+2$ is odd. Identify the domain, hypothesis, and conclusion. Prove the claim directly from the definition of odd, supply an explicit integer witness for the conclusion, and explain why three successful numerical examples would not prove the claim.

Use no notes, tutor, solutions, or computer. Pass only with a valid argument for arbitrary permitted $n$, a justified integer witness, and a correct explanation of why examples are insufficient. Record actual elapsed time and assistance; then supply your own dated 2–4 sentence reflection after grading.
