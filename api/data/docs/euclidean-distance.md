# Euclidean distance

In mathematics, the Euclidean distance between two points in a Euclidean space is the length of the line segment between them. It can be calculated from the Cartesian coordinates of the points using the Pythagorean theorem, and therefore is occasionally called the Pythagorean distance.

These names come from the ancient Greek mathematicians Euclid and Pythagoras. In the Greek deductive geometry exemplified by Euclid's Elements, distances were not represented as numbers but line segments of the same length, which were considered "equal". The notion of distance is inherent in the compass tool used to draw a circle, whose points all have the same distance from a common center point. The connection from the Pythagorean theorem to distance calculation was not made until the 18th century.

The distance between two objects that are not points is usually defined to be the smallest distance among pairs of points from the two objects. Formulas are known for computing distances between different types of objects, such as the distance from a point to a line. In advanced mathematics, the concept of distance has been generalized to abstract metric spaces, and other distances than Euclidean have been studied. In some applications in statistics and optimization, the square of the Euclidean distance is used instead of the distance itself.

The distance between any two points on the real line is the absolute value of the numerical difference of their coordinates, their absolute difference. Thus if p and q are two points on the real line, then the distance between them is given by:

d(p,q)=|p−q|.

A more complicated formula, giving the same value, but generalizing more readily to higher dimensions, is:

d(p,q)=(p−q)2.

In this formula, squaring and then taking the square root leaves any positive number unchanged, but replaces any negative number by its absolute value.

In the Euclidean plane, let point p have Cartesian coordinates (p1,p2) and let point q have coordinates (q1,q2). Then the distance between p and q is given by:

d(p,q)=(p1−q1)2+(p2−q2)2.

This can be seen by applying the Pythagorean theorem to a right triangle with horizontal and vertical sides, having the line segment from p to q as its hypotenuse. The two squared formulas inside the square root give the areas of squares on the horizontal and vertical sides, and the outer square root converts the area of the square on the hypotenuse into the length of the hypotenuse. In terms of the Pythagorean addition operation ⊕, available in many software libraries as hypot, the same formula can be expressed as:

d(p,q)=(p1−q1)⊕(p2−q2)=𝗁𝗒𝗉𝗈𝗍(p1−q1,p2−q2).

It is also possible to compute the distance for points given by polar coordinates. If the polar coordinates of p are (r,θ) and the polar coordinates of q are (s,ψ), then their distance is given by the law of cosines:

d(p,q)=r2+s2−2rscos⁡(θ−ψ).

When p and q are expressed as complex numbers in the complex plane, the same formula for one-dimensional points expressed as real numbers can be used, although here the absolute value sign indicates the complex norm:

d(p,q)=|p−q|.

In three dimensions, for points given by their Cartesian coordinates, the distance is

d(p,q)=(p1−q1)2+(p2−q2)2+(p3−q3)2.

In general, for points given by Cartesian coordinates in n-dimensional Euclidean space, the distance is

d(p,q)=(p1−q1)2+(p2−q2)2+⋯+(pn−qn)2.

The Euclidean distance may also be expressed more compactly in terms of the Euclidean norm of the Euclidean vector difference:

d(p,q)=‖p−q‖.

For pairs of objects that are not both points, the distance can most simply be defined as the smallest distance between any two points from the two objects, although more complicated generalizations from points to sets such as Hausdorff distance are also commonly used. Formulas for computing distances between different types of objects include:

The distance from a point to a line, in the Euclidean plane

The distance from a point to a plane in three-dimensional Euclidean space

The distance between two lines in three-dimensional Euclidean space

The distance from a point to a curve can be used to define its parallel curve, another curve all of whose points have the same distance to the given curve.

The Euclidean distance is the prototypical example of the distance in a metric space, and obeys all the defining properties of a metric space:

It is symmetric, meaning that for all points p and q, d(p,q)=d(q,p). That is (unlike road distance with one-way streets) the distance between two points does not depend on which of the two points is the start and which is the destination.

It is positive, meaning that the distance between every two distinct points is a positive number, while the distance from any point to itself is zero.

It obeys the triangle inequality: for every three points p, q, and r, d(p,q)+d(q,r)≥d(p,r). Intuitively, traveling from p to r via q cannot be any shorter than traveling directly from p to r.

Another property, Ptolemy's inequality, concerns the Euclidean distances among four points p, q, r, and s. It states that

d(p,q)⋅d(r,s)+d(q,r)⋅d(p,s)≥d(p,r)⋅d(q,s).

For points in the plane, this can be rephrased as stating that for every quadrilateral, the products of opposite sides of the quadrilateral sum to at least as large a number as the product of its diagonals. However, Ptolemy's inequality applies more generally to points in Euclidean spaces of any dimension, no matter how they are arranged. For points in metric spaces that are not Euclidean spaces, this inequality may not be true. Euclidean distance geometry studies properties of Euclidean distance such as Ptolemy's inequality, and their application in testing whether given sets of distances come from points in a Euclidean space.

According to the Beckman–Quarles theorem, any transformation of the Euclidean plane or of a higher-dimensional Euclidean space that preserves unit distances must be an isometry, preserving all distances.

In many applications, and in particular when comparing distances, it may be more convenient to omit the final square root in the calculation of Euclidean distances, as the square root does not change the order (d12>d22 if and only if d1>d2). The value resulting from this omission is the square of the Euclidean distance, and is called the squared Euclidean distance. For instance, the Euclidean minimum spanning tree can be determined using only the ordering between distances, and not their numeric values. Comparing squared distances produces the same result but avoids an unnecessary square-root calculation and sidesteps issues of numerical precision. As an equation, the squared distance can be expressed as a sum of squares:

d2(p,q)=(p1−q1)2+(p2−q2)2+⋯+(pn−qn)2.

Source: https://en.wikipedia.org/wiki/Euclidean_distance (Wikipedia, CC BY-SA 4.0)
