# ===== ПЕРЕВОД lambda ↔ def =====
def func_one(a, b):
    return a + b

def func_two(fruit):
    return fruit['name']

len_word = lambda word: len(word) > 5

def alert(dialog):
    return dialog.dismiss()


print(func_one(2, 3))
print(func_two({'name': 'Kiwi', 'id': 7}))
print(len_word('banana'))
