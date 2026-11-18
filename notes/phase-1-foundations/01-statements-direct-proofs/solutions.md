# Solutions: statements and direct proofs

Separate answer key. Attempt required problems first. Keep this file closed during unaided work.

## 1

(a) is a true proposition; (b) is an open sentence with free variable $x$; (c) is a true universally quantified proposition. Fixing $x$ or quantifying it over a stated domain turns (b) into a proposition.

**Check.** For example, $x=3$ makes the equation true and $x=0$ makes it false, showing why the unspecified variable matters.

## 2

Domain: integers. Hypothesis: $6\mid n$. Conclusion: $3\mid n$.

**Check.** The claim concerns any integer satisfying the hypothesis, including $0$ and negative multiples, not just positive examples.

## 3

$-8=2(-4)$; $-7=2(-4)+1$; $-12=3(-4)$. The witness in each case is $-4$.

**Check.** Substitution verifies all three equalities and the witness lies in $\mathbb Z$.

## 4

Let $a=2r$, $b=2s$ for integers $r,s$. Then $a+b=2(r+s)$, with integer witness $r+s$.

**Check.** Independent witnesses cover unequal inputs; closure of integer addition justifies integrality.

## 5

Let the even input be $a=2r$, $r\in\mathbb Z$, and let $b$ be any integer. Then $ab=2(rb)$, with integer witness $rb$.

**Check.** Neither positivity nor parity of $b$ is assumed, so the proof covers all allowed inputs.

## 6

For arbitrary $n\in\mathbb Z$, $4n+6=2(2n+3)$. The witness $2n+3$ is an integer.

**Check.** Expanding the factorization returns the original expression; it uses the definition of even directly.

## 7

For arbitrary $n\in\mathbb Z$, $6n+5=2(3n+2)+1$, with integer witness $3n+2$.

**Check.** At $n=-1$ the expression is $-1=2(-1)+1$, consistent with a general proof covering negative integers.

## 8

Three successful examples do not cover all nonnegative integers. At $n=41$,

$$
n^2+n+41=41^2+41+41=41(43)=1763.
$$

Both factors exceed $1$, so the value is composite, refuting the claim.

**Check.** $41$ is in the stated domain, and the factorization exhibits a positive divisor other than $1$ and $1763$.

## 9

Converse: if an integer is divisible by $4$, then it is divisible by $8$. It is false: $4$ is divisible by $4$, but no integer $k$ satisfies $4=8k$.

**Check.** The counterexample has a true hypothesis and false conclusion; $k=1/2$ is not an integer witness.

## 10

The shared witness forces $a=b$, though arbitrary odd inputs can differ. Write $a=2r+1$, $b=2s+1$ for independent integers $r,s$.

**Check.** Inputs $a=1$, $b=3$ can now use $r=0$, $s=1$, so the setup covers unequal cases.

## 11

The number of readings is $12n=3(4n)$. Since $4n$ is a nonnegative integer, it is the number of complete groups of $3$.

**Check.** Counting groups and multiplying by $3$ recovers $12n$; $n=0$ is included with zero groups.

## 12

Write $n=2k+1$ for an integer $k$. The new length is $n+2=2k+3=2(k+1)+1$, with integer witness $k+1$.

**Check.** The operation adds two cells, not one; a positive row length remains a positive integer.

## 13

Let $a=3r$, $b=3s$ with integers $r,s$. Then $2a-b=6r-3s=3(2r-s)$. The integer witness is $2r-s$.

**Check.** Integer closure under addition, multiplication, and negation justifies the witness even when it is negative.

## 14

Write $a=2r+1$, $b=2s+1$ for arbitrary integers $r,s$. Then

$$
ab=4rs+2r+2s+1=2(2rs+r+s)+1.
$$

The witness $2rs+r+s$ is an integer, proving oddness for all such $a,b$. The single pair $a=b=1$ does not cover other allowed pairs.

**Check.** Multiplying out verifies the identity; independent witnesses avoid an assumption that the inputs are equal.

## 15 — optional

Let $n=2k+1$. Then $n^2-1=4k(k+1)$. If $k=2r$, the product $k(k+1)=2[r(k+1)]$ is even. If $k=2r+1$, then $k+1=2(r+1)$ and $k(k+1)=2[k(r+1)]$ is even. Thus in either case $k(k+1)=2m$ for an integer $m$, so $n^2-1=8m$.

**Check.** The even/odd cases exhaust integer $k$, including negative values. The witness is integral and the final factor is $8$, not merely $4$.

## Exit-test solution

The domain is $\mathbb Z$. The hypothesis is that $n$ is odd; the conclusion is that $5n+2$ is odd. Let $n$ be an arbitrary odd integer, so $n=2k+1$ for some integer $k$. Then

$$
5n+2=5(2k+1)+2=10k+7=2(5k+3)+1.
$$

Since $5k+3\in\mathbb Z$, it witnesses the required oddness. Three numerical examples cover only three integers, whereas the claim covers every odd integer. The arbitrary-witness argument covers them all.

**Check.** Expansion returns $10k+7$. No positivity restriction was added, the witness is explicitly integral, and the proof never assumes the conclusion. A passing exit assessment must include both the general proof and the explanation about examples; timing and assistance must be recorded separately.
