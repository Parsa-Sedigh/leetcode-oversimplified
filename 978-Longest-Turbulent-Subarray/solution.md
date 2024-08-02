## Brute-force
By checking every single sub-arr, we can do this in o(n^2) because that's how many sub-arrays it's gonna be.

## sliding window 
We want to identify patterns to eliminate repeated work in the solution.

r - l + 1 is the length of the current subarr


Note: when we have =, we wanna get rid of those two consecutive equal elements in our window. So move r forward
and l to where r previously was. By moving r forward, we would completely get rid of the equal elements.
But in case of a duplicate sign, we wanna get rid of the prev sign so that we don't have any duplicates.
And we know the last 3 els are causing the duplicate signs, so we wanna get rid of the first one. To do that,
we move l to be behind r and we won't move r.
So when we have ... , 4, 5, 6, 2
                            ^
                            r

we wanna move l to where 5 exists. So that we don't have this anymore: 4 < 5 < 6 , instead we have: 5 < 6 which is not 
duplicate anymore. Then, in the next iteration we know the prev is gonna be "", so r is gonna move forward.