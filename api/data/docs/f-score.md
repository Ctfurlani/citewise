# F-score

In statistical analysis of binary classification and information retrieval systems, the F-score or F-measure is a measure of predictive performance. It is calculated from the precision and recall of the test, where the precision is the number of true positive results divided by the number of all samples predicted to be positive, including those not identified correctly, and the recall is the number of true positive results divided by the number of all samples that should have been identified as positive. Precision is also known as positive predictive value, and recall is also known as sensitivity in diagnostic binary classification.

The F1 score is the harmonic mean of the precision and recall. It thus symmetrically represents both precision and recall in one metric. The more generic Fβ score applies additional weights, valuing one of precision or recall more than the other.

The highest possible value of an F-score is 1.0, indicating perfect precision and recall, and the lowest possible value is 0, if the precision or the recall is zero.

The name F-measure is believed to be named after a different F function in Van Rijsbergen's book, when introduced to the Fourth Message Understanding Conference (MUC-4, 1992).

The traditional F-measure or balanced F-score (F1 score) is the harmonic mean of precision and recall:

F1=2recall−1+precision−1=2precision⋅recallprecision+recall=2TP2TP+FP+FN

With precision = TP / (TP + FP) and recall = TP / (TP + FN), it follows that the numerator of F1 is the sum of their numerators and the denominator of F1 is the sum of their denominators.

If FP = FN

F1=2TP2TP+2FP=TPTP+FP

or

F1=2TP2TP+2FN=TPTP+FN

So, F1 = precision = recall

If TP = FP = FN

F1=2TP2TP+2FP=2TP4TP=12=0.5

or

F1=2TP2TP+2FN=2TP4TP=12=0.5

To see it as a harmonic mean, note that F1−1=12(recall−1+precision−1).

A more general F score, Fβ, that uses a positive real factor β, where β is chosen such that recall is considered β2 times as important as precision, is:

Fβ=β2+1(β2⋅recall−1)+precision−1=(1+β2)⋅precision⋅recall(β2⋅precision)+recall

To see that as a weighted harmonic mean, note that Fβ−1=1β+β−1(β⋅recall−1+β−1⋅precision−1).

In terms of Type I and type II errors this becomes:

Fβ=(1+β2)⋅TP(1+β2)⋅TP+β2⋅FN+FP=(1+β2)⋅TP(TP+FN)⋅β2+(TP+FP)

Two commonly used values for β are 2, which weighs recall higher than precision, and 1/2, which weighs recall lower than precision.

The F-measure was derived so that Fβ "measures the effectiveness of retrieval with respect to a user who attaches β times as much importance to recall as precision". It is based on Van Rijsbergen's effectiveness measure

E=1−(αp+1−αr)−1

Their relationship is: Fβ=1−E where α=11+β2

This is related to the field of binary classification where recall is often termed "sensitivity".

Precision-recall curve, and thus the Fβ score, explicitly depends on the ratio

r of positive to negative test cases.

This means that comparison of the

F-score across different problems with differing class ratios is

problematic. One way to address this issue (see e.g., Siblini et al.,

2020) is to use a standard class ratio r0 when making such comparisons.

The F-score is often used in the field of information retrieval for measuring search, document classification, and query classification performance. It is particularly relevant in applications which are primarily concerned with the positive class and where the positive class is rare relative to the negative class.

Earlier works focused primarily on the F1 score, but with the proliferation of large scale search engines, performance goals changed to place more emphasis on either precision or recall and so Fβ is seen in wide application.

The F-score is also used in machine learning. However, the F-measures do not take true negatives into account, hence measures such as the Matthews correlation coefficient, Informedness or  Cohen's kappa may be preferred to assess the performance of a binary classifier.

The F-score has been widely used in the natural language processing literature, such as in the evaluation of named entity recognition and word segmentation.

The F1 score is the Dice coefficient of the set of retrieved items and the set of relevant items.

The F1-score of a classifier which always predicts the positive class converges to 1 as the probability of the positive class increases.

The F1-score of a classifier which always predicts the positive class is equal to 2 * proportion_of_positive_class / ( 1 + proportion_of_positive_class ), since the recall is 1, and the precision is equal to the proportion of the positive class.

If the scoring model is uninformative (cannot distinguish between the positive and negative class) then the optimal threshold is 0 so that the positive class is always predicted.

F1 score is concave in the true positive rate.

David Hand and others criticize the widespread use of the F1 score since it gives equal importance to precision and recall. In practice, different types of mis-classifications incur different costs. In other words, the relative importance of precision and recall is an aspect of the problem.

According to Davide Chicco and Giuseppe Jurman, the F1 score is less truthful and informative than the Matthews correlation coefficient (MCC) in binary evaluation classification.

David M W Powers has pointed out that F1 ignores the True Negatives and thus is misleading for unbalanced classes, while kappa and correlation measures are symmetric and assess both directions of predictability - the classifier predicting the true class and the true class predicting the classifier prediction, proposing separate multiclass measures Informedness and Markedness for the two directions, noting that their geometric mean is correlation.

Another source of critique of F1 is its lack of symmetry. It means it may change its value when dataset labeling is changed - the "positive" samples are named "negative" and vice versa.

This criticism is met by the P4 metric definition, which is sometimes indicated as a symmetrical extension of F1.

Finally, Ferrer

and Dyrland et al.

argue that the expected cost (or its counterpart, the expected utility) is the only principled metric for evaluation of classification decisions, having various advantages over the F-score and the MCC. Both works show that the F-score can result in wrong conclusions about the absolute and relative quality of systems.

While the F-measure is the harmonic mean of recall and precision, the Fowlkes–Mallows index is their geometric mean.

The F-score is also used for evaluating classification problems with more than two classes (Multiclass classification). A common method is to average the F-score over each class, aiming at a balanced measurement of performance.

Macro F1 is a macro-averaged F1 score aiming at a balanced performance measurement. To calculate macro F1, two different averaging-formulas have been used: the F1 score of (arithmetic) class-wise precision and recall means or the arithmetic mean of class-wise F1 scores, where the latter exhibits more desirable properties.

Source: https://en.wikipedia.org/wiki/F-score (Wikipedia, CC BY-SA 4.0)
