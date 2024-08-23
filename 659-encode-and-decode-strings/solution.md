Having just a single special char as delimiter of words is not gonna work because that delimiter could show up in some of the words.
Wouldn't it be nice if in the encoded string, we somehow already knew how many chars would go in the first word, how many chars would
go into the second word and ... .

But we can't store a separate state like: [4, 5] meaning the first word is 4 chars, the second has 5 chars. We want the 
encode and decode ops to be **stateless**.

We wanna store it in the encoded string itself.

We can put the word len at the beginning of the word like: 4neet. But what if the word itself had some integers in it?
Then we need another delimiter. We want to have sth like: 4#neet.

So in decode(), we're gonna read each char until we hit a #(delimiter) and once we reach the delimiter and we take all the chars
that we read and transform it into an int and then we're gonna count the chars after the delimiter until we count the exact number
of chars that is specified by the integer at the beginning.

With this, we're gonna expect a **single** #, even if the next char was a #, it still works. It also works if there was some integer in the
word itself.

![](./659-1.png)