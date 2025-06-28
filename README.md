# What is the longest sum of consecutive integers that add up to *n*?


## Description

A simple program that calculates the longest sum of consecutive numbers that add up to any given integer. It can be configured to display all possible consecutive sums, not just the longest.


## How it works

Here is a rough overview of the mathematics behind the process:


Firstly, the sum can be represented as (x + 1) + (x + 2) + (x + 3)... + (x + L), where *x* is the integer just below the smallest number in the sum, and *L* is the length of the sum.

This can be written more algebraically in the expression Lx + 0.5L<sup>2</sup> + 0.5L

Making this expression equal to the number *n* that we want to sum to, we can rearrange to obtain a formula for our starting number *x* (given the integer *n* that we want to sum to and a given length *L* of the sum) and then construct the rest of the sum from there.
