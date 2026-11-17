# Trie

In computer science, a trie (,  ), also known as a digital tree or prefix tree, is a specialized search tree data structure used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. Instead, each node's position within the trie determines its associated key, with the connections between nodes defined by individual characters rather than the entire key.

Tries are particularly effective for tasks such as autocomplete, spell checking, and IP routing, offering advantages over hash tables due to their prefix-based organization and lack of hash collisions. Every child node shares a common prefix with its parent node, and the root node represents the empty string. While basic trie implementations can be memory-intensive, various optimization techniques such as compression and bitwise representations have been developed to improve their efficiency. A notable optimization is the radix tree, which provides more efficient prefix-based storage.

While tries store character strings, they can be adapted to work with any ordered sequence of elements, such as permutations of digits or shapes. A notable variant is the bitwise trie, which uses individual bits from fixed-length binary data (such as integers or memory addresses) as keys.

The idea of a trie for representing a set of strings was first abstractly described by Axel Thue in 1912. Tries were first described in a computer context by René de la Briandais in 1959.

The idea was independently described in 1960 by Edward Fredkin, who coined the term trie, pronouncing it  (as "tree"), after the middle syllable of retrieval. However, other authors pronounce it  (as "try"), in an attempt to distinguish it verbally from "tree".

Tries are a form of string-indexed look-up data structure, which is used to store a dictionary list of words that can be searched on in a manner that allows for efficient generation of completion lists. A prefix trie is an ordered tree data structure used in the representation of a set of strings over a finite alphabet set, which allows efficient storage of words with common prefixes.

Tries can be efficacious on string-searching algorithms such as predictive text, approximate string matching, and spell checking in comparison to binary search trees. A trie can be seen as a tree-shaped deterministic finite automaton.

Tries support various operations: insertion, deletion, and lookup of a string key. Tries are composed of nodes that contain links, which either point to other suffix child nodes or null. As for every tree, each node except the root is pointed to by only one other node, called its parent. Each node contains as many links as the number of characters in the applicable alphabet (although tries tend to have a substantial number of null links). In some cases, the alphabet used is simply that of the character encoding—resulting in, for example, a size of 128 in the case of ASCII.

The null links within the children of a node emphasize the following characteristics:

Characters and string keys are implicitly stored in the trie, and include a character sentinel value indicating string termination.

Each node contains one possible link to a prefix of strong keys of the set.

A basic structure type of nodes in the trie is as follows: Node may contain an optional Value, which is associated with the key that corresponds to the node.

Searching for a value in a trie is guided by the characters in the search string key, as each node in the trie contains a corresponding link to each possible character in the given string. Thus, following the string within the trie yields the associated value for the given string key. A null link during the search indicates the inexistence of the key.

The following pseudocode implements the search procedure for a given string key in a rooted trie x.

In the above pseudocode, x and key correspond to the pointer of the trie's root node and the string key, respectively. The search operation takes O(m) time, where m is the size of the string parameter key. In a balanced binary search tree, on the other hand, it takes O(mlog⁡n) time, in the worst case, since key needs to be compared with O(log⁡n) other keys and each comparison takes O(m) time, in the worst case.

The trie occupies less space, in comparison with a binary search tree, in the case of a large number of short strings, since nodes share common initial string subsequences and store the keys implicitly.

Insertion into a trie is guided by using the character sets as indexes to the children array until the last character of the string key is reached. Each node in the trie corresponds to one call of the radix sorting routine, as the trie structure reflects the execution pattern of the top-down radix sort.

If null links are encountered before reaching the last character of the string key, new nodes are created. The input value is assigned to the value of the last node traversed, which is the node that corresponds to the key.

Deletion of a key–value pair from a trie involves finding the node corresponding to the key, setting its value to null, and recursively removing nodes that have no children.

The procedure begins by examining key; an empty string indicates arrival at the node corresponding to the (original) key, in which case its value is set to null. If the node, then, has null value and no children, it is removed from the trie by returning null; otherwise, the node is kept by returning the node itself.

A trie can be used to replace a hash table, over which it has the following advantages:

Searching for a node with an associated key of size m has the complexity of O(m), whereas an imperfect hash function may have numerous colliding keys, and the worst-case lookup speed of such a table would be O(N), where N denotes the total number of nodes within the table.

Tries do not need a hash function for the operation, unlike a hash table; there are also no collisions of different keys in a trie.

Within a trie, keys can be efficiently sorted lexicographically.

However, tries are less efficient than a hash table when the data is directly accessed on a secondary storage device such as a hard disk drive that has higher random access time than the main memory.

Source: https://en.wikipedia.org/wiki/Trie (Wikipedia, CC BY-SA 4.0)
