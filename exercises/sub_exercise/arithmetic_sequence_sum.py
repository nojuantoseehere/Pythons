def get_variable():
    a = int(input("Enter Start Value: "))
    d = int(input("Enter Common difference: "))
    n = int(input("Enter number of iteration: "))
    return a,d, n
def arithmetic_sequencer(a,d,n):
    sum = 0
    for i in range(n):
        sum += a
        print(a)
        a += d
    print(f"Result: {sum}")

print("=== Arithmetic Sequence(Sum) ===")
print()
a, d , n = get_variable()
arithmetic_sequencer(a,d,n)