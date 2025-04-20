def kaprekar_steps(n):
    steps = []
    while True:
        n = str(n).zfill(4)  # Ensure 4-digit format
        asc = int(''.join(sorted(n)))
        desc = int(''.join(sorted(n, reverse=True)))
        res = desc - asc
        steps.append(res)
        if res == 6174 or res == 0:
            break
        n = res
    return steps

# Input
a = input("Enter a 4-digit number (at least two different digits): ")

# Validate input
if len(set(a)) == 1:
    print("All digits are the same. Kaprekar's routine won't work.")
else:
    results = kaprekar_steps(a)

    # Print all iterations
    print("\nIteration results:")
    prev = a
    for i, val in enumerate(results):
        asc = int(''.join(sorted(str(prev).zfill(4))))
        desc = int(''.join(sorted(str(prev).zfill(4), reverse=True)))
        print(f"Step {i+1}: {desc:04d} - {asc:04d} = {val:04d}")
        prev = val

    
