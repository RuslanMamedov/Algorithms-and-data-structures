# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:10:12 2018

@author: Mamedov
"""
#Linked list    is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node.
#doesn't have to be contiguos in memory;
#mutable, can change length, no indexing only move in 1 direction (for sigly linked one)
#1. Write an algorithm to determine if a linkedlist is a palindrome
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
node1 = Node('a') 
node2 = Node('b') 
node3 = Node('c')
node4 = Node('c') 
node5 = Node('b') 
node6 = Node('a') 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

class Stack: #creates stack using python list

    #Constructor creates a list
    def __init__(self):
        self.stack = list()

    #Adding elements to stack
    def push(self,data):
        #Checking to avoid duplicate entries
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    #Removing last element from the stack
    def pop(self):
        if len(self.stack)<=0:
            return ("Stack Empty!")
        return self.stack.pop()

def Reverse(head):
    s=head #slow pointer
    if s==None: #empty linked list
        return False
    if s.next==None: #1 element in linked list
        return True
    f=head.next #fast pointer
    st=Stack()
    while f!=None and f.next!=None:
        st.push(s.data)
        s=s.next
        f=f.next.next
    if f!=None: #for even length will need to include the element at slow pointer to the stack
        st.push(s.data)
    s = s.next
    while s!=None:
        if s.data!=st.pop():
            return False
        s=s.next
    return True
print ('#1.',Reverse(node1))

#2. Write an algorithm to determine if a linkedlist is circular. FOLLOW UP: Determine where the circle meets. 
node6.next = node3
def Circular(head):
    if head==None: #empty linked list
        return False
    s=head #slow pointer
    if s==None: #empty linked list
        return False 
    f=head #fast pointer
    while f.next.next!=None:
        f=f.next.next
        s=s.next
        if f==s:
            s=head
            while f!=s:
                f=f.next
                s=s.next            
            return s.data
    return False
print ('#2.',Circular(node1))
    
#6. Reverse a linked list