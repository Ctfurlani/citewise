# Long short-term memory

Long short-term memory (LSTM) is a type of recurrent neural network (RNN) aimed at mitigating the vanishing gradient problem commonly encountered by traditional RNNs. Its relative insensitivity to gap length is its advantage over other RNNs, hidden Markov models, and other sequence learning methods. It aims to provide a short-term memory for RNN that can last thousands of timesteps (thus "long short-term memory"). The name is made in analogy with long-term memory and short-term memory and their relationship, studied by cognitive psychologists since the early 20th century.

An LSTM unit is typically composed of a cell and three gates: a forget gate, an input gate and an output gate. The cell remembers values over arbitrary time intervals, and the gates regulate the flow of information into and out of the cell. Forget gates decide what information to discard from the previous state, by mapping the previous state and the current input to a value between 0 and 1. A (rounded) value of 1 signifies retention of the information, and a value of 0 represents discarding. Input gates decide which pieces of new information to store in the current cell state, using the same system as forget gates. Output gates control which pieces of information in the current cell state to output, by assigning a value from 0 to 1 to the information, considering the previous and current states. Selectively outputting relevant information from the current state allows the LSTM network to maintain useful, long-term dependencies to make predictions, both in current and future time-steps.

LSTM has wide applications in classification, data processing, time series analysis tasks, speech recognition,  machine translation, speech activity detection, robot control, video games, healthcare, energy forecasting.

In theory, classic RNNs can keep track of arbitrary long-term dependencies in the input sequences. The problem with classic RNNs is computational (or practical) in nature: when training a classic RNN using back-propagation, the long-term gradients which are back-propagated can "vanish", meaning they can tend to zero due to very small numbers creeping into the computations, causing the model to effectively stop learning. RNNs using LSTM units partially solve the vanishing gradient problem, because LSTM units allow gradients to also flow with little to no attenuation. However, LSTM networks can still suffer from the exploding gradient problem.

The intuition behind the LSTM architecture is to create an additional module in a neural network that learns when to remember and when to forget pertinent information. In other words, the network effectively learns which information might be needed later on in a sequence and when that information is no longer needed. For instance, in the context of natural language processing, the network can learn grammatical dependencies. An LSTM might process the sentence "Dave, as a result of his controversial claims, is now a pariah" by remembering the (statistically likely) grammatical gender and number of the subject Dave. Note that this information is pertinent for the pronoun his and note that this information is no longer important after the verb is.

In the equations below, the lowercase variables represent vectors. Matrices Wq and Uq contain, respectively, the weights of the input and recurrent connections, where the subscript q can either be the input gate i, output gate o, the forget gate f or the memory cell c, depending on the activation being calculated. In this section, we are thus using a "vector notation". So, for example, ct∈ℝh is not just one unit of one LSTM cell, but contains h LSTM cell's units.

The compact forms of the equations for the forward pass of an LSTM cell with a forget gate are:

ft=σg(Wfxt+Ufht−1+bf)it=σg(Wixt+Uiht−1+bi)ot=σg(Woxt+Uoht−1+bo)c~t=σc(Wcxt+Ucht−1+bc)ct=ft⊙ct−1+it⊙c~tht=ot⊙σh(ct)

where the initial values are c0=0 and h0=0 and the operator ⊙ denotes the Hadamard product (element-wise product). The subscript t indexes the time step.

Letting the superscripts d and h refer to the number of input features and number of hidden units, respectively:

xt∈ℝd: input vector to the LSTM unit

ft∈(0,1)h: forget gate's activation vector

it∈(0,1)h: input/update gate's activation vector

ot∈(0,1)h: output gate's activation vector

ht∈(−1,1)h: hidden state vector also known as output vector of the LSTM unit

c~t∈(−1,1)h: cell input activation vector

ct∈ℝh: cell state vector

W∈ℝh×d, U∈ℝh×h and b∈ℝh: weight matrices and bias vector parameters which need to be learned during training

σg: sigmoid function.

σc: hyperbolic tangent function.

σh: hyperbolic tangent function or, as the peephole LSTM paper suggests, σh(x)=x.

The figure on the right is a graphical representation of an LSTM unit with peephole connections (i.e. a peephole LSTM). Peephole connections allow the gates to access the constant error carousel (CEC), whose activation is the cell state. ht−1 is not used, ct−1 is used instead in most places.

ft=σg(Wfxt+Ufct−1+bf)it=σg(Wixt+Uict−1+bi)ot=σg(Woxt+Uoct−1+bo)ct=ft⊙ct−1+it⊙σc(Wcxt+bc)ht=ot⊙σh(ct)

Each of the gates can be thought as a "standard" neuron in a feed-forward (or multi-layer) neural network: that is, they compute an activation (using an activation function) of a weighted sum. it,ot and ft represent the activations of respectively the input, output and forget gates, at time step t.

The 3 exit arrows from the memory cell c to the 3 gates i,o and f represent the peephole connections. These peephole connections actually denote the contributions of the activation of the memory cell c at time step t−1, i.e. the contribution of ct−1 (and not ct, as the picture may suggest). In other words, the gates i,o and f calculate their activations at time step t (i.e., respectively, it,ot and ft) also considering the activation of the memory cell c at time step t−1, i.e. ct−1.

The single left-to-right arrow exiting the memory cell is not a peephole connection and denotes ct.

The little circles containing a × symbol represent an element-wise multiplication between its inputs. The big circles containing an S-like curve represent the application of a differentiable function (like the sigmoid function) to a weighted sum.

Peephole convolutional LSTM. The ∗ denotes the convolution operator.

ft=σg(Wf∗xt+Uf∗ht−1+Vf⊙ct−1+bf)it=σg(Wi∗xt+Ui∗ht−1+Vi⊙ct−1+bi)ct=ft⊙ct−1+it⊙σc(Wc∗xt+Uc∗ht−1+bc)ot=σg(Wo∗xt+Uo∗ht−1+Vo⊙ct+bo)ht=ot⊙σh(ct)

An RNN using LSTM units can be trained in a supervised fashion on a set of training sequences, using an optimization algorithm like gradient descent combined with backpropagation through time to compute the gradients needed during the optimization process, in order to change each weight of the LSTM network in proportion to the derivative of the error (at the output layer of the LSTM network) with respect to corresponding weight.

A problem with using gradient descent for standard RNNs is that error gradients vanish exponentially quickly with the size of the time lag between important events. This is due to limn→∞Wn=0 if the spectral radius of W is smaller than 1.

Source: https://en.wikipedia.org/wiki/Long_short-term_memory (Wikipedia, CC BY-SA 4.0)
