# README.md includes an overview and usage instructions for the program, written in both Japanese and English.
# README.md にはプログラムの概要や使い方が含まれており、日本語と英語で内容が記述されています。

from fractions import Fraction

# 探索を行う関数を定義
def find_solutions(n, limit):
    solutions = []
    
    # 再帰関数で探索を行う
    def search(current, partial_sum, last):
        # 部分和が1なら解とみなす
        if partial_sum == Fraction(1) and len(current) == n:
            solutions.append(tuple(current))
            print(tuple(current))
            return
        
        # 分数の和が1を超えた場合や、項数が超えた場合は終了
        if partial_sum >= Fraction(1) or len(current) >= n:
            return
        
        # 残りの項数から次の項の最大値を動的に設定
        remaining_terms = n - len(current)
        max_denominator = limit
        
        if partial_sum > 0:
            # 残りの項で均等に分配するための最大値を調整
            min_required_sum = Fraction(1) - partial_sum
            max_denominator = min(max_denominator, int(remaining_terms / min_required_sum) + 1)
        else:
            # はじめの項の最大値はnと一致する
            max_denominator = n

        # 次の値を試す
        # print("max: ", max_denominator)
        for next_num in range(last - 1, max_denominator + 1):
            if next_num > 1:
                search(current + [next_num], partial_sum + Fraction(1, next_num), next_num + 1)
    
    # 探索を開始
    search([], Fraction(0), 2)  # 最初の分母は2以上でスタート
    
    return solutions

n = 3  # 項数
limit = 10000000  # 探索限界
solutions = find_solutions(n, limit)

# 結果をテキストファイルに出力する関数を定義
def write_solutions_to_file(solutions, filename):
    with open(F"{filename}_{n}.txt", 'w') as f:
        for sol in solutions:
            f.write(str(tuple(sol))+'\n')

# 結果を表示
print("---------------------------------------------------")
# for sol in solutions:
#     print(sol)
print("len: ", len(solutions))

# 結果をテキストファイルに出力
write_solutions_to_file(solutions, 'solutions')