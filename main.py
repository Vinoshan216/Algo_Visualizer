import tkinter as tk
import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 


# def heap_sort(arr, length):
    

def insertion_sort(arr, length):

    #loops through array from second index to end
    for i in range(1,length):
        #variable for comparison index holding current element
        key = arr[i]
        #variable for previous index
        j = i - 1
        
        #loop to move elements larger than comparison index to 
        #one position ahead of their current position and goes backwards
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            yield arr 

        #sets next element as current element
        arr[j+1] = key

def selection_sort(arr, length):

    #loops through array
    for i in range(length):
        #sets smallest value to current index
        smallest = i
        #loops through array from current smallest value to end
        for j in range(i+1, length):
            #if current element is smaller than current smallest
            if arr[j] < arr[smallest]:

                #sets new current smallest index
                smallest = j
        #swaps index of current element and smallest element
        arr[i], arr[smallest] = arr[smallest], arr[i]
        yield arr

def bubble_sort(arr, length):
    
    #loop to iterate through array
    for i in range(length):
        #nested loop to iterate through rest of array once max element is found, until it reaches end
        for j in range(length-i-1):
            #if element is larger than the next one
            if arr[j] > arr[j+1]:
                #swaps positions so larger number is after
                arr[j+1], arr [j] = arr[j], arr[j+1]
                yield arr
    
def update(arr):

    for bar, height in zip(bars,arr):

        bar.set_height(height)       

arr = [17, 38, 94, 92, 13, 84, 100, 64, 54, 88, 62, 8, 2, 55, 95, 45, 57, 3, 83,
12, 42, 60, 43, 39, 87, 51, 75, 72, 30, 93, 29, 97, 91, 16, 40, 71, 66, 73, 78,
61, 19, 63, 14, 82, 53, 80, 24, 56, 77, 25, 59, 21, 22, 35, 69, 86, 9, 76, 68,
79, 85, 58, 6, 46, 27, 31, 1, 33, 11, 34, 96, 41, 23, 37, 28, 20, 74, 81, 5,
52, 4, 44, 18, 15, 90, 10, 65, 7, 98, 89, 48, 32, 67, 47, 50, 49, 36, 26, 70, 99]

length = len(arr)

fig, ax = plt.subplots()
bars = ax.bar(range(length), arr)

algo = insertion_sort(arr, length)

ani = animation.FuncAnimation(fig, update, frames= algo, interval = 1, repeat=False)

plt.show()

# x = selection_sort(arr, length)
# for z in x:
#     print(z)

