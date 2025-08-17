# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generater(limit):
    for i in range(2, limit + 1, 2):
        yield i # puts the function along with its state in memory, (like how much work is being performed internally)


for num in even_generater(10):
    print(num)

print(list(even_generater(10)))  # This will print: [2, 4, 6, 8, 10]

###############################################################