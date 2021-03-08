*Data Source:*

-	Webscraped  Websites for Texts related to Nature Based Solution adaptation  

Models:
Why we chose Topic Modeling - 
	Problem description was to assess the coalition websites and their respective organizations’ websites, and  uncover if and how these platforms are approaching or mentioning climate adaptation, and understand the key climate risks and adaptation measures that are present in and across these platforms.
	
  Inorder to achieve what was requested in the problem statement the data were scraped from various websites but the data collected is large and going over it manually to understand what nbs approaches would prove to be a herculean task, so we planned to use AI specifically topic modeling algorithms.
	
  Topic modelling provides us with methods to organize, understand and summarize large collections of textual information. It helps in:
	
  - Discovering hidden topical patterns that are present across the collection
	
  - Annotating documents according to these topics
	
  - Using these annotations to organize, search and summarize texts

Topic modelling can be described as a method for finding a group of words known as  topics from a collection of documents that best represents the information in the collection. It can also be thought of as a form of text mining – a way to obtain recurring patterns of words in textual material.
There are many techniques that can be used to obtain topic models, The algorithm tried here is:LDA with Gensim and Spacy.

*LDA with Gensim and Spacy*
Latent Dirichlet Allocation(LDA) is a popular algorithm for topic modeling with excellent implementations in the Python’s Gensim package.

What does LDA do?

LDA’s approach to topic modeling is it considers each document as a collection of topics in a certain proportion. And each topic as a collection of keywords, again, in a certain proportion.
Once you provide the algorithm with the number of topics, all it does is rearrange the topics distribution within the documents and keywords distribution within the topics to obtain a good composition of topic-keywords distribution.

Steps Taken :
Data was Cleaned and Tokenized. Lanuage detection, removing documents with less than 5 words, removing commonly occuring words and words with less than 3 characters.

LDA Model was fine tuned for the number of Topics. Model perplexity and topic coherence Scores: These scores are a measure to judge how good a given topic model is.

●	Topic Coherence measures score a single topic by measuring the degree of semantic similarity between high scoring words in the topic.

●	Perplexity is a statistical measure of how well a probability model predicts a sample; the statistic makes more sense when comparing it across different models with varying the number of topics. The model with the lowest perplexity is generally considered the “best”


After which visualizations were done:

1. Word Clouds from Analysis
 
2. Words and Topic Distributions

3. A t-SNE visualization of keywords/topics in the Texts.
4. 
The distance in the 3D space among points represents the closeness of keywords / topics in the URL.
The color dot represents a URL, hovering over a point provides more information about the Topics referred to in the URL.
One can further group the URL’s by the color grouping and analyze the data in greater depth.
 

A few limitations are:
  
1)	Topic modeling requires a lot of relevant data and consistent structure to be able to form clusters.
	
2)	It also needs domain expertise to interpret the results.

Future Scope: To create a front end where we can search for the keyword and relevant topics and where they were found can be visualized.
