#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/30-linked-list
import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        if head == None: head = Node(data)        
        else:
            temp = head
            while True:
                if temp.next == None:
                    temp.next = Node(data)
                    break
                else: temp = temp.next

        return head

mylist= Solution()
T=int(input())
head=None

for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)  

mylist.display(head);