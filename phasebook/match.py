import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    
    i = 0
    n = len(fave_numbers_2)
    m = len(fave_numbers_1)
    quickSort(fave_numbers_1, 0, m-1)
    for i in range(n):
        if (binarySearch(fave_numbers_1, 0, m - 1, fave_numbers_2[i]) == -1):
            return False
 

    return True
 

 
def binarySearch(arr, low, high, x):
    if(high >= low):
        mid = (low + high)//2
 

        if((mid == 0 or x > arr[mid-1]) and (arr[mid] == x)):
            return mid
        elif(x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)
 
    return -1
 
 
def partition(A, start, end):
    x = A[end]
    i = (start - 1)
 
    for j in range(start, end):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return (i + 1)
 

 
def quickSort(A, start, end):

    if(start < end):
        pi = partition(A, start, end)
        quickSort(A, start, pi - 1)
        quickSort(A, pi + 1, end)
 
 

 