def count(start, end):
    prime = []
    num = start + 1
    prime_ = False
    while num != end:
        for i in range(2, num):

            # num = start
            if num % i == 0:
                prime_ = True
                break
        if prime_:
            prime.append(num)
            num = num +1
        else:
            prime_ = False
            num = num+1


        # else:
        #     pass

        # num = num +1
    return len(prime)

print(count(10, 100))