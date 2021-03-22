def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))


######################
#   A           B    #
#   192         162  #
#   162         30   #
#   30          12   #
#   12          6    #
######################