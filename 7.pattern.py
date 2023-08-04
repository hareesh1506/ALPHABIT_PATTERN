# inc = 1
# char = 65  # ASCII of 'A'
# for x in range(5, 0, -1):
#     for y in range(x, 0,-1):
#         print(" ", end="")
#     print(chr(char) * inc, end="")
#     char += 2
#     inc += 2
#     print()

# code
#      A
#     CCC
#    EEEEE
#   GGGGGGG
#  IIIIIIIII


# code
inc = 1
for x in range(5, 0, -1):
    for y in range(x, 0, -1):
        print(" ", end="")
    for z in range(1, inc + 1):
        print(chr(z + 64), end="")
    inc += 2;
    print()


 #
 #     A
 #    ABC
 #   ABCDE
 #  ABCDEFG
 # ABCDEFGHI
