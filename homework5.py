
def get_number():
    for i in range(30):
        if i%2!=0:
            yield i
numbers = get_number()
first = None
fifth = None
last = None
count = 0
for number in numbers:
    count += 1
    if first is None:
        first = number
    if count == 5:
        fifth = number
    last = number
print("Первое нечетное число:", first)
print("Пятое нечетное число:", fifth)
print("Последнее нечетное число:", last)

