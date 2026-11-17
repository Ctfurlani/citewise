# Hash table

In computer science, a hash table is a data structure that implements an associative array, also called a dictionary or simply map; an associative array is an abstract data type that maps keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. A map implemented by a hash table is called a hash map.

Most hash table designs employ an imperfect hash function. Hash collisions, where the hash function generates the same index for more than one key, therefore typically must be accommodated in some way. Common strategies to handle hash collisions include separate chaining, which stores multiple elements in the same slot using linked lists, and open addressing, which searches for the next available slot according to a probing sequence.

In a well-dimensioned hash table, the average time complexity for each lookup is independent of the number of elements stored in the table. Many hash table designs also allow arbitrary insertions and deletions of key–value pairs, at amortized constant average cost per operation.

Hashing is an example of a space–time tradeoff. If memory is infinite, the entire key can be used directly as an index to locate its value with a single memory access. On the other hand, if infinite time is available, values can be stored without regard for their keys, and a binary search or linear search can be used to retrieve the element.

In many situations, hash tables turn out to be on average more efficient than search trees or any other table lookup structure. For this reason, they are widely used in many kinds of computer software, particularly for associative arrays, database indexing, caches, and sets. Many programming languages provide built-in hash table structures, such as Python’s dictionaries, Java’s HashMap, C++’s unordered_map, and Go maps, which abstract the complexity of hashing from the programmer.

The idea of hashing arose independently in different places. In January 1953, Hans Peter Luhn wrote an internal IBM memorandum that used hashing with chaining.  The first example of open addressing was proposed by A. D. Linh, building on Luhn's memorandum. Around the same time, Gene Amdahl, Elaine M. McGraw, Nathaniel Rochester, and Arthur Samuel of IBM Research implemented hashing for the IBM 701 assembler. Open addressing with linear probing is credited to Amdahl, although Andrey Ershov independently had the same idea. The term "open addressing" was coined by W. Wesley Peterson in his article which discusses the problem of search in large files.

The first published work on hashing with chaining is credited to Arnold Dumey, who discussed the idea of using remainder modulo a prime as a hash function. The word "hashing" was first published in an article by Robert Morris. A theoretical analysis of linear probing was submitted originally by Konheim and Weiss.

An associative array stores a set of (key, value) pairs and allows insertion, deletion, and lookup (search), with the constraint of unique keys. In the hash table implementation of associative arrays, an array A of length m is partially filled with n elements, where m≥n. A key x is hashed using a hash function h to compute an index location A[h(x)] in the hash table, where h(x)<m. At this index, both the key and its associated value are stored. Storing the key alongside the value ensures that lookups can verify the key at the index to retrieve the correct value, even in the presence of collisions. Under reasonable assumptions, hash tables have better time complexity bounds on search, delete, and insert operations in comparison to self-balancing binary search trees.

The efficiency of a hash table depends on the load factor (α), defined as the ratio of the number of stored elements to the number of available slots, with lower load factors generally yielding faster operations. Load factor is a critical statistic of a hash table, and is defined as follows:

load factor (α)=nm,

where

n is the number of key-value pairs in the hash table.

m is the number of buckets.

The performance of the hash table deteriorates in relation to the load factor α.  In the limit of large m and n, each bucket statistically has a Poisson distribution with expectation λ=α for an ideally random hash function.

The implementation of a hash table typically ensures that the load factor α remains below a certain constant, αmax. This helps maintain good performance. Therefore, a common approach is to resize or "rehash" the hash table whenever the load factor α reaches αmax. Similarly the table may also be resized if the load factor drops below αmax/4.

With open addressing, each slot of the bucket array holds exactly one item. Therefore an open-addressed hash table cannot have a load factor greater than 1.

The performance of open addressing becomes very bad when the load factor approaches 1. Therefore a hash table that uses open addressing must be resized or rehashed if the load factor α approaches 1.

With open addressing, acceptable figures of max load factor αmax should range around 0.6 to 0.75.

With separate chaining hash tables, each slot of the bucket array stores a pointer to a list or array of data.

Separate chaining hash tables suffer gradually declining performance as the load factor grows, unlike the sharply decreasing performance of open addressing hash tables around α=1. There is not a fixed point with respect to load factor beyond which resizing is absolutely needed.

With separate chaining, the value of αmax that gives best performance is typically between 1 and 3.

A hash function h:U→{0,...,m−1} maps the universe U of keys to indices or slots within the table, that is, h(x)∈{0,...,m−1} for x∈U. The conventional implementations of hash functions are based on the integer universe assumption that all elements of the table stem from the universe U={0,...,u−1}, where the bit length of u is confined within the word size of a computer architecture.

A hash function h is said to be perfect for a given set S if it is injective on S, that is, if each element x∈S maps to a different value in 0,...,m−1. A perfect hash function can be created if all the keys are known ahead of time.

The schemes of hashing used in integer universe assumption include hashing by division, hashing by multiplication, universal hashing, dynamic perfect hashing, and static perfect hashing. However, hashing by division is the commonly used scheme.

Source: https://en.wikipedia.org/wiki/Hash_table (Wikipedia, CC BY-SA 4.0)
