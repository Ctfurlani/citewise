# Suffix array

In computer science, a suffix array is a sorted array of all suffixes of a string. It is a data structure used in, among others, full-text indices, data-compression algorithms, and the field of bibliometrics.

Suffix arrays were introduced by Manber & Myers (1990) as a simple, space efficient alternative to suffix trees. They had independently been discovered by Gaston Gonnet in 1987 under the name PAT array (Gonnet, Baeza-Yates & Snider 1992).

Li, Li & Huo (2016) gave the first in-place 𝒪(n) time suffix array construction algorithm that is optimal both in time and space, where in-place means that the algorithm only needs 𝒪(1) additional space beyond the input string and the output suffix array.

Enhanced suffix arrays (ESAs) are suffix arrays with additional tables that reproduce the full functionality of suffix trees preserving the same time and memory complexity.

A sorted array of only some (rather than all) suffixes of a string is called a sparse suffix array.

Let S=S[1]S[2]...S[n] be an n-string and let S[i,j] denote the substring of S ranging from i to j inclusive.

The suffix array A of S is now defined to be an array of integers providing the starting positions of suffixes of S in lexicographical order. This means, an entry A[i] contains the starting position of the i-th smallest suffix in S and thus for all 1≤i≤n: S[A[i−1],n]<S[A[i],n].

Each suffix of S shows up in A exactly once. Suffixes are simple strings. These strings are sorted (as in a paper dictionary), before their starting positions (integer indices) are saved in A.

Consider the text S=banana$ to be indexed:

The text ends with the special sentinel letter $ that is unique and lexicographically smaller than any other character. The text has the following suffixes:

These suffixes can be sorted in ascending order:

The suffix array A contains the starting positions of these sorted suffixes:

The suffix array with the suffixes written out vertically underneath for clarity:

So for example, A[3] contains the value 4, and therefore refers to the suffix starting at position 4 within S, which is the suffix ana$.

Suffix arrays are closely related to suffix trees:

Suffix arrays can be constructed by performing a depth-first traversal of a suffix tree. The suffix array corresponds to the leaf-labels given in the order in which these are visited during the traversal, if edges are visited in the lexicographical order of their first character.

A suffix tree can be constructed in linear time by using a combination of suffix array and LCP array. For a description of the algorithm, see the corresponding section in the LCP array article.

It has been shown that every suffix tree algorithm can be systematically replaced with an algorithm that uses a suffix array enhanced with additional information (such as the LCP array) and solves the same problem in the same time complexity.

Advantages of suffix arrays over suffix trees include improved space requirements, simpler linear time construction algorithms (e.g., compared to Ukkonen's algorithm) and improved cache locality.

Suffix arrays were introduced by Manber & Myers (1990) in order to improve over the space requirements of suffix trees: Suffix arrays store n integers. Assuming an integer requires 4 bytes, a suffix array requires 4n bytes in total. This is significantly less than the 20n bytes which are required by a careful suffix tree implementation.

However, in certain applications, the space requirements of suffix arrays may still be prohibitive. Analyzed in bits, a suffix array requires 𝒪(nlog⁡n) space, whereas the original text over an alphabet of size σ only requires 𝒪(nlog⁡σ) bits.

For a human genome with σ=4 and n=3.4×109 the suffix array would therefore occupy about 16 times more memory than the genome itself.

Such discrepancies motivated a trend towards compressed suffix arrays and BWT-based compressed full-text indices such as the FM-index. These data structures require only space within the size of the text or even less.

A suffix tree can be built in 𝒪(n) and can be converted into a suffix array by traversing the tree depth-first also in 𝒪(n), so there exist algorithms that can build a suffix array in 𝒪(n).

A naive approach to construct a suffix array is to use a comparison-based sorting algorithm. These algorithms require 𝒪(nlog⁡n) suffix comparisons, but a suffix comparison runs in 𝒪(n) time, so the overall runtime of this approach is 𝒪(n2log⁡n).

More advanced algorithms take advantage of the fact that the suffixes to be sorted are not arbitrary strings but related to each other. These algorithms strive to achieve the following goals:

minimal asymptotic complexity Θ(n)

lightweight in space, meaning little or no working memory beside the text and the suffix array itself is needed

fast in practice

One of the first algorithms to achieve all goals is the SA-IS algorithm of Nong, Zhang & Chan (2009). The algorithm is also rather simple (< 100 LOC) and can be enhanced to simultaneously construct the LCP array. The SA-IS algorithm is one of the fastest known suffix array construction algorithms. A careful implementation by Yuta Mori outperforms most other linear or super-linear construction approaches.

Beside time and space requirements, suffix array construction algorithms are also differentiated by their supported alphabet:  constant alphabets where the alphabet size is bound by a constant, integer alphabets where characters are integers in a range depending on n and general alphabets where only character comparisons are allowed.

Most suffix array construction algorithms are based on one of the following approaches:

Prefix doubling algorithms are based on a strategy of Karp, Miller & Rosenberg (1972). The idea is to find prefixes that honor the lexicographic ordering of suffixes. The assessed prefix length doubles in each iteration of the algorithm until a prefix is unique and provides the rank of the associated suffix.

Recursive algorithms follow the approach of the suffix tree construction algorithm by Farach (1997) to recursively sort a subset of suffixes. This subset is then used to infer a suffix array of the remaining suffixes. Both of these suffix arrays are then merged to compute the final suffix array.

Induced copying algorithms are similar to recursive algorithms in the sense that they use an already sorted subset to induce a fast sort of the remaining suffixes. The difference is that these algorithms favor iteration over recursion to sort the selected suffix subset. A survey of this diverse group of algorithms has been put together by Puglisi, Smyth & Turpin (2007).

Source: https://en.wikipedia.org/wiki/Suffix_array (Wikipedia, CC BY-SA 4.0)
