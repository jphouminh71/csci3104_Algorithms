#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:59:46 2019

@author: Jonathan Phouminh
ID: 106054641
PS3b
Question 1a
collaborted with: Zachary Chommalla
"""

'''
    Function takes in list and k, k is the amount of miles the robot can travel before
    needing gas
    
'''
def irobot(k,list):
    initialK = k  # add this after every time it stops
    solution_set = []  # just printing out the solution not returning anything
    size = len(list)-1
    for i in range(size): 
        if list[i+1] > k: 
            solution_set.append(list[i])
            k+=initialK
    for i in range(len(solution_set)):
        print(solution_set[i])
def main():
    # test cases to check
    list1 = [0,20,37,54,70,90]  # expecting, 37 70
    list2 = [0,18,21,24,37,56,66]  # expecting, 18 37 56
    list3 = [0,10, 15,18]  # expect nothing to be in the set
    k1 = 40
    k2 = 20
    k3 = 20
    irobot(k1,list1)
    print("----")
    irobot(k2,list2)
    print("----")
    irobot(k3,list3)
main()
