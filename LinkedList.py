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
        self.random = None #random pointer
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

#3.Clone a linked list with a random pointer.
node6.next = None
def Clone (head):
    p=head
    if head==None: #empty linked list
        return False
    while p!=None: #clonning the nodes
        p.random = Node(p.data+'2')
        p = p.next
    p = head    
    while p.next!=None: #linking the nodes
        p.random.next = p.next.random
        p = p.next
    p.random.next = None #taking care of the last node
    p = head
    head2 = p.random
    new_list = head2
    while p!=None: #unlinking 2 lists
        p.random = None
        p = p.next
    while head2 !=None:
        print (head2.data)
        head2 = head2.next
    return new_list
print ('#3',Clone(node1)) #O(3n)

#4. Write code to remove duplicates from an unsorted linked list. Follow up: How would you solve it if temporary buffer is not allowed?
def RemoveDups(head):
    if head==None: #empty linked list
        return False
    d = {}
    p = head
    d [p.data]=1
    while p.next!=None:
        if p.next.data in d:
            if p.next.next==None:
                p.next = None
            else:
                p.next = p.next.next
        else:
            d [p.next.data]=1
            p = p.next
    p=head
    while p!= None:
        print (p.data)
        p=p.next
    print(d)
    return head
print ('#4',RemoveDups(node1))       

#5. Implement an algorithm to find the kth to the last element of a singly linked list
def Kth(head, k): #O(2n)
    if head==None: #empty linked list
        return False
    p=head
    counter = 0
    while p!=None:
        counter+=1
        p=p.next
    counter = counter - k
    if counter<=0:
        return False
    p=head
    while counter>0:
        p = p.next
        counter-=1
    p=head
    while p!= None:
        print (p.data)
        p=p.next
    return head
print('5',Kth(node1,2))
