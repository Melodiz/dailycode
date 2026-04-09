Here is the translated document in Markdown format:

# [cite_start]SELECTED TOPICS IN AI [cite: 3]
## HOMEWORK | [cite_start]WEEK 8 [cite: 4, 5]

[cite_start]**CENTRAL UNIVERSITY** [cite: 1]
[cite_start]*Discovering the carry propagation* [cite: 2]

[cite_start]In this homework assignment, you will be asked to discover elements of the carry propagation circuit in pre-trained models. [cite: 6] [cite_start]You will need to prepare a report addressing the posed question and describe the work done, what succeeded, and what did not. [cite: 7]

---

### [cite_start]SETUP [cite: 8]

[cite_start]When adding numbers, the value of an individual digit can exceed the base of the numeral system, and then the higher-order digit is incremented by one. [cite: 9] [cite_start]This is exactly carry propagation: [cite: 10]

[cite_start]$$\begin{aligned}18+28=1.0^{+}+8.10^{+}+210^{+}\\ =(1+2\cdot10^{+}+(5+10^{+}+10^{+}\\ =3.10^{+}+10^{+}+10^{+}\\ =(8+1)+10^{+}+2\cdot10^{+}\\ =(8+1)+10^{+}+2\cdot10^{+}\\ =(8+1)+2\cdot10^{+}\end{aligned}$$ [cite: 11]

[cite_start]An autoregressive model predicts the digits of the answer from left to right, from the highest order to the lowest. [cite: 12] [cite_start]During the generation of each token, it must perform carry propagation in advance, sometimes for many tokens in a row. [cite: 13] [cite_start]What mechanism inside the model allows it to do this? [cite: 14] [cite_start]Can it be identified? [cite: 14]

#### [cite_start]Calculating Mediator Significance [cite: 15]

[cite_start]The following method for calculating the indirect effect is often used in the literature; for simplicity, we will rely on the formulation from the paper "Arithmetic Without Algorithms". [cite: 16] [cite_start]Let $p$ and $p^{\prime}$ be prompts of the form "$a+b=$", and let $r$ be the correct answers for these prompts. [cite: 17] [cite_start]Let's run the model on both prompts and save the activations of its elements in memory. [cite: 18] [cite_start]Then the mediator's contribution will be calculated as follows: [cite: 19]

[cite_start]$$IE=\frac{1}{2}(\frac{\mathbb{P}^{*}(r\prime)-\mathbb{P}(r\prime)}{\mathbb{P}(r\prime)}+\frac{\mathbb{P}(r)-\mathbb{P}^{*}(r)}{\mathbb{P}^{*}(r)})$$ [cite: 20]

[cite_start]where $\mathbb{P}$ is the probability of the answer when running the model with prompt $p$, and $\mathbb{P}^{*}$ denotes the probabilities calculated in a run with intervention: activations for the run on prompt $p$ are replaced with activations calculated on prompt $p^{\prime}$ (i.e., noising is performed), $p^{\prime}\rightarrow p$. [cite: 21] [cite_start]Instead of probabilities, logits at the model output can be used. [cite: 22]

---

### [cite_start]ASSIGNMENT [cite: 25]

[cite_start]It is necessary to analyze a trained transformer to determine where it is localized and whether there is a mechanism dedicated to carry propagation. [cite: 26]

* [cite_start]Take any pre-trained model capable of performing addition with sufficient quality, otherwise you will be studying noise instead of mechanisms. [cite: 32] [cite_start]You can also train your own small transformer-calculator, which will give you more freedom. [cite: 33] [cite_start]Pay attention to the tokenizer: some models encode multi-digit numbers as a single token (for example, GPT-2 encodes numbers 0-512 this way), while others encode numbers character by character. [cite: 34] [cite_start]This strongly affects what the mechanism will look like. [cite: 35]
* [cite_start]Select a dataset, a method for generating counterfactual prompts, and an intervention procedure that will allow you to isolate individual features of this mechanism. [cite: 36] [cite_start]How will the noising and denoising scenarios differ? [cite: 37]
* [cite_start]Determine which components and paths in the model are important for performing carry propagation: choose an acceptable granularity of analysis (entire Attn/MLP modules, individual heads/neurons, SAE features, etc.), then calculate the importance of the components and paths you are interested in. [cite: 38] [cite_start]You can use various circuit discovery methods; choose the one that seems most understandable for analysis to you. [cite: 39]
* [cite_start]Evaluate the necessity and sufficiency of the identified components and paths for executing carry propagation. [cite: 40] [cite_start]Identify the role of the discovered elements. [cite: 40] [cite_start]Check if there are any paths (e.g., compensatory ones) that participate in this procedure and were not detected during the first pass. [cite: 41]
* [cite_start]Draw conclusions: can the circuit be localized, or is it distributed throughout the entire model, or is it completely absent, and carry propagation is an effect of something less interesting? [cite: 42]

[cite_start]There is no need to do all the work of identifying the circuit; what is important is not the final result, but the research process and the ability to formulate hypotheses and experiments to test them. [cite: 43, 44, 45] [cite_start]Focus on conducting a detailed analysis and identifying the mechanisms that allow the model to produce the correct answer, or finding out that they do not exist (the model may rely on heuristics; this is also a good result). [cite: 46] [cite_start]Ideally, disabling the found circuit should lead to errors on examples with carry propagation, but there should be no drop in quality on other examples. [cite: 47]

[cite_start]You can use any libraries that seem necessary to you (except for those that implement automatic circuit discovery; use them only to validate your observations and assess whether you are moving in the right direction). [cite: 48] [cite_start]For interventions, you can use pyvene and transformer-lens. [cite: 49]

[cite_start]Draw inspiration from the following papers: [cite: 50]
* [cite_start]Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics; [cite: 51]
* [cite_start]A Mechanistic Interpretation of Arithmetic Reasoning in Language Models using Causal Mediation Analysis; [cite: 52]
* [cite_start]Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small; [cite: 53]
* [cite_start]Towards Best Practices of Activation Patching in Language Models: Metrics and Methods; [cite: 54]
* [cite_start]Interpreting and Improving Large Language Models in Arithmetic Calculation; [cite: 55]
* [cite_start]How to use and interpret activation patching; [cite: 58]
* [cite_start]Understanding Addition in Transformers. [cite: 59]

[cite_start]You can rely on the methodology described in the "Arithmetic Without Algorithms" paper. [cite: 60] [cite_start]The main difference will be the dataset (counterfactual pairs). [cite: 60] [cite_start]Optionally, you can work with other mechanisms and potential circuits if you can characterize them clearly and in detail. [cite: 61] [cite_start]Be sure to include this in the report along with the motivation. [cite: 62]

---

### [cite_start]EVALUATION CRITERIA [cite: 63]

[cite_start]To receive a passing grade, you must provide a structured description of the search procedure for the carry propagation circuit (or another chosen circuit). [cite: 64] [cite_start]It is necessary to describe the model being analyzed, the experimental setup used for the analysis, hypotheses, and the method of testing them, as well as neatly present the experimental results (graphs, tables). [cite: 65] [cite_start]Formulate conclusions from each experiment and the analysis as a whole. [cite: 66] [cite_start]Describe the found mechanisms and the role of the identified components (if possible)—what exactly do they do to solve the task? [cite: 66]