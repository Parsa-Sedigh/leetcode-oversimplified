In fibonacci sequence, we start with number 0, next is 1 and then every number after that, is going to be the sum of two previous numbers.

We don't have a `return` statement in the generator function because it's a generator function. Instead, the way we return values from a
generator function is with the keyword `yield`.

Note: We don't break in the `while(true)` loop of our generator function because when calling `next()`, that's gonna execute the generator
function until yield gets called in our loop and it will pause the execution of that generator function. So we won't get an infinite loop.

So calling next() for the first time will yield 0, then the next time of calling next(), it will complete one iteration of the while loop,
updates n2, updates n1 and then yield again and the next time of calling next(), will reiterate the while loop(because the execution continues) and
yield the next number.

So the iteration of our infinite while loop pauses and continues when we call next() when using that generator function.

Note: Python supports generators but a lot of languages do not, like c++ and java doesn't have native support for generators. There are
workarounds for this in those languages.

Why would you even want to implement a generator in the first place?
- for an infinite sequence like fibonacci, we don't have to actually execute that infinite loop forever, we can just call .next() on it as
many times as we want to. Iterator design pattern is related to this. A generator could be used to iterate through sth like 
a linked list or maybe a binary tree. The difference is usually iterators are only used on finite data structures not necessarily on an infinite sequence.
- it saves our state for us. Maybe using a generator would be more simple for sth like a binary search tree where we kinda still save our
pointers. You can also do that with an iterator but the code would be slightly more complex.