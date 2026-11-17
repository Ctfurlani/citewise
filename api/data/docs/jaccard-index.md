# Jaccard index

The Jaccard index is a statistic used for gauging the similarity and diversity of sample sets.

It is defined in general taking the ratio of two sizes (areas or volumes), the intersection size divided by the union size, also called intersection over union (IoU).

The concept was first introduced by Grove Karl Gilbert in 1884 as the “ratio of verification” in contexts of geological prediction evaluation. and now is often called the critical success index in meteorology. It was later developed independently by Paul Jaccard, originally giving the French name coefficient de communauté (coefficient of community), and independently formulated again by Taffee Tadashi Tanimoto. Thus, it is also called Tanimoto index or Tanimoto coefficient in some fields.

The Jaccard index measures similarity between finite non-empty sample sets and is defined as the size of the intersection divided by the size of the union of the sample sets:

J(A,B)=|A∩B||A∪B|=|A∩B||A|+|B|−|A∩B|.

The Jaccard index can be interpreted as a normalized measure of overlap between two sets, where the intersection represents shared elements and the union represents the total set of distinct elements. By definition, 0≤J(A,B)≤1. If the sets A and B have no elements in common, their intersection is empty, so |A∩B|=0 and therefore J(A,B)=0. The other extreme is that the two sets are equal. In that case A∩B=A∪B=A=B, so then J(A,B)=1. The Jaccard index is widely used in computer science, ecology, genomics and other sciences where binary or binarized data are used.

Both the exact solution and approximation methods are available for hypothesis testing with the Jaccard index. Jaccard similarity also applies to bags, i.e., multisets. This has a similar formula, but the symbols used represent bag intersection and bag sum (not union). The maximum value is 1/2.

J(A,B)=|A∩B||A⊎B|=|A∩B||A|+|B|.

The Jaccard distance, which measures dissimilarity between sample sets, is complementary to the Jaccard index and is obtained by subtracting the Jaccard index from 1 or, equivalently, by dividing the difference of the sizes of the union and the intersection of two sets by the size of the union:

dJ(A,B)=1−J(A,B)=|A∪B|−|A∩B||A∪B|.

An alternative interpretation of the Jaccard distance is as the ratio of the size of the symmetric difference A△B=(A∪B)−(A∩B) to the union.

Jaccard distance is commonly used to calculate an n × n matrix for clustering and multidimensional scaling  of n sample sets. These distance measures are commonly used in cluster analysis for grouping similar observations.

This distance is a metric on the collection of all finite sets.

There is also a version of the Jaccard distance for measures, including probability measures. If μ is a measure on a measurable space X, then we define the Jaccard index by

Jμ(A,B)=μ(A∩B)μ(A∪B),

and the Jaccard distance by

dμ(A,B)=1−Jμ(A,B)=μ(A△B)μ(A∪B).

The definition is not well-defined when μ(A∪B)=0 or μ(A∪B)=∞.

The MinHash min-wise independent permutations locality-sensitive hashing scheme may be used to efficiently compute an accurate estimate of the Jaccard similarity index of pairs of sets, where each set is represented by a constant-sized signature derived from the minimum values of a hash function.

The Jaccard index is particularly useful for analyzing large-scale and sparse datasets in modern data mining applications.

Given two objects, A and B, each with n binary attributes, the Jaccard index is a useful measure of the overlap that A and B share with their attributes.  Each attribute of A and B can either be 0 or 1.  The total number of each combination of attributes for both A and B are specified as follows:

M11 represents the total number of attributes where A and B both have a value of 1.

M01 represents the total number of attributes where the attribute of A is 0 and the attribute of B is 1.

M10 represents the total number of attributes where the attribute of A is 1 and the attribute of B is 0.

M00 represents the total number of attributes where A and B both have a value of 0.

Each attribute must fall into one of these four categories, meaning that

M11+M01+M10+M00=n.

The Jaccard similarity index, J, is given as

J=M11M01+M10+M11.

The Jaccard distance, dJ, is given as

dJ=M01+M10M01+M10+M11=1−J.

Statistical inference can be made based on the Jaccard similarity index, and consequently related metrics. Given two sample sets A and B with n attributes, a statistical test can be conducted to see if an overlap is statistically significant. The exact solution is available, although computation can be costly as n increases. Estimation methods are available either by approximating a multinomial distribution or by bootstrapping.

When used for binary attributes, the Jaccard index is very similar to the simple matching coefficient. The main difference is that the SMC has the term M00 in its numerator and denominator, whereas the Jaccard index does not. Thus, the SMC counts both mutual presences (when an attribute is present in both sets) and mutual absence (when an attribute is absent in both sets) as matches and compares it to the total number of attributes in the universe, whereas the Jaccard index only counts mutual presence as matches and compares it to the number of attributes that have been chosen by at least one of the two sets.

In market basket analysis, for example, the basket of two consumers who we wish to compare might only contain a small fraction of all the available products in the store, so the SMC will usually return very high values of similarities even when the baskets bear very little resemblance. This can be inappropriate in sparse datasets where M00 is typically large, making the Jaccard index a more appropriate measure of similarity in that context. For example, consider a supermarket with 1000 products and two customers. The basket of the first customer contains salt and pepper and the basket of the second contains salt and sugar. In this scenario, the similarity between the two baskets as measured by the Jaccard index would be 1/3, but the similarity becomes 0.998 using the SMC.

Source: https://en.wikipedia.org/wiki/Jaccard_index (Wikipedia, CC BY-SA 4.0)
