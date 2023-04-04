# Naive-Bayes-Spam-Filter
Naive Bayes spam filter in Python (final project of the basic programming course for Computational Linguistics).

The module **corpus.py** includes:
- a *tokenize(text)* function which accepts as input a string (text) and returns a list of tokens;
- a *read_file(path)* function which accepts as input a string (path), opens the file at the specified path, and returns the file contents as a list of tokens. Each file starts with a line corresponding to the subject of the e-mail, which is discarded here;
- a *read_dataset(path)* function whcih accepts as input a string (path) which points to a dataset containing two directories, ham and spam. The function discovers all e-mail files contained in the two directories and read their contents via *read_file*. Every e-mail has to be combined into a tuble with its respective label ("ham" or "spam") to form a training instance, e.g. (["buy", "cheap", "medications"], "spam"). The function returns a list of training instances.

The module **nb.py** contains a class *SpamFilter*, which deals only with token sequences provided by corpus.py. The class has the two following methods:
- *train(self, emails)* trains the spam filter by learning the statistics of emails, where emails is a list of training instances returned by *read_dataset*;
- *classify(self, email)* classifies email (a list of tokens representing the contents of an e-mail) into spam or ham. The return value is a tuple consisting of both the spam score and the spam classification result for the email ("spam" or "ham").

The module **main.py** is responsible for user interaction - by invoking main.py, all functionality is exposed.

The whole program allows the user to train a spam filter from a dataset of e-mails, classify an e-mail as spam or ham, and batch-classify an entire dataset of e-mails.

***NOTE***: the dataset used contains two directories, ham and spam. Each e-mail file is named as numericID.ham or numericID.spam respectively.
