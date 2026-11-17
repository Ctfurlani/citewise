# Locality-sensitive hashing

In computer science, locality-sensitive hashing (LSH) is a fuzzy hashing technique that hashes similar input items into the same "buckets" with high probability. The number of buckets is much smaller than the universe of possible input items. Since similar items end up in the same buckets, this technique can be used for data clustering and nearest neighbor search. It differs from conventional hashing techniques in that hash collisions are maximized, not minimized. Alternatively, the technique can be seen as a way to reduce the dimensionality of high-dimensional data; high-dimensional input items can be reduced to low-dimensional versions while preserving relative distances between items.

Hashing-based approximate nearest-neighbor search algorithms generally use one of two main categories of hashing methods: either data-independent methods, such as locality-sensitive hashing (LSH); or data-dependent methods, such as locality-preserving hashing (LPH).

Locality-preserving hashing was initially devised as a way to facilitate data pipelining in implementations of massively parallel algorithms that use randomized routing and universal hashing to reduce memory contention and network congestion.

A finite family ℱ of functions h:M→S is defined to be an LSH family

for

a metric space ℳ=(M,d),

a threshold r>0,

an approximation factor c>1,

and probabilities p1>p2

if it satisfies the following condition. For any two points a,b∈M and a hash function h chosen uniformly at random from ℱ:

If d(a,b)≤r, then h(a)=h(b) (i.e., a and b collide) with probability at least p1,

If d(a,b)≥cr, then h(a)=h(b) with probability at most p2.

Such a family ℱ is called (r,cr,p1,p2)-sensitive.

Alternatively it is possible to define an LSH family on a universe of items U endowed with a similarity function ϕ:U×U→[0,1]. In this setting, a LSH scheme is a family of hash functions H coupled with a probability distribution D over H such that a function h∈H chosen according to D satisfies Pr[h(a)=h(b)]=ϕ(a,b) for each a,b∈U.

Given a (d1,d2,p1,p2)-sensitive family ℱ, we can construct new families 𝒢 by either the AND-construction or OR-construction of ℱ.

To create an AND-construction, we define a new family 𝒢 of hash functions g, where each function g is constructed from k random functions h1,…,hk from ℱ.  We then say that for a hash function g∈𝒢, g(x)=g(y) if and only if all hi(x)=hi(y) for i=1,2,…,k.  Since the members of ℱ are independently chosen for any g∈𝒢, 𝒢 is a (d1,d2,p1k,p2k)-sensitive family.

To create an OR-construction, we define a new family 𝒢 of hash functions g, where each function g is constructed from k random functions h1,…,hk from ℱ.  We then say that for a hash function g∈𝒢, g(x)=g(y) if and only if hi(x)=hi(y) for one or more values of i.  Since the members of ℱ are independently chosen for any g∈𝒢, 𝒢 is a (d1,d2,1−(1−p1)k,1−(1−p2)k)-sensitive family.

LSH has been applied to several problem domains, including:

Near-duplicate detection

Hierarchical clustering

Genome-wide association study

Image similarity identification

VisualRank

Gene expression similarity identification

Audio similarity identification

Nearest neighbor search

Audio fingerprint

Digital video fingerprinting

Shared memory organization in parallel computing

Physical data organization in database management systems

Training fully connected neural networks

Computer security

Machine learning

One of the easiest ways to construct an LSH family is by bit sampling. This approach works for the Hamming distance over d-dimensional vectors {0,1}d. Here, the family ℱ of hash functions is simply the family of all the projections of points on one of the d coordinates, i.e., ℱ={h:{0,1}d→{0,1}∣h(x)=xi for some i∈{1,…,d}}, where xi is the ith coordinate of x. A random function h from ℱ simply selects a random bit from the input point. This family has the following parameters: P1=1−R/d, P2=1−cR/d.

That is, any two vectors x,y with Hamming distance at most R collide under a random h with probability at least P1.

Any x,y with Hamming distance at least cR collide with probability at most P2.

Suppose U  is composed of subsets of some ground set of enumerable items S and the similarity function of interest is the Jaccard index J. If π is a permutation on the indices of S, for A⊆S let h(A)=mina∈A{π(a)}. Each possible choice of π defines a single hash function h mapping input sets to elements of S.

Define the function family H to be the set of all such functions and let D be the uniform distribution. Given two sets A,B⊆S the event that h(A)=h(B) corresponds exactly to the event that the minimizer of π over A∪B lies inside A∩B. As h was chosen uniformly at random, Pr[h(A)=h(B)]=J(A,B) and (H,D) define an LSH scheme for the Jaccard index.

Because the symmetric group on n elements has size n!, choosing a truly random permutation from the full symmetric group is infeasible for even moderately sized n. Because of this fact, there has been significant work on finding a family of permutations that is "min-wise independent" — a permutation family for which each element of the domain has equal probability of being the minimum under a randomly chosen π. It has been established that a min-wise independent family of permutations is at least of size lcm⁡{1,2,…,n}≥en−o(n), and that this bound is tight.

Because min-wise independent families are too big for practical applications, two variant notions of min-wise independence are introduced: restricted min-wise independent permutations families, and approximate min-wise independent families.

Restricted min-wise independence is the min-wise independence property restricted to certain sets of cardinality at most k.

Approximate min-wise independence differs from the property by at most a fixed ε.

Nilsimsa is a locality-sensitive hashing algorithm used in anti-spam efforts. The goal of Nilsimsa is to generate a hash digest of an email message such that the digests of two similar messages are similar to each other.  The paper suggests that the Nilsimsa satisfies three requirements:

The digest identifying each message should not vary significantly for changes that can be produced automatically.

The encoding must be robust against intentional attacks.

The encoding should support an extremely low risk of false positives.

Testing performed in the paper on a range of file types identified the Nilsimsa hash as having a significantly higher false positive rate when compared to other similarity digest schemes such as TLSH, Ssdeep and Sdhash.

TLSH is locality-sensitive hashing algorithm designed for a range of security and digital forensic applications. The goal of TLSH is to generate hash digests for messages such that low distances between digests indicate that their corresponding messages are likely to be similar.

An implementation of TLSH is available as open-source software.

The random projection method of LSH due to Moses Charikar called SimHash (also sometimes called arccos) uses an approximation of the cosine distance between vectors.  The technique was used to approximate the NP-complete max-cut problem.

Source: https://en.wikipedia.org/wiki/Locality-sensitive_hashing (Wikipedia, CC BY-SA 4.0)
