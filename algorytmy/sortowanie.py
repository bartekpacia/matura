{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "source": [
    "# Here it is!\n",
    "My first Jupyter Notebook, for testing purposes.\n",
    "\n",
    "Cool, isn't it?"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "source": [
    "list = []\n",
    "for i in range(1000):\n",
    "    list.append(i)\n",
    "\n",
    "print(len(list))\n"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": 174,
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "1000\n"
     ]
    }
   ]
  },
  {
   "source": [
    "# Let's do something useful\n",
    "First, I'll create a list filled with random numbers. Then, I'll sort it and in the end, I'll check whether it contains 50 and if it does, then on which position it is.\n",
    "\n",
    "### Random list"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[14, 26, 73, 5, 0, 50, 73, 51, 36, 81, 8, 81, 0, 35, 86, 0, 8, 22, 86, 93, 32, 22, 52, 79, 51, 96, 40, 27, 82, 100, 0, 93, 88, 46, 97, 51, 0, 79, 97, 98, 40, 77, 70, 8, 55, 5, 78, 33, 46, 61, 98, 65, 0, 15, 25, 72, 78, 77, 29, 41, 84, 19, 40, 73, 60, 8, 17, 74, 49, 22, 44, 56, 16, 56, 97, 31, 52, 99, 24, 98, 39, 38, 38, 34, 70, 62, 92, 10, 17, 37, 91, 91, 57, 22, 87, 26, 8, 79, 93, 91]\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "nums = []\n",
    "for i in range(0, 100):\n",
    "    random_num = random.randint(0, 100)\n",
    "    nums.append(random_num)\n",
    "\n",
    "print(nums)"
   ]
  },
  {
   "source": [
    "### Sorting\n"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "len(nums)=100 [0, 0, 0, 0, 0, 0, 5, 5, 8, 8, 8, 8, 8, 10, 14, 15, 16, 17, 17, 19, 22, 22, 22, 22, 24, 25, 26, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 40, 40, 41, 44, 46, 46, 49, 50, 51, 51, 51, 52, 52, 55, 56, 56, 57, 60, 61, 62, 65, 70, 70, 72, 73, 73, 73, 74, 77, 77, 78, 78, 79, 79, 79, 81, 81, 82, 84, 86, 86, 87, 88, 91, 91, 91, 92, 93, 93, 93, 96, 97, 97, 97, 98, 98, 98, 99, 100]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "from typing import List\n",
    "\n",
    "def bubble_sort(arr: List[int]) -> List[int]:\n",
    "    narr = arr.copy()\n",
    "    l = len(narr)\n",
    "    for i in range(l - 1):\n",
    "        for j in range(l - i - 1):\n",
    "            if narr[j] > narr[j + 1]:\n",
    "                narr[j], narr[j + 1] = narr[j + 1], narr[j]\n",
    "\n",
    "    return narr\n",
    "\n",
    "\n",
    "sorted_nums = bubble_sort(nums)\n",
    "print(f\"{len(nums)=}\", sorted_nums)"
   ]
  },
  {
   "source": [
    "# Finding\n",
    "Now, let's code binary search to find 50!\n"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "index=None\n"
     ]
    }
   ],
   "source": [
    "def bsearch(arr: List[int], target: int) -> int:\n",
    "    low = 0\n",
    "    high = len(arr) - 1\n",
    "\n",
    "    while low <= high:\n",
    "        mid = (low + high) // 2\n",
    "        guess = arr[mid]\n",
    "        if guess < target:\n",
    "            low = guess + 1\n",
    "        elif guess > target:\n",
    "            high = guess - 1\n",
    "        elif guess == target:\n",
    "            return mid\n",
    "\n",
    "        return None\n",
    "\n",
    "\n",
    "index = bsearch(sorted_nums, 50)\n",
    "print(f\"{index=}\")"
   ]
  },
  {
   "source": [
    "# Voila\n",
    "This is cool."
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}