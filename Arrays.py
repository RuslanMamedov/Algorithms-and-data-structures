# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:12:06 2018

@author: Mamedov

Algorithms and data structures: Arrays
"""

'''Arrays - consequitive(contiguous) memory allocations. Arrays in python are called lists []. Unlike in java, these arrays are mutable objects and can store various data types
Tuples() are immutable lists. Can be used as keys in dictionary.
Arrays are base for many other data structures 
Arrays are good when searching by index (storing data in order) - unlike dictionaries(unordered) or linked lists(slow) -  or when a size is defined
built-in function for sorting an array is based on quick sort and have n*log(n) running time
use binomial search for ordered arrays'''

#1. Largest subarray sum problem
#O(n) - running through the array once
#the idea is to create to sum variables: running_sum vs. max sum, and then start adding array values consequitively
#if  running sum > max sum: update the max_sum
#if running sum <max sum: If it's negatve then reset it to 0, if it's positive - keep going

a = [-1,-2,3,4,5,-8]
b = [0,0,0,0]
c = [1,2,3,4,5]
d = [111]
e = [1,2,4,5,6]

def Max_Sum(arr):
    curr_sum = 0
    max_sum = 0
    if arr is None or len(arr) == 0:
        raise Exception ('The array is empty')
    for i in arr:
        curr_sum = curr_sum + i
        if curr_sum> max_sum:
            max_sum = curr_sum
        if curr_sum<0 and curr_sum < max_sum:
            curr_sum = 0
    return max_sum
    
print ('#1. Largest subarrays sums:\na ', Max_Sum(a),'\nb:', Max_Sum(b), '\nc:', Max_Sum(c), '\nd:',Max_Sum(d))
    
        
#2. Find missing value in a list of 1...n integers
'''Subtract the sum of all elemnts from the sum of arithmetic progression from 1 to n. O(n) running time.
Formulas for sum of arithmetic progression:
general one: (max(arr)+min(arr))*len(arr)/2 (the sum is the same for each consequent pair; we divide it by 2 and multiply by the number of elements)
special case for 1..n array: (max(arr)+1)*max(arr)/2
Note that in programming we sometimes go by the index n (starts from 0),
that is the sum is = (n+1)*(n+2)/2 - where n is number of elements
'''

def MissingValue (arr):
    if arr is None or len(arr) == 0:
        raise Exception ('The array is empty')
    arith_sum = (max(arr)+min(arr))*(len(arr)+1)/2 #len(arr)+1 - number of elements with missing values
    actual_sum = 0
    for i in arr:
        actual_sum+=i
    return (arith_sum - actual_sum)
print('\n\n#2. ') 
print ("Missing value:",MissingValue(e))

#3-4. Given an unsorted array of integers, find a subarray which adds to a given number. 
#If there are more than one subarrays with sum as the given number, print any of them.
#2 pointers, collecting sum of elements between them; O(2n)

a = [1, 4, 20, 3, 10, 5]

def SubarraySum (arr, n):
    if arr is None or len(arr) == 0:
        raise Exception ('The array is empty')
    start=0
    finish=0
    sum = arr[start]
    while finish<len(arr):
        if sum<n:
            finish+=1
            sum+=arr[finish]
        if sum==n:
            print('Sum found between indexes ',start,'and ',finish)
            break
        if sum>n:
            sum-=arr[start]
            start+=1
    return False
    
print('\n\n#3-4. ') 
print(SubarraySum(a,33))

#5.Write a program to sort an array of 0's,1's and 2's in ascending order.
'''Solve internally - use counters instead of swabbing. O(2n)'''
a=[0,0,0,1,1,1,2,2,0,1,0]
b=[0,0]

def SortArray (arr):
    if arr is None or len(arr) == 0:
        raise Exception ('The array is empty')
    zeros=0
    ones=0
    twos = 0
    for i in arr:
        if i==0:
            zeros+=1
        if i==1:
            ones+=1
        if i==2:
            twos+=1
        if i<0 or i>2:
            raise ValueError('Array elements should be 0, 1 or 2')
    j=0
    while zeros>0:
        arr[j]=0
        zeros-=1
        j+=1
    while ones>0:
        arr[j]=1
        ones-=1
        j+=1
    while twos>0:
        arr[j]=2
        twos-=1
        j+=1
    return arr
print('\n\n#5. ') 
print (SortArray (a), '\n\n\n')

#6. Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
#O(2n)
a = [-7, 1, 5, 2, -4, 3, 0]
def Equillibrium(arr):
    if len(arr)==0 or len(arr)==1 or arr is None:
        return -1
    total_sum=0
    for i in arr:
        total_sum+=i
    pointer = 0
    sum=0
    while pointer+1<len(arr):
        sum+=arr[pointer]
        if sum*2+arr[pointer+1]==total_sum:
            return pointer+1
        else:
            pointer+=1
    return -1
    
print('\n\n#6. ') 
print (Equillibrium(a), '\n\n\n')

            
        
    
    
        
                                     
#7.Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
#wouldn't need 2 pointers, just store max value in a variable
#O(n)

a=[16, 17, 4, 3, 5, 2]
def ArrayLeaders (arr):
    if arr is None or len(arr) == 0:
        raise Exception ('The array is empty')
    i = len(arr)-1
    maximum = arr[i]-1
    while i>=0:
        if arr[i]>maximum:
            print (arr[i])
        maximum = max(maximum,arr[i])
        i-=1
print('#7. ')        
ArrayLeaders(a)

#8. Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that ll array elements are distinct.
#O(n*logn) - quick sort 
def K_smallest(arr,k):
     arr_sorted=arr.sort()
     return arr[k-1]
print('\n\n#8. ')
print (K_smallest([7, 10, 4, 3, 20, 15],3))

#9. Given a 2D array, print it in spiral form. 
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def SpiralForm(arr):
    if arr is None or len(arr) == 0:
        raise Exception ('The array is empty')
    if arr is None:
        return Null
    for i in range (0,len(arr)):
        for j in range (0, len(arr[0])):
            print (arr[i][j],end =" ")
print('\n\n#9. ') 
SpiralForm(a)

#10. Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first.
#will have to use hash map.

        
    

    

