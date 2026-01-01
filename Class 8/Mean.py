mean1 = 38
wrng_num = 36
crct_num = 56
tot_num = 40
# sum of 40 numbers
sum = mean1 * tot_num
print("Sum of 40 numbers is:", sum)
# sum after correcting the wrong number
sum2 = sum - (wrng_num - crct_num)
print("Sum after correcting the wrong number is:", sum2)
mean2 = sum2 / tot_num
print("New Mean is:", mean2)