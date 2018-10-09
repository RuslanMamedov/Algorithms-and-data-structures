# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:36:11 2018

@author: Mamedov
"""

#String - array of characters. Immutable, need to convert to list (array) first
#use dictionaries for string look-ups

#1. Longest palindromic substring

def PalSubstring(s):
    s=list(s)
    if s is None or len(s)==0:
        raise Exception ('The string is empty')
    if len(s)==1:
        return s
    max_start, max_finish = 0,0
    for mid in range (0,len(s)): #looking for even length palindromes
        start,finish = mid, mid+1
        while start>=0 and finish<len(s):
            if s[start] == s[finish]:
                start-=1
                finish+=1
                if start<0 or finish>=len(s):
                    if finish-start-2>max_finish-max_start:
                        max_finish=finish-1
                        max_start = start+1
            else:
                if finish-start-2>max_finish-max_start:
                    max_finish=finish
                    max_start = start
                else:
                    start = -1 #to break out of the loop
    for mid in range (0,len(s)): #looking for odd length palindromes
        start,finish = mid-1, mid+1
        while start>=0 and finish<len(s):
            if s[start] == s[finish]:
                start-=1
                finish+=1
                if start<0 or finish>=len(s):
                    if finish-start-2>max_finish-max_start:
                        max_finish=finish-1
                        max_start = start+1
            else:
                if finish-start-2>max_finish-max_start:
                    max_finish=finish
                    max_start = start
                else:
                    start = -1 #to break out of the loop
    if max_start!=max_finish:
        return s[max_start:max_finish+1]
    else:
        return None
print ('#1.',PalSubstring('m'))     

#2.recursively remove adjacent duplicate characters from string. 
#The output string should not have any adjacent duplicates.          

def RemoveDup(s):
    if s is None or len(s)==0:
        return None   
    if len(s)==1:
        return s
    s = list(s)
    new_s=''
    for i in range (0,len(s)-1): #excluding the last character
        if s[i]!=s[i+1]: #adding noncontiguos characters to new string
            if i == len(s)-2:
                new_s+=s[i]+s[i+1] #including the last character when it's different from the previous one
            else:
                new_s+=s[i]
        else: #skipping contiguous characters
            while i<len(s)-1 and s[i]==s[i+1]:
                i+=1
                if i == len(s)-2:
                    if s[i]==s[i+1]:
                        i+=1 #when the last character needs to be excluded
                    else:
                        new_s+=s[i+1]
    '''if len (new_s)<len(s):
        return RemoveDup(new_s)
    else:'''
    return new_s
            
print ('#2.', RemoveDup('aaaabbb333334'))
    
#3. Given two strings, the task is to find if a string ('a') can be obtained by rotating another string ('b') by two places.
#O(n)
def Rotation (s1, s2):
    s1, s2 = list (s1), list (s2)
    if len (s1)!=len(s2):
        return False
    if s1 is None or s2 is None or len(s1) == 0:
        raise Exception ('The string is empty')
    if len(s1)==1:
        if s1[0]==s2[0]:
            return True
        else:
            return False
    if len(s1)==2:
        if s1[0]==s2[0] and s1[1]==s2[1]:
            return True
    #clockwise rotations:
    for i in range (2, len(s2)):
        if s1[i-2]==s2[i]:
            if i == len(s2)-1:
                for j in range (0,2): #checking the rotated characters
                    if s1[len(s1)-2+j]==s2[j]:
                        if j==1:
                            return True
                    else:
                        j=2 #getting out of the loop
        else:
            i=len(s2) #getting out of the loop
    #counter-clockwise rotations:      
    for i in range (2, len(s1)):
        if s1[i]==s2[i-2]:
            if i == len(s1)-1:
                for j in range (0,2): #checking the rotated characters
                    if s2[len(s1)-2+j]==s1[j]:
                        if j==1:
                            return True
                    else:
                        j=2 #getting out of the loop
        else:
            i=len(s2) #getting out of the loop
    return False

print ('#3.',Rotation('amazon','azonam'))

#4.Given a string in roman no format (s)  your task is to convert it to integer .
# I=1, X=10, L=50, C=100, M=1000
#the algorithm is to convert each of the pairsa above to dictionary key-value pairs
#then start adding the keys 
#unless you encounter a key of higher value - then you subtract previous sum from this number

def Roman (s):
    s=list(s)
    d={'I':1, 'X':10, 'L':50, 'C':100, 'M':1000}
    sum=0
    for i in range (0, len(s)):
        if i == len(s)-1: #taking care of the last element
            sum+=d[s[i]] 
        else:
            if int(d[s[i]])>=int(d[s[i+1]]): #when following # is greater or equal the following one - simple addition
                sum+=d[s[i]]
            else: #otherwise subtracting the numbers
                for j in range (i,-1,-1):
                    if int(d[s[j]])==int(d[s[i]]):
                        if j!=i:
                            sum-=2*d[s[j]]
                        else:
                            sum-=d[s[j]]#first number in the series to subtract
                            
                    else:
                        j=-1 #getting out of the loop
    return sum
print ('#4.',Roman ('XIX'))
            
#7.Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.
def atoi (s):
    if s is None:
        raise Exception ('Empty string!')
    s=list(s)
    integer,j=0,1
    for i in range (len(s)-1,-1,-1):
        integer+=int(s[i])*j
        j*=10
    return integer
print ('#7.', atoi('123400000000'))

#8. Your task  is to implement the function strstr. The function takes two strings as arguments(s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting  the first occurrence of the string x .
def strstr(s,x):
    if s is None or len(s) == 0 or len(x) == 0 or len(x)>len(s):
        return None
    s=list(s)
    x=list(x)
    for i in range (0,len(s)-len(x)):
        if s[i]==x[0]:
            j=i
            while s[i]==x[i-j]:
                if i-j==len(x)-1:
                    return j
                else:
                    i+=1
                
    return None
    
print ('#8.', strstr('abcdefg', 'de'))
       
#9. Given a array of Nstrings, find the longest common prefix among all strings present in the array.
def Prefix(arr): 
    for i in range (0,len(arr)):
        if len(arr[i])==0 or arr[i] is None:
            raise Exception ('Empty string!')
        arr[i]=arr[i].lower()
        arr[i]=list(arr[i])
    prefix = ''
    j=0
    while j>=0: #to keep the loop running until it is broken within
        for i in range (0,len(arr)):
            if i == 0:
                c= arr[i][j]
            if j>=len(arr[i]):
                return prefix # to check for the length of the word
            if arr[i][j]==c and i==len(arr)-1:
                prefix=prefix+arr[i][j]
            if arr[i][j]!=c:
                if prefix == '':
                    return False
                else:
                    return prefix
        j+=1
arr=['apple','ape', 'April']
print ('#9.',Prefix(arr))
        
        
#11. Remove white spaces in the string
s='I love you'

def RemoveSpaces (s):
    ns=''
    if s is None or len(s) == 0:
        raise Exception ('The string is empty')
    for i in range (0, len(s)):
        if s[i]!=" ":
            ns+=s[i]
    return ns

print ('#11.',RemoveSpaces(s))

#12. Reverse a string 'in-line'
#O(n/2)

def ReverseString (st):
    if st is None or len(st) == 0:
        raise Exception ('The string is empty.')
    st = list(st)
    s=0
    f=len(st)-1
    temp=''
    while f>s:
        temp=st[f]
        st[f] = st[s]
        st[s] = temp
        f-=1
        s+=1
    st=''.join(st)
    return st
    
print('#12.',ReverseString (ReverseString (s)))

#13. Is this a palyndrome?
#O(n/2) same as previous, but instead of swabbing - compare

def Palindrome(s):
    if s is None or len(s)==0:
        raise Exception ("The string is empty.")
    s = list(s)
    start, finish = 0, len(s)-1
    while start<finish:
        if s[start]!=s[finish]:
            return ('This is not a palindrome!')
        else:
            start+=1
            finish-=1
    return ('This is a palindrome')
    
print ('#13.',Palindrome ('Madam'))
    
#14. Is it an anagram (e.g. 'cat' and 'act')
s1, s2 = 'cata', 'acta'
def Anagram (s1, s2):
    if len(s1)!=len(s2):
        return ('This is not an anagram!')
    if len(s1)==0 or s1 is None or s2 is None:
        return ('Empty string!')
    d={}
    s1, s2 = list(s1), list(s2)
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s2:
        if i in d:
            d[i]-=1
        else:
            return (d,'This is not an anagram!')
    for i in d.values():
        if i!=0:
            return (d,'This is not an anagram!')
    return (d,'This is anagram!')
print ('#14.',Anagram (s1, s2))

#15. Count contigious characters, e.g in: aaabbbcccd, out: a3b3c3d1
#O(n)
s='aabcccdeee'
def CountContig (s):
    if s is None or len(s)==0:
        raise Exception ('Empty string!')
    st = list(s) 
    p = st[0] #pointer
    c = 1 #counter
    cs='' #compressed string
    for i in range (1, len(st)):
        if st[i]==p:
            c+=1
        else:
            cs+=p+str(c)
            if len(cs)>len(s):
                return s
            p=st[i]
            c=1
            
    cs+=p+str(c) #to take care of the very last character
    if len(cs)>len(s):
        return s
    else:
        return cs
 
print ('#15.',CountContig (s) )

#16 Identify all unique characters in the string
s='abc'
def Unique (s):
    if len(s)==0 or s is None:
        raise Exception ('Empty string!')
    s = list(s)
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d.keys()

print (Unique(s))



    
    

            
            
        
        
    
        
    

    

    

