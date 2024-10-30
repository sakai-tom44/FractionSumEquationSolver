# Fraction Sum Equation Solver

## 概要 (Overview)

### JP
このプログラムは、方程式 1/a + 1/b + 1/c + ... = 1 を満たす分数の組み合わせを探索します。  
項数 `n` と分母の上限 `limit` を指定し、条件に合うすべての解を見つけてファイルに出力します。
### EN
This program searches for all combinations of fractions that satisfy the equation 1/a + 1/b + 1/c + ... = 1.  
It finds solutions by specifying the number of terms `n` and the upper limit of denominators, `limit`, then outputs all valid solutions to a file.

## ファイル構成 (File Structure)

### JP
- `main.py` : メインプログラムのコード。探索アルゴリズムとファイル出力機能が含まれています。
- `solutions_<n>.txt` : プログラム実行後に生成されるテキストファイル。すべての解が保存されます。
### EN
- `main.py` : Main program code. Contains the search algorithm and file output functionality.
- `solutions_<n>.txt` : Text file generated after running the program, storing all solutions.

## 使用方法 (Usage)

### JP
1. `n` に項数（分数の数）、`limit` に分母の最大値を設定します。
2. プログラムを実行すると、各解がコンソールに表示され、全ての解が `solutions_<n>.txt` に書き出されます。
3. `solutions_<n>.txt` ファイルには、それぞれの解が1行にカンマ区切りで記述されます。

### EN
1. Set the number of terms `n` (number of fractions) and the maximum denominator `limit`.
2. Run the program. Each solution is printed to the console, and all solutions are written to `solutions_<n>.txt`.
3. The `solutions_<n>.txt` file stores each solution on a new line, separated by commas.

### 実行例 (Example Execution)

```python
n = 3  # 項数 (Number of terms)
limit = 10000000  # 分母の上限 (Upper limit for denominators)
solutions = find_solutions(n, limit)
