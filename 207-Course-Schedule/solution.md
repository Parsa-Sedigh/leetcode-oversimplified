Courses are nodes in the graph.

The prerequisites arr is basically an arr of edges.

We can use both DFS and BFS.

In the adjacency list, for each of the courses(hashmap keys), we're gonna have a list of all of it's prerequisites.

As we backtrack, we can remove the node that we visited previously.

![](207-1.png)
![](207-2.png)

If we're able to complete every course, we can return True.

T: O(N + P). We have to go through every single path right? So we get O(P). We could have some nodes that don't have any paths or 
connections for them, so it depends on `n` as well. In other words, we have to go through every single node **and** path once.

How can we detect the cycle?

We use a hashset or arr. If we encountered a node that is already in visited hashset, we return False.

## Cracking FAANG
We wanna solve this with topological sort.

Why are we solving it with topological sort? When it seems like a DFS will work.

First of all, a topological sort is a DFS. Second: the followup of this question(II), we want the order that we can complete the courses in.
We can use topological sort for both of these questions.

---

First: We need to take the list of lists and build a graph or adjList where the keys are the courses and values are list of all prerequisites.
{course : [prereq1, ...], ...} .

Then starting from anypoint in graph, explore all the children of that node. We're keeping track of visited nodes and after exploring
a node, we backtrack(compensating actions).

We wanna check if our DFS can visit every node and we wanna watch out for cycles. But we wanna solve it in topological sort manner.

We typically use 3 sets for solving topological sort problems:
- white set: represents all of the nodes that we still need to process.
- grey set: all of the nodes that we're currently processing. Remember in DFS, we get to a node but first we need to fully
explore it's children. Now what happens when somewhere along the dependency chain of it's children, you end up at the node that
you started the search from? That would indicate a cycle and this is what the grey set aims to prevent. When we're processing a node, we
put it in grey set and if down the line in dfs, we end up at that node again, it means we have a cycle, so we exit and return False
- black set: nodes that we have fully visited. Meaning we have visited it's children and itself. So if we ever get back to a node
that's in black set, we can stop the search there and backtrack. Because it's already explored.

## Topological sort space and time:
- Time: O(V + E), V = number of vertexes in graph, E = number of edges in graph(or connections between nodes)
- Space: O(V). We're just storing the vertexes not any path OFC. So it only depends on number of vertexes