import nltk

txt = "Hello, it's me. I was wondering" \
      "if after all these years. You'd like"
txt
sentences = nltk.tokenize.sent_tokenize(txt)
sentences
