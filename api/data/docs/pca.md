# Principal component analysis

Principal component analysis (PCA) is a linear dimensionality reduction technique with applications in exploratory data analysis, visualization and data preprocessing.

The data are linearly transformed onto a new coordinate system such that the directions (principal components) capturing the largest variation in the data can be easily identified. PCA is a form of feature selection by collapsing correlated features.

The principal components of a collection of points in a real coordinate space are a sequence of p unit vectors, where the i-th vector is the direction of a line that best fits the data while being orthogonal to the first i−1 vectors. Here, a best-fitting line is defined as one that minimizes the average squared perpendicular distance from the points to the line. These directions (i.e., principal components) constitute an orthonormal basis in which different individual dimensions of the data are linearly uncorrelated. Many studies use the first two principal components in order to plot the data in two dimensions and to visually identify clusters of closely related data points.

Principal component analysis has applications in many fields such as population genetics, microbiome studies, and atmospheric science.

When performing PCA, the first principal component of a set of p variables is the derived variable formed as a linear combination of the original variables that explains the most variance. The second principal component explains the most variance in what is left once the effect of the first component is removed, and we may proceed through p iterations until all the variance is explained. PCA is most commonly used when many of the variables are highly correlated with each other and it is desirable to reduce their number to an independent set.

The first principal component can equivalently be defined as a direction that maximizes the variance of the projected data. The i-th principal component can be taken as a direction orthogonal to the first i−1 principal components that maximizes the variance of the projected data.

For either objective, it can be shown that the principal components are eigenvectors of the data's covariance matrix. Thus, the principal components are often computed by eigendecomposition of the data covariance matrix or singular value decomposition of the data matrix. PCA is the simplest of the true eigenvector-based multivariate analyses and is closely related to factor analysis. Factor analysis typically incorporates more domain-specific assumptions about the underlying structure and solves eigenvectors of a slightly different matrix. PCA is also related to canonical correlation analysis (CCA). CCA defines coordinate systems that optimally describe the cross-covariance between two datasets while PCA defines a new orthogonal coordinate system that optimally describes variance in a single dataset. Robust and L1-norm-based variants of standard PCA have also been proposed.

PCA was invented in 1901 by Karl Pearson, as an analogue of the principal axis theorem in mechanics; it was later independently developed and named by Harold Hotelling in the 1930s. Depending on the field of application, it is also named the discrete Karhunen–Loève transform (KLT) in signal processing, the Hotelling transform in multivariate quality control, proper orthogonal decomposition (POD) in mechanical engineering, singular value decomposition (SVD) of X (invented in the last quarter of the 19th century), eigenvalue decomposition (EVD) of XTX in linear algebra, factor analysis (for a discussion of the differences between PCA and factor analysis see Ch. 7 of Jolliffe's Principal Component Analysis), Eckart–Young theorem (Harman, 1960), or empirical orthogonal functions (EOF) in meteorological science (Lorenz, 1956), empirical eigenfunction decomposition (Sirovich, 1987), quasiharmonic modes (Brooks et al., 1988), spectral decomposition in noise and vibration, and empirical modal analysis in structural dynamics.

PCA can be thought of as fitting a p-dimensional ellipsoid to the data, where each axis of the ellipsoid represents a principal component. If some axis of the ellipsoid is small, then the variance along that axis is also small.

To find the axes of the ellipsoid, we must first center the values of each variable in the dataset on 0 by subtracting the mean of the variable's observed values from each of those values. These transformed values are used instead of the original observed values for each of the variables. Then, we compute the covariance matrix of the data and calculate the eigenvalues and corresponding eigenvectors of this covariance matrix. Then we must normalize each of the orthogonal eigenvectors to turn them into unit vectors. Once this is done, each of the mutually-orthogonal unit eigenvectors can be interpreted as an axis of the ellipsoid fitted to the data. This choice of basis will transform the covariance matrix into a diagonalized form, in which the diagonal elements represent the variance of each axis. The proportion of the variance that each eigenvector represents can be calculated by dividing the eigenvalue corresponding to that eigenvector by the sum of all eigenvalues.

Biplots and scree plots (degree of explained variance) are used to interpret findings of the PCA.

PCA is defined as an orthogonal linear transformation on a real inner product space that transforms the data to a new coordinate system such that the greatest variance by some scalar projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.

Consider an n×p data matrix, X, with column-wise zero empirical mean (the sample mean of each column has been shifted to zero), where each of the n rows represents a different repetition of the experiment, and each of the p columns gives a particular kind of feature (say, the results from a particular sensor).

Mathematically, the transformation is defined by a set of size l (where l is usually selected to be strictly less than p to reduce dimensionality) of p-dimensional vectors of weights or coefficients 𝐰(k)=(w1,…,wp)(k) that map each row vector 𝐱(i)=(x1,…,xp)(i) of X to a new vector of principal component scores 𝐭(i)=(t1,…,tl)(i), given by

tk(i)=𝐱(i)⋅𝐰(k)fori=1,…,nk=1,…,l

in such a way that the individual variables t1,…,tl of t considered over the data set successively inherit the maximum possible variance from X, with each coefficient vector w constrained to be a unit vector.

The above may equivalently be written in matrix form as

𝐓=𝐗𝐖

where

𝐓ik=tk(i),

𝐗ij=xj(i), and

𝐖jk=wj(k).

In order to maximize variance, the first weight vector w(1) thus has to satisfy

𝐰(1)=arg⁡max‖𝐰‖=1{∑i(t1)(i)2}=arg⁡max‖𝐰‖=1{∑i(𝐱(i)⋅𝐰)2}

Equivalently, writing this in matrix form gives

𝐰(1)=arg⁡max‖𝐰‖=1{‖𝐗𝐰‖2}=arg⁡max‖𝐰‖=1{𝐰𝖳𝐗𝖳𝐗𝐰}

Since w(1) has been defined to be a unit vector, it equivalently also satisfies

𝐰(1)=arg⁡max⁡{𝐰𝖳𝐗𝖳𝐗𝐰𝐰𝖳𝐰}

Source: https://en.wikipedia.org/wiki/Principal_component_analysis (Wikipedia, CC BY-SA 4.0)
