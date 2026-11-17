# Latent semantic analysis

Latent semantic analysis (LSA) is a technique in natural language processing, in particular distributional semantics, of analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms.  LSA assumes that words that are close in meaning will occur in similar pieces of text (the distributional hypothesis).  A matrix containing word counts per document (rows represent unique words and columns represent each document) is constructed from a large piece of text and a mathematical technique called singular value decomposition (SVD) is used to reduce the number of rows while preserving the similarity structure among columns.  Documents are then compared by cosine similarity between any two columns.  Values close to 1 represent very similar documents while values close to 0 represent very dissimilar documents.

An information retrieval technique using latent semantic structure was patented in 1988 by Scott Deerwester, Susan Dumais, George Furnas, Richard Harshman, Thomas Landauer, Karen Lochbaum and Lynn Streeter. In the context of its application to information retrieval, it is sometimes called latent semantic indexing (LSI).

LSA can use a document-term matrix which describes the occurrences of terms in documents; it is a sparse matrix whose rows correspond to terms and whose columns correspond to documents. A typical example of the weighting of the elements of the matrix is tf-idf (term frequency–inverse document frequency): the weight of an element of the matrix is proportional to the number of times the terms appear in each document, where rare terms are upweighted to reflect their relative importance.

This matrix is also common to standard semantic models, though it is not necessarily explicitly expressed as a matrix, since the mathematical properties of matrices are not always used.

After the construction of the occurrence matrix, LSA finds a low-rank approximation to the term-document matrix. There could be various reasons for these approximations:

The original term-document matrix is presumed too large for the computing resources; in this case, the approximated low rank  matrix is interpreted as an approximation (a "least and necessary evil").

The original term-document matrix is presumed noisy: for example, anecdotal instances of terms are to be eliminated. From this point of view, the approximated matrix is interpreted as a de-noisified matrix (a better matrix than the original).

The original term-document matrix is presumed overly sparse relative to the "true" term-document matrix.  That is, the original matrix lists only the words actually in each document, whereas we might be interested in all words related to each document—generally a much larger set due to synonymy.

The consequence of the rank lowering is that some dimensions are combined and depend on more than one term:

{(car), (truck), (flower)} → {(1.3452 * car + 0.2828 * truck), (flower)}

This mitigates the problem of identifying synonymy, as the rank lowering is expected to merge the dimensions associated with terms that have similar meanings. It also partially mitigates the problem with polysemy, since components of polysemous words that point in the "right" direction are added to the components of words that share a similar meaning. Conversely, components that point in other directions tend to either simply cancel out, or, at worst, to be smaller than components in the directions corresponding to the intended sense.

Let X be a matrix where element (i,j) describes the occurrence of term i in document j (this can be, for example, the frequency). X will look like this:

𝐝j↓𝐭iT→[x1,1…x1,j…x1,n⋮⋱⋮⋱⋮xi,1…xi,j…xi,n⋮⋱⋮⋱⋮xm,1…xm,j…xm,n]

Now a row in this matrix will be a vector corresponding to a term, giving its relation to each document:

𝐭iT=[xi,1…xi,j…xi,n]

Likewise, a column in this matrix will be a vector corresponding to a document, giving its relation to each term:

𝐝j=[x1,j⋮xi,j⋮xm,j]

Now the dot product 𝐭iT𝐭p between two term vectors gives the correlation between the terms over the set of documents. The matrix product XXT contains all these dot products. Element (i,p) (which is equal to element (p,i)) contains the dot product 𝐭iT𝐭p (=𝐭pT𝐭i). Likewise, the matrix XTX contains the dot products between all the document vectors, giving their correlation over the terms: 𝐝jT𝐝q=𝐝qT𝐝j.

Now, from the theory of linear algebra, there exists a decomposition of X such that U and V are orthogonal matrices and Σ is a diagonal matrix. This is called a singular value decomposition (SVD):

X=UΣVT

The matrix products giving us the term and document correlations then become

XXT=(UΣVT)(UΣVT)T=(UΣVT)(VTTΣTUT)=UΣVTVΣTUT=UΣΣTUTXTX=(UΣVT)T(UΣVT)=(VTTΣTUT)(UΣVT)=VΣTUTUΣVT=VΣTΣVT

Since ΣΣT and ΣTΣ are diagonal we see that U must contain the eigenvectors of XXT, while V must be the eigenvectors of XTX. Both products have the same non-zero eigenvalues, given by the non-zero entries of ΣΣT, or equally, by the non-zero entries of ΣTΣ. Now the decomposition looks like this:

XUΣVT(𝐝j)(𝐝̂j)↓↓(𝐭iT)→[x1,1…x1,j…x1,n⋮⋱⋮⋱⋮xi,1…xi,j…xi,n⋮⋱⋮⋱⋮xm,1…xm,j…xm,n]=(𝐭̂iT)→[[𝐮1]…[𝐮l]]⋅[σ1…0⋮⋱⋮0…σl]⋅[[𝐯1]⋮[𝐯l]]

The values σ1,…,σl are called the singular values, and u1,…,ul and v1,…,vl the left and right singular vectors.

Notice the only part of U that contributes to 𝐭i is the i'th row.

Let this row vector be called t̂iT.

Likewise, the only part of VT that contributes to 𝐝j is the j'th column, d̂j.

These are not the eigenvectors, but depend on all the eigenvectors.

It turns out that when you select the k largest singular values, and their corresponding singular vectors from U and V, you get the rank k approximation to X with the smallest error (Frobenius norm). This approximation has a minimal error.  But more importantly we can now treat the term and document vectors as a "semantic space". The row "term" vector 𝐭̂iT then has k entries mapping it to a lower-dimensional space. These new dimensions do not relate to any comprehensible concepts. They are a lower-dimensional approximation of the higher-dimensional space. Likewise, the "document" vector 𝐝̂j is an approximation in this lower-dimensional space. We write this approximation as

Xk=UkΣkVkT

You can now do the following:

See how related documents j and q are in the low-dimensional space by comparing the vectors Σk⋅𝐝̂j and Σk⋅𝐝̂q (typically by cosine similarity).

Comparing terms i and p by comparing the vectors Σk⋅𝐭̂i and Σk⋅𝐭̂p. Note that 𝐭̂ is now a column vector.

Documents and term vector representations can be clustered using traditional clustering algorithms like k-means using similarity measures like cosine.

Given a query, view this as a mini document, and compare it to your documents in the low-dimensional space.

To do the latter, you must first translate your query into the low-dimensional space. It is then intuitive that you must use the same transformation that you use on your documents:

𝐝̂j=Σk−1UkT𝐝j

Note here that the inverse of the diagonal matrix Σk may be found by inverting each nonzero value within the matrix.

Source: https://en.wikipedia.org/wiki/Latent_semantic_analysis (Wikipedia, CC BY-SA 4.0)
