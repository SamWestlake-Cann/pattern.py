
pat_width = 5 # set the pattern width to end at 5 so we print 5 stars

for i in range(1,10):
# setting i in range 1 - 10 so code will run 9 iterations
    if i <= pat_width:
        print('*' * i)
# print '*' and multiply by 1 until equal with pat_width
    else:
        print('*' *(2 * pat_width - i))
# print '*' and minus by 1 until back to 1


