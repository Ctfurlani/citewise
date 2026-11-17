# Probabilistic relevance model

The probabilistic relevance model was devised by Stephen E. Robertson and Karen Spärck Jones as a framework for probabilistic models to come. It is a formalism of information retrieval useful to derive ranking functions used by search engines and web search engines in order to rank matching documents according to their relevance to a given search query.

It is a theoretical model estimating the probability that a document dj is relevant to a query q. The model assumes that this probability of relevance depends on the query and document representations. Furthermore, it assumes that there is a portion of all documents that is preferred by the user as the answer set for query q. Such an ideal answer set is called R and should maximize the overall probability of relevance to that user. The prediction is that documents in this set R are relevant to the query, while documents not present in the set are non-relevant.

sim(dj,q)=P(R|d→j)P(R¯|d→j)

There are some limitations to this framework that need to be addressed by further development:

There is no accurate estimate for the first run probabilities

Index terms are not weighted

Terms are assumed mutually independent

To address these and other concerns, other models have been developed from the probabilistic relevance framework, among them the Binary Independence Model from the same author. The best-known derivatives of this framework are the Okapi (BM25) weighting scheme and its multifield refinement, BM25F.

Source: https://en.wikipedia.org/wiki/Probabilistic_relevance_model (Wikipedia, CC BY-SA 4.0)
