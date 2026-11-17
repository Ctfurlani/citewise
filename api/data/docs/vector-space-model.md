# Vector space model

Vector space model (VSM) or term vector model is an algebraic model for representing text documents (or more generally, items) as vectors such that the distance between vectors represents the relevance between the documents. It is used in information filtering, information retrieval, indexing and relevance rankings.  Its first use was in the SMART Information Retrieval System.

In this section we consider a particular vector space model based on the bag-of-words representation. Documents and queries are represented as vectors.

dj=(w1,j,w2,j,…,wn,j)

q=(w1,q,w2,q,…,wn,q)

Each dimension corresponds to a separate term. If a term occurs in the document, its value in the vector is non-zero. Several different ways of computing these values, also known as (term) weights, have been developed. One of the best known schemes is tf-idf weighting (see the example below).

The definition of term depends on the application. Typically terms are single words, keywords, or longer phrases. If words are chosen to be the terms, the dimensionality of the vector is the number of words in the vocabulary (the number of distinct words occurring in the corpus).

Vector operations can be used to compare documents with queries.

Candidate documents from the corpus can be retrieved and ranked using a variety of methods. Relevance rankings of documents in a keyword search can be calculated, using the assumptions of document similarities theory, by comparing the deviation of angles between each document vector and the original query vector where the query is represented as a vector with same dimension as the vectors that represent the other documents.

In practice, it is easier to calculate the cosine of the angle between the vectors, instead of the angle itself:

cos⁡θ=𝐝𝟐⋅𝐪‖𝐝𝟐‖‖𝐪‖

Where 𝐝𝟐⋅𝐪 is the intersection (i.e. the dot product) of the document (d2 in the figure to the right) and the query (q in the figure) vectors, ‖𝐝𝟐‖ is the norm of vector d2, and ‖𝐪‖ is the norm of vector q. The norm of a vector is calculated as such:

‖𝐪‖=∑i=1nqi2

Using the cosine the similarity between document dj and query q can be calculated as:

cos(dj,q)=𝐝𝐣⋅𝐪‖𝐝𝐣‖‖𝐪‖=∑i=1Ndi,jqi∑i=1Ndi,j2∑i=1Nqi2

As all vectors under consideration by this model are element-wise nonnegative, a cosine value of zero means that the query and document vector are orthogonal and have no match (i.e. the query term does not exist in the document being considered). See cosine similarity for further information.

In the classic vector space model proposed by Salton, Wong and Yang, the term-specific weights in the document vectors are products of local and global parameters. The model is known as term frequency–inverse document frequency (tf–idf) model. The weight vector for document d is 𝐯d=[w1,d,w2,d,…,wN,d]T, where

wt,d=tft,d⋅log⁡|D||{d′∈D|t∈d′}|

and

tft,d is term frequency of term t in document d (a local parameter)

log⁡|D||{d′∈D|t∈d′}| is inverse document frequency (a global parameter). |D| is the total number of documents in the document set; |{d′∈D|t∈d′}| is the number of documents containing the term t.

The vector space model has the following advantages over the Standard Boolean model:

Allows ranking documents according to their possible relevance

Allows retrieving items with a partial term overlap

Most of these advantages are a consequence of the difference in the density of the document collection representation between Boolean and term frequency-inverse document frequency approaches. When using Boolean weights, any document lies in a vertex in a n-dimensional hypercube. Therefore, the possible document representations are 2n and the maximum Euclidean distance between pairs is n. As documents are added to the document collection, the region defined by the hypercube's vertices become more populated and hence denser. Unlike Boolean, when a document is added using term frequency-inverse document frequency weights, the inverse document frequencies of the terms in the new document decrease while that of the remaining terms increase. In average, as documents are added, the region where documents lie expands regulating the density of the entire collection representation. This behavior models the original motivation of Salton and his colleagues that a document collection represented in a low density region could yield better retrieval results.

The vector space model has the following limitations:

Query terms are assumed to be independent, so phrases might not be represented well in the ranking

Semantic sensitivity; documents with similar context but different term vocabulary won't be associated

Many of these difficulties can, however, be overcome by the integration of various tools, including mathematical techniques such as singular value decomposition and lexical databases such as WordNet.

Models based on and extending the vector space model include:

Generalized vector space model

Latent semantic analysis

Rocchio Classification

Random indexing

The following software packages may be of interest to those wishing to experiment with vector models and implement search services based upon them.

Apache Lucene. Apache Lucene is a high-performance, open source, full-featured text search engine library written entirely in Java.

OpenSearch (software), Elasticsearch and Solr: the three most well-known search engine programs based on Lucene. Others are also available.

Gensim is a Python+NumPy framework for Vector Space modelling. It contains incremental (memory-efficient) algorithms for term frequency-inverse document frequency, latent semantic indexing, random projections and latent Dirichlet allocation.

Weka. Weka is a popular data mining package for Java including WordVectors and Bag Of Words models.

Word2vec. Word2vec uses vector spaces for word embeddings.

The Generalized vector space model is a generalization of the VSM used in information retrieval. Wong et al. presented an analysis of the problems that the pairwise orthogonality assumption of the VSM creates. From here they extended the VSM to the generalized vector space model (GVSM).

Recently Tsatsaronis focused on the first approach. They measure semantic relatedness (SR) using a thesaurus (O) like WordNet. It considers the path length, captured by compactness (SCM), and the path depth, captured by semantic path elaboration (SPE).

Building also on the first approach, Waitelonis et al. have computed semantic relatedness from Linked Open Data resources including DBpedia as well as the YAGO taxonomy. Thereby they exploits taxonomic relationships among semantic entities in documents and queries after named entity linking.

G. Salton (1962), "Some experiments in the generation of word and document associations" Proceeding AFIPS '62 (Fall) Proceedings of the December 4–6, 1962, fall joint computer conference,  pages 234–250. (Early paper of Salton using the term-document matrix formalization)

G. Salton, A. Wong, and C. S. Yang (1975), "A Vector Space Model for Automatic Indexing" Communications of the ACM, vol. 18, nr. 11, pages 613–620. (Article in which a vector space model was presented)

David Dubin (2004), The Most Influential Paper Gerard Salton Never Wrote (Explains the history of the Vector Space Model and the non-existence of a frequently cited publication)

Description of the vector space model

Source: https://en.wikipedia.org/wiki/Vector_space_model (Wikipedia, CC BY-SA 4.0)
