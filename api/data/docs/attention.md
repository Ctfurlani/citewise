# Attention (machine learning)

In machine learning, attention is a method that determines the importance of, or "attends to", each component in a sequence relative to the other components in that sequence. In natural language processing, importance is represented by weights assigned to each word in a sentence. More generally, attention encodes vectors called token embeddings across a fixed-width sequence that can range from tens to millions of tokens in size.

Earlier designs implemented the attention mechanism in a serial recurrent neural network (RNN) language translation system, but a more recent design, namely the transformer, removed the slower sequential RNN and relied more heavily on the faster parallel attention scheme, which has largely replaced RNN in frontier models since BERT, T5 and GPT.

Inspired by ideas about attention in humans, the attention mechanism was developed to address the weaknesses of using information from the hidden layers of recurrent neural networks. Recurrent neural networks favor information contained in words at the end of a sentence and thus deemed more recent, thereby tending to attenuate the significance and associated predictive weight assigned to information earlier in the sentence. Attention allows a token equal access to any part of a sentence directly, rather than only through the previous state.

Academic reviews of the history of the attention mechanism are provided in Niu et al. and Soydaner.

Selective attention in humans had been well studied in neuroscience and cognitive psychology. In 1953, Colin Cherry studied selective attention in the context of audition, known as the cocktail party effect.

In 1958, Donald Broadbent proposed the filter model of attention. Selective attention of vision was studied in the 1960s by George Sperling's partial report paradigm. It was also noticed that saccade control is modulated by cognitive processes, insofar as the eye moves preferentially towards areas of high salience. As the fovea of the eye is small, the eye cannot sharply resolve the entire visual field at once. The use of saccade control allows the eye to quickly scan important features of a scene.

These research developments inspired algorithms such as the Neocognitron and its variants. Meanwhile, developments in neural networks had inspired circuit models of biological visual attention. One well-cited network from 1998, for example, was inspired by the low-level primate visual system. It produced saliency maps of images using handcrafted (not learned) features, which were then used to guide a second neural network in processing patches of the image in order of reducing saliency.

A key aspect of attention mechanism can be written (schematically) as ∑i⟨(query)i,(key)i⟩(value)iwhere the angled brackets denote dot product. This shows that it involves a multiplicative operation. Multiplicative operations within artificial neural networks had been studied under the names of higher-order neural networks, multiplication units, sigma-pi units, fast weight controllers, and hyper-networks.

In fast weight controller, one of its two networks has  "fast weights" or "dynamic links" (1981). A slow neural network learns by gradient descent to generate keys and values for computing the weight changes of the fast neural network which computes answers to queries. This is dot-product attention without softmax.

During the deep learning era, attention mechanism was developed to solve similar problems in encoding-decoding.

In machine translation, the seq2seq model, as it was proposed in 2014, would encode an input text into a fixed-length vector, which would then be decoded into an output text. If the input text is long, the fixed-length vector would be unable to carry enough information for accurate decoding. An attention mechanism was proposed to solve this problem.

An image captioning model was proposed in 2015, citing inspiration from the seq2seq model. that would encode an input image into a fixed-length vector. (Xu et al 2015), citing (Bahdanau et al 2014), applied the attention mechanism as used in the seq2seq model to image captioning.

One problem with seq2seq models was their use of recurrent neural networks, which are not parallelizable as both the encoder and the decoder must process the sequence token-by-token. Decomposable attention attempted to solve this problem by processing the input sequence in parallel, before computing a "soft alignment matrix" (alignment is the terminology used by Bahdanau et al) in order to allow for parallel processing.

The idea of using the attention mechanism for self-attention, instead of in an encoder-decoder (cross-attention), was also proposed during this period, such as in differentiable neural computers and neural Turing machines. It was termed intra-attention where an LSTM is augmented with a memory network as it encodes an input sequence.

These strands of development were brought together in 2017 with the Transformer architecture, published in the Attention Is All You Need paper.

Given three matrices: Q∈ℝm×dQ,K∈ℝn×dK and V∈ℝn×dV, the scaled dot-product attention is defined as:Attention(Q,K,V)=softmax(λQKT)V∈ℝm×dvwhere T denotes transpose and the softmax function is applied independently to every row of its argument. λ is a scalar. It is usually set to 1/dK.

The matrix Q contains m queries, while matrices K,V jointly contain n key-value pairs. Value vectors in matrix V are weighted using the weights resulting from the softmax operation, so that the rows of the m-by-dv output matrix are confined to the convex hull of the points in ℝdv given by the rows of V.

Attention mechanism without positional encoding is permutation-invariant.

For decoder self-attention, all-to-all attention is inappropriate, because during the autoregressive decoding process, the decoder cannot attend to future outputs that have yet to be decoded. This can be solved by forcing the attention weights wij=0 for all i<j, called "causal masking". This attention mechanism is the "causally masked self-attention".

Formally,Attention(Q,K,V)=softmax(QKTdk+M)VwhereM=[0−∞−∞…−∞00−∞…−∞000…−∞⋮⋮⋮⋱⋮000…0]The effect of adding −∞ is to zero out the corresponding attention weight, after applying the softmax.

Other forms of masking are possible, to enforce different types of attention weight patterns.

Several dot-product attention mechanisms can be combined, resulting in the Multi-Head Attention (MHA):MultiHead(Q,K,V)=Concat(head1,...,headh)WOwhere each head is computed with QKV attention as:headi=Attention(QWiQ,KWiK,VWiV)and WiQ,WiK,WiV, and WO are learnable matrices.

Self-attention is essentially the same as cross-attention, except that query, key, and value vectors all come from the same model. Both encoder and decoder can use self-attention, but with subtle differences.

For encoder self-attention, we can start with a simple encoder without self-attention, such as an "embedding layer", which simply converts each input word into a vector by a fixed lookup table. This gives a sequence of hidden vectors h0,h1,…. These can then be applied to a dot-product attention mechanism, to obtainh0′=Attention(h0WQ,HWK,HWV)h1′=Attention(h1WQ,HWK,HWV)⋮or more succinctly, H′=Attention(HWQ,HWK,HWV). This can be applied repeatedly, to obtain a multilayered encoder. This is the "encoder self-attention", sometimes called the "all-to-all attention", as the vector at every position can attend to every other.

Source: https://en.wikipedia.org/wiki/Attention_%28machine_learning%29 (Wikipedia, CC BY-SA 4.0)
