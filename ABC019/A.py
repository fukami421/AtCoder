p = list(map(int, input().split()))
p_sort = sorted(p, reverse=False)
print(p_sort[1])

# 別解
a = sorted(list(map(int,input().split())))
print(a[1])

a = list(map(int, input().split()))
a.sort(reverse=True)
print(a[1])

'''
リスト型のメソッドsort(): 元のリストをソート
組み込み関数sorted(): ソートした新たなリストを生成
'''