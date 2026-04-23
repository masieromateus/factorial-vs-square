# Factorial vs Square

A Python script to find the real counterexample for the conjecture $n! \le n^2$.

## 💡 The Idea
In discrete mathematics, some statements seem true for the first few cases but fail as numbers grow. While $n! \le n^2$ holds for $n = 1, 2, 3$, it fails at $n = 4$.

This project explores the exact "rupture point" between 3 and 4 where the factorial growth permanently overtakes the quadratic growth by using a continuous approach.

## 🛠️ Tech
* **Python 3**
* **Math Library:** Specifically the `gamma()` function to calculate factorials for non-integer (decimal) numbers.

## 🧠 Challenges & Learning
* **Floating Point Precision:** Dealt with the classic binary precision issue (e.g., `3.0000000000000004`) by implementing formatted f-strings and `round()` to keep the logic consistent.
* **Dynamic Formatting:** Used nested f-strings `:.{nrange}f` to allow the output precision to scale according to the user's input.
* **Mathematical Logic:** Applied the Gamma function $\Gamma(n+1)$ to bridge the gap between discrete factorials and continuous functions.
