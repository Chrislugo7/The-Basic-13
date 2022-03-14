# The “Basic 13”
# The foundation “Basic 13” algorithm challenges.


# Print 1-255
# Print all the integers from 1 to 255.
# for i in range(1,256):
#     print(i)



# Print Sum 0-255
# Print integers from 0 to 255, and with each integer print the sum so far.
# sum = 0
# for i in range(0,255):
#     sum += i
#     print(sum)


# Find and Print Max
# Given an array, find and print its largest element.
# arr = [25, 11, 7, 75, 56];     
# max = arr[0];    
# for i in range(0, len(arr)):    
#     if(arr[i] > max):    
#         max = arr[i];    
# print("Largest element present in given array: " + str(max));  


# Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).
# for i in range(0,256):
#     if i % 2 == 1:
#         print(i)


# Greater Than Y
# Given an array and a value Y, count and print the number of array values greater than Y.
# def greater_than_y(arr,y):
#     count = 0
#     for i in range(0, len(arr)):
#         if arr[i] > y:
#             count += 1
#     print(count)

# greater_than_y([7,16,32,2,79,40,11,12,44,56],15)


# Max, Min, Average
# Given an array, print the max, min and average values for that array.
# def max_min_avg(arr):
#     max = 0
#     min = 0
#     # min = arr[0]
#     avg = 0
#     for i in range(0,len(arr)):
#         if arr[i] > max:
#             max = arr[i]
#         if arr[i] < min:
#             min = arr[i]
#         avg += arr[i]
#     avg = avg / len(arr)
#     return max, min, avg
# print(max_min_avg([15,7,8,2,95,6,3]))



# Swap String For Array Negative Values
# Replace any negative array values with 'Dojo'.
# def swaping_dojos(arr):
#     for i in range(0, len(arr)):
#         if arr[i] < 0:
#             arr[i] = "Dojo"
#         print(arr[i])
# swaping_dojos([15,7,-8,2,-95,6,3])




# Print Odds 1-255
# Print all odd integers from 1 to 255.
# for i in range(1,256):
#     if i % 2 == 1:
#         print(i)


# Iterate and Print Array
# Iterate through a given array, printing each value.
# def iterate_arr(arr):
#     for i in range(0, len(arr)):
#         print(arr[i])
# iterate_arr([5,7,12,34,5,2,7])


# Get and Print Average
# Analyze an array’s values and print the average.
# def avg(arr):
#     avg = 0
#     for i in range(0, len(arr)):
#         avg += arr[i]
#     avg = avg / len(arr)
#     return avg
# print(avg([7,16,27,2,4,6,8,10,112,13]))



# Square the Values
# Square each value in a given array, returning that same array with changed values.
# def squared(arr):
#     for i in range(0, len(arr)): 
#         arr[i] *= arr[i]
#     return arr
# print(squared([12,4,6,7,8,2,3,6,1]))


# Zero Out Negative Numbers
# Return the given array, after setting any negative values to zero.
# def zeros(arr):
#     for i in range(0, len(arr)):
#         if arr[i] < 0:
#             arr[i] = 0
#     return arr
# print(zeros([15,7,-8,2,-95,6,3]))


# Shift Array Values
# Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the
# end


# def shift_forward(arr):
#     for i in range(0, len(arr) - 1):
#             arr[i] = arr[i + 1]
#     arr[len(arr) - 1] = 0
#     return arr
# print(shift_forward([10,12,14,6,3]))




