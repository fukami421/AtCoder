# 初期化
ans_dict = {}

# 例
_dict = {"apple":1, "orange":2, "banana":3}
# 格納(数値はint型にしてから)
for i, a_s in enumerate(A_S):
  a, s = a_s.split(':')
    ans_dict[int(a)] = s

# 長さ
len(ans_dict)

# keyでsort
sortedList = sorted(ans_dict.items())
sortedDict = dict(sortedList)

# for文
ans = ""
for value in a.values():
  ans += value
print(ans)


# 要素削除
mydict.pop("orange") # key指定

# clear
mydict.clear()

# 既存の辞書のkeyのリストを取り出す
dic = {"A": "cat", "B": "dog"}
print(dic.keys()) # valueの場合はvalues()t
# 出力
# ["A", "B"]