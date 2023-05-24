print("The Fibonacci Sequence:")
p ="0"
while int(p)<3:
    p=input("Please enter a number,( at least 3")

q = 0
while q <= 0:
    q = int(input("Please enter number of terms to generate (should be a positive integer): "))

print("\n", q, "numbers in the sequence starting from term ", p, ":")

# convert p and q to integers
p, q = int(p), int(q)

# initialise term counters to zero
p_counter, q_counter = 2, 0

#initialise the first two terms in the sequence
n1, n2 = 0, 1

while q_counter < q:
    nth = n1 + n2
    n1, n2 = n2, nth
    p_counter += 1
    if p_counter >= p:
        q_counter += 1
        if q_counter < q:
            print(nth, end = ", ")
        else:
            print(nth)
