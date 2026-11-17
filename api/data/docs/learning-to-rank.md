# Learning to rank

Learning to rank (LTR) or machine-learned ranking (MLR) is the application of machine learning, often supervised, semi-supervised or reinforcement learning, in the construction of ranking models for information retrieval and recommender systems. Training data may, for example, consist of lists of items with some partial order specified between items in each list. This order is typically induced by giving a numerical or ordinal score or a binary judgment (e.g. "relevant" or "not relevant") for each item. The goal of constructing the ranking model is to rank new, unseen lists in a similar way to rankings in the training data.

Ranking is a central part of many information retrieval problems, such as document retrieval, collaborative filtering, sentiment analysis, and online advertising.

A possible architecture of a machine-learned search engine is shown in the accompanying figure.

Training data consists of queries and documents matching them together with the relevance degree of each match. It may be prepared manually by human assessors (or raters, as Google calls them), who check results for some queries and determine relevance of each result. It is not feasible to check the relevance of all documents, and so typically a technique called pooling is used — only the top few documents, retrieved by some existing ranking models are checked. This technique may introduce selection bias. Alternatively, training data may be derived automatically by analyzing clickthrough logs (i.e. search results which got clicks from users), query chains, or such search engines' features as Google's (since-replaced) SearchWiki. Clickthrough logs can be biased by the tendency of users to click on the top search results on the assumption that they are already well-ranked.

Training data is used by a learning algorithm to produce a ranking model which computes the relevance of documents for actual queries.

Typically, users expect a search query to complete in a short time (such as a few hundred milliseconds for web search), which makes it impossible to evaluate a complex ranking model on each document in the corpus, and so a two-phase scheme is used. First, a small number of potentially relevant documents are identified using simpler retrieval models which permit fast query evaluation, such as the vector space model, Boolean model, weighted AND, or BM25. This phase is called top-k document retrieval and many heuristics were proposed in the literature to accelerate it, such as using a document's static quality score and tiered indexes. In the second phase, a more accurate but computationally expensive machine-learned model is used to re-rank these documents.

Learning to rank algorithms have been applied in areas other than information retrieval:

In machine translation for ranking a set of hypothesized translations;

In computational biology for ranking candidate 3-D structures in protein structure prediction problems;

In recommender systems for identifying a ranked list of related news articles to recommend to a user after he or she has read a current news article.

For the convenience of MLR algorithms, query-document pairs are usually represented by numerical vectors, which are called feature vectors. Such an approach is sometimes called bag of features and is analogous to the bag of words model and vector space model used in information retrieval for representation of documents.

Components of such vectors are called features, factors or ranking signals. They may be divided into three groups (features from document retrieval are shown as examples):

Query-independent or static features — those features, which depend only on the document, but not on the query. For example, PageRank or document's length. Such features can be precomputed in off-line mode during indexing. They may be used to compute document's static quality score (or static rank), which is often used to speed up search query evaluation.

Query-dependent or dynamic features — those features, which depend both on the contents of the document and the query, such as TF-IDF score or other non-machine-learned ranking functions.

Query-level features or query features, which depend only on the query. For example, the number of words in a query.

Some examples of features, which were used in the well-known LETOR dataset:

TF, TF-IDF, BM25, and language modeling scores of document's zones (title, body, anchors text, URL) for a given query;

Lengths and IDF sums of document's zones;

Document's PageRank, HITS ranks and their variants.

Selecting and designing good features is an important area in machine learning, which is called feature engineering.

There are several measures (metrics) which are commonly used to judge how well an algorithm is doing on training data and to compare the performance of different MLR algorithms. Often a learning-to-rank problem is reformulated as an optimization problem with respect to one of these metrics.

Examples of ranking quality measures:

Mean average precision (MAP);

DCG and NDCG;

Precision@n, NDCG@n, where "@n" denotes that the metrics are evaluated only on top n documents;

Mean reciprocal rank;

Kendall's tau;

Spearman's rho.

DCG and its normalized variant NDCG are usually preferred in academic research when multiple levels of relevance are used. Other metrics such as MAP, MRR and precision, are defined only for binary judgments.

Recently, there have been proposed several new evaluation metrics which claim to model user's satisfaction with search results better than the DCG metric:

Expected reciprocal rank (ERR);

Yandex's pfound.

Both of these metrics are based on the assumption that the user is more likely to stop looking at search results after examining a more relevant document, than after a less relevant document.

Learning to Rank approaches are often categorized using one of three approaches: pointwise (where individual documents are ranked), pairwise (where pairs of documents are ranked into a relative order), and listwise (where an entire list of documents are ordered).

Tie-Yan Liu of Microsoft Research Asia has analyzed existing algorithms for learning to rank problems in his book Learning to Rank for Information Retrieval. He categorized them into three groups by their input spaces, output spaces, hypothesis spaces (the core function of the model) and loss functions: the pointwise, pairwise, and listwise approach. In practice, listwise approaches often outperform pairwise approaches and pointwise approaches. This statement was further supported by a large scale experiment on the performance of different learning-to-rank methods on a large collection of benchmark data sets.

In this section, without further notice, x denotes an object to be evaluated, for example, a document or an image, f(x) denotes a single-value hypothesis, h(⋅) denotes a bi-variate or multi-variate function and L(⋅) denotes the loss function.

Source: https://en.wikipedia.org/wiki/Learning_to_rank (Wikipedia, CC BY-SA 4.0)
