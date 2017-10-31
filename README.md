# AppHaste

AppHaste is a web portal that aggregates and filters jobs and internships that are relevant to users

It uses Selenium to parse a csv of job links and goes through each one. AppHaste takes advantage of the good UX of boards such as Greenhouse and Jobvite.

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

