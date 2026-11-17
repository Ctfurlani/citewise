# Dot product

In mathematics, the dot product is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors), and returns a single number. In Euclidean geometry, the scalar product of two vectors is the dot product of their Cartesian coordinates, and is independent from the choice of a particular Cartesian coordinate system. The terms "dot product" and "scalar product" are often used interchangeably when a Cartesian coordinate system has been fixed once for all. The scalar product being a particular inner product, the term "inner product" is also often used.

Algebraically, the dot product is the sum of the products of the corresponding entries of the two sequences of numbers. Geometrically, the scalar product of two vectors is the product of their lengths and the cosine of the angle between them. These definitions are equivalent when using Cartesian coordinates. In modern geometry, Euclidean spaces are often defined by using vector spaces. In this case, the scalar product is used for defining lengths (the length of a vector is the square root of the scalar product of the vector by itself) and angles (the cosine of the angle between two vectors is the quotient of their scalar product by the product of their lengths).

The name "dot product" is derived from the dot operator " ⋅ " that is often used to designate this operation; the alternative name "scalar product" emphasizes that the result is a scalar, rather than a vector (as with the vector product in three-dimensional space).

The dot product may be defined algebraically or geometrically. The geometric definition is based on the notions of angle and distance (magnitude) of vectors. The equivalence of these two definitions relies on having a Cartesian coordinate system for Euclidean space.

In modern presentations of Euclidean geometry, the points of space are defined in terms of their Cartesian coordinates, and Euclidean space itself is commonly identified with the real coordinate space 𝐑n. In such a presentation, the notions of length and angle are defined by means of the dot product. The length of a vector is defined as the square root of the dot product of the vector by itself, and the cosine of the (non oriented) angle between two vectors of length one is defined as their dot product. So the equivalence of the two definitions of the dot product is a part of the equivalence of the classical and the modern formulations of Euclidean geometry.

The dot product of two vectors 𝐚=[a1,a2,⋯,an] and 𝐛=[b1,b2,⋯,bn], specified with respect to an orthonormal basis, is defined, in summation notation, as:

𝐚⋅𝐛=∑i=1naibi=a1b1+a2b2+⋯+anbn

where n is the dimension of the vector space. For instance, in three-dimensional space, the dot product of vectors [1,3,−5] and [4,−2,−1] is:

[1,3,−5]⋅[4,−2,−1]=(1×4)+(3×−2)+(−5×−1)=4−6+5=3

If vectors are identified with column vectors, the dot product can also be written as a matrix product

𝐚⋅𝐛=𝐚𝖳𝐛,

where 𝐚𝖳 denotes the transpose of 𝐚.

Expressing the above example in this way, a 1 × 3 matrix (row vector) is multiplied by a 3 × 1 matrix (column vector) to get a 1 × 1 matrix that is identified with its unique entry:

[13−5][4−2−1]=[3]

Likewise, the dot product of the vector [1,3,−5] with itself is:

[1,3,−5]⋅[1,3,−5]=(1×1)+(3×3)+(−5×−5)=1+9+25=35

In Euclidean space, a Euclidean vector is a geometric object that possesses both a magnitude and a direction. A vector can be pictured as an arrow. Its magnitude is its length, and its direction is the direction to which the arrow points. The magnitude of a vector 𝐚 is denoted by ‖𝐚‖. The dot product of two Euclidean vectors 𝐚 and 𝐛 is defined by

𝐚⋅𝐛=‖𝐚‖‖𝐛‖cos⁡θ,

where θ is the angle between 𝐚 and 𝐛.

In particular, if the vectors 𝐚 and 𝐛 are orthogonal (i.e., their angle is π2 or 90∘), then cos⁡π2=0, which implies that

𝐚⋅𝐛=0.

At the other extreme, if they are codirectional, then the angle between them is zero with cos⁡0=1 and

𝐚⋅𝐛=‖𝐚‖‖𝐛‖

This implies that the dot product of a vector 𝐚 with itself is

𝐚⋅𝐚=‖𝐚‖2,

which gives

‖𝐚‖=𝐚⋅𝐚,

the formula for the Euclidean length of the vector.

The scalar projection (or scalar component) of a Euclidean vector 𝐚 in the direction of a Euclidean vector 𝐛 is given by

ab=‖𝐚‖cos⁡θ,

where θ is the angle between 𝐚 and 𝐛.

In terms of the geometric definition of the dot product, this can be rewritten as

ab=𝐚⋅𝐛^,

where 𝐛^=𝐛/‖𝐛‖ is the unit vector in the direction of 𝐛.

The dot product is thus characterized geometrically by

𝐚⋅𝐛=ab‖𝐛‖=ba‖𝐚‖.

The dot product, defined in this manner, is homogeneous under scaling in each variable, meaning that for any scalar α,

(α𝐚)⋅𝐛=α(𝐚⋅𝐛)=𝐚⋅(α𝐛).

It also satisfies the distributive law, meaning that

𝐚⋅(𝐛+𝐜)=𝐚⋅𝐛+𝐚⋅𝐜.

These properties may be summarized by saying that the dot product is a bilinear form. Moreover, this bilinear form is positive definite, which means that 𝐚⋅𝐚 is never negative, and is zero if and only if 𝐚=𝟎, the zero vector.

If 𝐞1,⋯,𝐞n are the standard basis vectors in 𝐑n, then we may write

𝐚=[a1,…,an]=∑iai𝐞i𝐛=[b1,…,bn]=∑ibi𝐞i.

The vectors 𝐞i are an orthonormal basis, which means that they have unit length and are at right angles to each other. Since these vectors have unit length,

𝐞i⋅𝐞i=1

and since they form right angles with each other, if i≠j,

𝐞i⋅𝐞j=0.

Thus in general, we can say that:

𝐞i⋅𝐞j=δij,

where δij is the Kronecker delta.

Also, by the geometric definition, for any vector 𝐞i and a vector 𝐚, we note that

𝐚⋅𝐞i=‖𝐚‖‖𝐞i‖cos⁡θi=‖𝐚‖cos⁡θi=ai,

where ai is the component of vector 𝐚 in the direction of 𝐞i. The last step in the equality can be seen from the figure.

Now applying the distributivity of the geometric version of the dot product gives

𝐚⋅𝐛=𝐚⋅∑ibi𝐞i=∑ibi(𝐚⋅𝐞i)=∑ibiai=∑iaibi,

which is precisely the algebraic definition of the dot product. So the geometric dot product equals the algebraic dot product.

The dot product fulfills the following properties if 𝐚, 𝐛, 𝐜 and 𝐝 are real vectors and α, β, γ and δ are scalars.

Commutative

𝐚⋅𝐛=𝐛⋅𝐚, which follows from the definition (θ is the angle between 𝐚 and 𝐛): 𝐚⋅𝐛=‖𝐚‖‖𝐛‖cos⁡θ=‖𝐛‖‖𝐚‖cos⁡θ=𝐛⋅𝐚. The commutative property can also be easily proven with the algebraic definition, and in more general spaces (where the notion of angle might not be geometrically intuitive but an analogous product can be defined) the angle between two vectors can be defined as

θ=arccos⁡(𝐚⋅𝐛‖𝐚‖‖𝐛‖).

Bilinear (additive, distributive and scalar-multiplicative in both arguments)

(α𝐚+β𝐛)⋅(γ𝐜+δ𝐝)=αγ(𝐚⋅𝐜)+αδ(𝐚⋅𝐝)+βγ(𝐛⋅𝐜)+βδ(𝐛⋅𝐝).

Not associative

Because the dot product is not defined between a scalar 𝐚⋅𝐛 and a vector 𝐜, associativity is meaningless. However, bilinearity implies c(𝐚⋅𝐛)=(c𝐚)⋅𝐛=𝐚⋅(c𝐛). This property is sometimes called the "associative law for scalar and dot product", and one may say that "the dot product is associative with respect to scalar multiplication".

Source: https://en.wikipedia.org/wiki/Dot_product (Wikipedia, CC BY-SA 4.0)
