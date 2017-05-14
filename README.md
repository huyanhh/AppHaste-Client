# mesos-scraper

## `keywords.txt`

text file of possible keywords, in the format `keyword : question`

## `questions.txt`

text file of questions, where each word is an id that represents a
question that will be asked on the application process

---
these files together represent a graph (reversed n-ary tree) that will
be used to look up the applicant's answer to the generalized question

```
keyword1 -->

keyword2 --> question1 --> answer

keyword3 -->
```

