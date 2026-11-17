# Large language model

A large language model (LLM) is a machine learning model (typically a neural network) trained on a vast amount of text for natural language processing tasks, especially language generation. LLMs can typically generate, summarize, translate, and analyze text in many contexts. They are the basis for many modern chatbots, such as ChatGPT, Claude, Vibe, Gemini, Grok, Qwen and DeepSeek.

LLMs are typically based on the transformer neural network architecture. Generative pre-trained transformers (GPTs) are a type of LLM that is pre-trained to predict the next word. GPTs are then often fine-tuned to follow instructions and to behave as assistants.

Biased or inaccurate training data can make an LLM's output less reliable. A software harness can provide LLMs with memory and access to tools such as web search. Benchmark evaluations for LLMs attempt to measure model reasoning, factual accuracy, alignment, and safety.

Before the emergence of transformer-based models in 2017, some language models were considered large relative to the computational and data constraints of their time. In the early 1990s, IBM's statistical models pioneered word alignment techniques for machine translation, laying the groundwork for corpus-based language modeling. In 2001, a smoothed n-gram model, such as those employing Kneser–Ney smoothing, trained on 300 million words, achieved state-of-the-art perplexity on benchmark tests. During the 2000s, with the rise of widespread internet access, researchers began compiling massive text datasets from the web ("web as corpus") to train statistical language models.

Moving beyond n-gram models, researchers started in 2000 to use neural networks as language models. Following the breakthrough of deep neural networks in image classification around 2012, similar architectures were adapted for language tasks. This shift was marked by the development of word embeddings (e.g., Word2Vec by Mikolov in 2013) and sequence-to-sequence (seq2seq) models using LSTM. In 2016, Google transitioned its translation service to neural machine translation (NMT), replacing statistical phrase-based models with deep recurrent neural networks. These early NMT systems used LSTM-based encoder-decoder architectures, as they preceded the invention of transformers.

At the 2017 NeurIPS conference, Google researchers introduced the transformer architecture in their landmark paper "Attention Is All You Need". This paper's goal was to improve upon 2014 seq2seq technology, and was based mainly on the attention mechanism developed by Bahdanau et al. in 2014. The following year in 2018, BERT was introduced and quickly became "ubiquitous". Though the original transformer has both encoder and decoder blocks, BERT is an encoder-only model. Academic and research usage of BERT began to decline in 2023, following rapid improvements in the abilities of decoder-only models (such as GPT) to solve tasks via prompting.

Although decoder-only GPT-1 was introduced in 2018, it was GPT-2 in 2019 that caught widespread attention because OpenAI claimed to have initially deemed it too powerful to release publicly, out of fear of malicious use. GPT-3 in 2020 went a step further and as of 2025 is available only via API with no offering of downloading the model to execute locally. But it was the consumer-facing chatbot ChatGPT in late 2022 that received extensive media coverage and public attention by 2023. The 2023 GPT-4 was praised for its increased accuracy and as a "holy grail" for its multimodal capabilities. OpenAI did not reveal the high-level architecture and the number of parameters of GPT-4. The release of ChatGPT led to an uptick in LLM usage across several research subfields of computer science, including robotics, software engineering, and societal impact work. In 2024, OpenAI released the reasoning model OpenAI o1, which generates long chains of thought before returning a final answer. Many LLMs with parameter counts comparable to those of OpenAI's GPT series have been developed.

Since 2022, open-source models (those with their source code and weights made publicly available) have been gaining popularity, especially at first with BLOOM and LLaMA, though both have restrictions on the field of use. Mistral AI's open-weight models Mistral 7B and Mixtral 8x7B have a more permissive Apache License. In January 2025, DeepSeek released DeepSeek R1, a 671-billion-parameter open-weight model that performs comparably to OpenAI o1 but at a much lower price per token for users.

Since 2023, many LLMs have been trained to be multimodal, having the ability to also process or generate other types of data, such as images, audio, or 3D meshes.

Open-weight LLMs have become more influential since 2023. Per Vake et al. (2025), community-driven contributions to open-weight models improve their efficiency and performance via collaborative platforms such as Hugging Face.

There is no standard for naming large language models, but certain conventions are common. Usually, a model has a name with several parts, such as in "Qwen3-235B-A22B-Thinking-2507". The commonly used parts are:

Model family name. For example: Llama, Kimi, GPT, Gemma.

Some models are derived from a more famous model family. These may be named somewhat idiosyncratically. For example, the Alpaca series was named so because they were derived from the Llama series.

Version number. If the model family has several releases, a version number may be added. Like software versioning, it can have several parts (semantic versioning). For example, in DeepSeek-V4.1-Flash-1017, "DeepSeek" is the model family name, "Flash" is the relative size, "V4" is the major version number, ".1" is the minor version number, and "1017" is a patch version number meaning "released on 2026-10-17".

Training stage: A model released straight out of pretraining is marked "Base". A model finetuned to follow instructions is marked "Instruct", "Chat", or "it" (instruction-tuned). A model finetuned generically is marked "SFT". Similarly for "RLHF" (reinforcement learning from human feedback) or "DPO" (direct preference optimization). For example, Mistral-7B-Instruct-v0.2, Llama-2-7b-chat, Gemma-2-9b-it.

Parameter count. This is usually written as nM (n-million), nB (n-billion), or nT (n-trillion). For mixture-of-expert models, there is an optional count for active parameters. For example, "GLM-5.3-Flash (320B-A18B)" is a model with 320 billion parameters, of which 18 billion are active per forward pass.

Relative size. When the members of a model family are not named by their precise parameter counts, their relative sizes might still be named. A commonly used series: Tiny, Small, Base, Big, Large, Huge. For example, the original BERT series included "Tiny", "Base", and "Large". Proprietary model families may use idiosyncratic names for the relative sizes for branding purposes, such as Haiku/Sonnet/Opus (from the Claude series), and Terra/Luna/Sol (from the GPT series).

Source: https://en.wikipedia.org/wiki/Large_language_model (Wikipedia, CC BY-SA 4.0)
