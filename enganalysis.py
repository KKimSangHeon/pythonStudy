import nltk
txt = "Hello, it's me. I was wondering "
print(txt)

sentences = nltk.tokenize.sent_tokenize(txt)
print(sentences)

tokens = [nltk.tokenize.sent_tokenize(sen) for sen in sentences]
print(tokens)

pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
print(pos_tagged_tokens)