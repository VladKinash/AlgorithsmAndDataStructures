from typing import List
from collections import Counter 
import time
import random
import heapq

def containsDuplicate(nums: List[int]) -> bool:
    uniques = set()

    for i in nums: 
        if i in uniques:
            return True
        uniques.add(i)
    
    return False


lst = [2, 2, 4, 5]

def AAAgroupAnagrams( strs: List[str]) -> List[List[str]]:
    h = {}
    for word in strs:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in h:
            h[sortedWord] = [word]
        else:
            h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
    return final

strs = ["eat","tea","tan","ate","nat","bat"]


def is_there_duplicate(arr):
    seen = set()

    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    
    return False


def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right: 
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[right].lower() != s[left].lower():
            return False 
        left += 1
        right -= 1
    return True
        

    

def is_balanced(s):
    stack = []

    for i in s:
        if i in "[({":
            stack.append(i)
        elif i in ")]}":
            if not stack:
                return False
            elif(i == ")" and stack[-1] != "(") or \
                (i == "]" and stack[-1] != "[") or \
                (i == "}" and stack[-1] != "{"):
                    return False
            stack.pop()
    return not stack


def is_int_Palindrome(x: int) -> bool:
    x_string = str(x)
    return x_string == x_string[::-1]

def mergelists(l1, l2):

    return sorted(l1+l2)


#for loop will take a slice of ints and see if there's an element of window larger than the first one
#if no element is larger than output is 0

def best_time_to_buy_sell(prices):
    total = 0
    for i in range(len(prices)):
        window = prices[i:]
        if max(window) > prices[i] and prices[i] == min(window):
            total = max(window) - prices[i]
    return total


def getConcatenation(nums: List[int]) -> List[int]:

    for i in nums: 
        nums.append(i)

    return nums


def stackBaseball(operations: List[str]) -> int:
    stack = []

    for i in operations:
        try:
            stack.append(int(i))
        except ValueError:
            if i == "C" and stack:
                stack.pop()
            elif i == "D": 
                stack.append(stack[-1]*2)
            elif i == "+":
                stack.append(sum(stack[-2:]))
    return sum(stack)




def removeDuplicates(nums: List[int]) -> int:
    hash_table = set()
    k = 0
    for i in nums: 
        if i not in hash_table:
            hash_table.add(i)
            k += 1
    return k + 1


def removeDuplicatess(nums):
    if len(nums) == 0:
        return 0

    # Use two pointers: one for iterating the array, and the other for placing unique elements
    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    # Return the new length of the modified array (unique elements + 1)
    return unique_index + 1


def largestAltitude( gain: List[int]) -> int:
        stack = [0]

        for i in gain:
            stack.append(i+stack[-1])

        return max(stack)




def reverseList(head):
    output = []
    point = len(head) - 1
    for i in head:
        output.append(head[point])
        point -= 1
    return output



def lengthOfLastWord(s: str) -> int:
    words = s.split()
    return len(words[-1])



def searchInsert(nums: List[int], target: int) -> int:
    total = 0
    if nums[-1] < target:
        return len(nums)
    for i in nums:
        if i == target:
            return total
        elif i > target:
            return total
        else:
            total+=1
    return 0


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]: 
    temp = []
    stack = 0
    
    for i in nums:
        for d in nums:
            if i > d:
                stack += 1
        temp.append(stack)
        stack = 0
    return temp


def permute(nums: List[int]) -> List[List[int]]:
    output = []
    
    while len(output) != len(nums) * len(nums):
        
        random.shuffle(nums)

        if nums not in output:
            output.append(nums)
        print(output)

    return output




    
def fixed_sliding_window(arr: List[int], k: int):
    
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    for i in range(1, len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray + arr[i+k-1]

        result.append(curr_subarray)
    
    return result




def findMaxAverage(nums: List[int], k: int) -> float:
    curr_sub = sum(nums[:k])
    result = [curr_sub]

    for i in range(1, len(nums)-k+1):
        curr_sub = curr_sub - nums[i-1]
        curr_sub = curr_sub + nums[i+k-1]
        
        result.append(curr_sub)
    
    return max(result) / k


def missingNumber(nums: List[int]) -> int:

    for i in range(len(nums) +1 ):
        if i not in nums:
            return i


def numJewelsInStones(jewels: str, stones: str) -> int:
    h = set()
    total = 0

    for i in jewels:
        h.add(i)

    for i in stones:
        if i in h:
            total += 1

    return total





def commonChars(words: List[str]) -> List[str]:

    h = set()
    curr_word = ""
    output = []
    to_remove = []

    for i in words:
        curr_word = i
        for i in curr_word:
            h.add(i)
    
    for i in words:
        curr_word = i
        for i in h:
            if i not in curr_word:
                to_remove.append(i)

    

    for i in h:
        output.append(i)

    return output




def intersection( nums1: List[int], nums2: List[int]) -> List[int]:

    common = []
    for i in nums1:
        if i in nums2 and i not in common:
            common.append(i)


    return common





def uncommonFromSentences(s1: str, s2: str) -> List[str]:

    words = [word for word in s1.split() + s2.split()]
    output = []
    seen = set()

    for i in words:
        if i not in seen and words.count(i) == 1:
            seen.add(i)
            output.append(i)


    return output



def reverseVowels(s: str) -> str:
    left = 0
    right = len(s) - 1
    vowels = "AEIOUaeiou"
    chars = list(s)

    while left < right: 

        if chars[left] in vowels and chars[right] in vowels:
            chars[right] = s[left]
            chars[left] = s[right]
            right -= 1
            left += 1

        elif chars[left] in vowels and chars[right] not in vowels:
            right -= 1
        
        elif chars[right] in vowels and chars[left] not in vowels:
            left += 1

        else:
            right -= 1
            left += 1

    s = ""
    for i in chars:
        s += i

    return s


def moveZeroes( nums: List[int]) -> None:

    zeroes = 0

    for i in nums:
        if i == 0:
            nums.remove(i)
            zeroes += 1
    print(nums)

    for i in range(zeroes):
        nums.append(0)
    
    return nums



def twoSumII(numbers: List[int], target: int) -> List[int]:

    left = 0
    right = len(numbers) - 1
    result = []

    while left < right:

        if numbers[left] + numbers[right] == target:
            result.append(left + 1) 
            result.append(right + 1)
            return result
        
        elif numbers[left] + numbers[right] < target:
            left += 1

        elif numbers[left] + numbers[right] > target:
            right -= 1  



    return result

        

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    h = {}

    for i in nums:
        
        if i not in h:
            h[i] = 1

        elif i in h:
            h[i] += 1


    top_frequent = dict(sorted(h.items(), key=lambda x: x[1], reverse=True))
        
    output = list(top_frequent.keys())[:k]

    return output




def repeatedNTimes(nums: List[int]) -> int:
    h = set()

    for i in reversed(nums):
        if i not in h:
            h.add(i)
        else:
            return i
        
    return 0



def generate_hashtag(s):
    if len(s) >= 140 or s == "":
        return False
    hashtag = "#"
    s = s.split()
    for i in s:
        low_i = i.lower()
        hashtag += low_i[0].upper() + low_i[1:]
    return hashtag



s = "CoDeWaRs is niCe"


print(generate_hashtag(s))