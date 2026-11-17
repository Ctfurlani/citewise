# B-tree

In computer science, a B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. The B-tree generalizes the binary search tree, allowing nodes to have more than two children.

By allowing more children under one node than a regular self-balancing binary search tree, the B-tree reduces the height of the tree and puts the data in fewer separate blocks. This is especially important for trees stored in secondary storage (e.g., disk drives), as these systems have relatively high latency and work with relatively large blocks of data, hence the B-tree's use in databases and file systems. This remains a major advantage when the tree is stored in memory, as modern computer systems rely heavily on CPU caches. Compared to reading from the cache, reading from memory after a cache miss costs significant time.

While working at Boeing Research Labs, Rudolf Bayer and Edward M. McCreight invented B-trees to efficiently manage index pages for large random-access files. Their basic assumption was that indices would be so voluminous that only small chunks of the tree could fit in the main memory. Bayer and McCreight's paper Organization and maintenance of large ordered indices was first circulated in July 1970 and later published in Acta Informatica.

Bayer and McCreight never explained what, if anything, the B stands for; Boeing, balanced, between, broad, bushy, and Bayer have been suggested. When asked, "I want to know what B in B-Tree stands for," McCreight answered:Everybody does!

So you just have no idea what a lunchtime conversation can turn into. So there we were, Rudy and I, at lunch. We had to give the thing a name.... We were working for Boeing at the time, but we couldn't use the name without talking to the lawyers. So there's a B.

It has to do with Balance. There's another B.

Rudy was the senior author. Rudy (Bayer) was several years older than I am, and had... many more publications than I did. So there's another B.

And so at the lunch table, we never did resolve whether there was one of those that made more sense than the rest.

What Rudy likes to say is, the more you think about what the B in B-Tree means, the better you understand B-Trees!

According to Knuth's definition, a B-tree of order m is a tree that satisfies the following properties:

Every node has at most m children.

Every node, except for the root and the leaves, has at least ⌈m/2⌉ children.

The root node has at least two children unless it is a leaf.

All leaves appear on the same level.

A non-leaf node with k children contains k−1 keys.

The keys of each non-leaf node act as separation values that divide its subtrees. For example, if an internal node has 3 child nodes (or subtrees), then it must have 2 keys: a1 and a2. All values in the leftmost subtree will be less than a1, all values in the middle subtree will be between a1 and a2, and all values in the rightmost subtree will be greater than a2.

Internal nodes

Internal nodes (also known as inner nodes) are all nodes except for leaf nodes and the root node. They are usually represented as an ordered set of elements and child pointers. Every internal node contains a maximum of U children and a minimum of L children. Thus, the number of elements is always 1 less than the number of child pointers (the number of elements is between L−1 and U−1). U must be either 2L or 2L−1; therefore, each internal node is at least half full. The relationship between U and L implies that two half-full nodes can be joined to make a legal node, and one full node can be split into two legal nodes (if there's room to push one element up into the parent). These properties make it possible to delete and insert new values into a B-tree while also adjusting the tree to preserve its properties.

The root node

The root node's number of children has the same upper limit as internal nodes but has no lower limit. For example, when there are fewer than L−1 elements in the entire tree, the root will be the only node in the tree with no children at all.

Leaf nodes

In Knuth's terminology, the "leaf" nodes are the actual data objects/chunks. The internal nodes that are one level above these leaves are what would be called the "leaves" by other authors: these nodes only store keys (at most m-1, and at least m/2-1 if they are not the root) and pointers (one for each key) to nodes carrying the data objects/chunks.

A B-tree of depth n+1 can hold about U times as many items as a B-tree of depth n, but the cost of search, insert, and delete operations grows with the depth of the tree. As with any balanced tree, the cost grows much more slowly than the number of elements.

Some balanced trees store values only at leaf nodes and use different kinds of nodes for leaf nodes and internal nodes. B-trees keep values in every node in the tree except leaf nodes.

The literature on B-trees is not uniform in its terminology.

Bayer and McCreight (1972), Comer (1979), and others define the order of a B-tree as the minimum number of keys in a non-root node. Folk and Zoellick point out that terminology is ambiguous because the maximum number of keys is unclear. An order 3 B-tree might hold a maximum of 6 keys or a maximum of 7 keys. Knuth (1998) avoids the problem by defining the order to be the maximum number of children (which is one more than the maximum number of keys).

The term leaf is also inconsistent. Bayer and McCreight (1972) considered the leaf level to be the lowest level of keys, but Knuth considered the leaf level to be one level below the lowest keys. There are many possible implementation choices. In some designs, the leaves may hold the entire data record; in other designs, the leaves may only hold pointers to the data record. Those choices are not fundamental to the idea of a B-tree.

For simplicity, most authors assume there is a fixed number of keys that fit in a node. The basic assumption is that the key size and node size are both fixed. In practice, variable-length keys may be employed.

As with other trees, B-trees can be represented as a collection of three types of nodes: root, internal (a.k.a. interior), and leaf.

Source: https://en.wikipedia.org/wiki/B-tree (Wikipedia, CC BY-SA 4.0)
