# Solutions

Scribbles about the problems and the approaches taken to solve them.

### Two Sum

<details open>
<summary>Description</summary>

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

</details>

<details>
<summary>Examples</summary>

**1:**

> Input: nums = [2,7,11,15], target = 9
> 
> Output: [0,1]
> 
> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


**2:**

> Input: nums = [3,2,4], target = 6
> 
> Output: [1,2]


**3:**

> Input: nums = [3,3], target = 6
> 
> Output: [0,1]


</details>

<details>
<summary>Solution</summary>

Iterate through the given array of integers only once. While you go through it, store it and the index in a dictionary.

Should be something like:

dict[number] = index_of_number.

So now, while iterating through the array, you come across a preexisting complement in the array, you can return the index of the complement and the number you are on.

</details>

