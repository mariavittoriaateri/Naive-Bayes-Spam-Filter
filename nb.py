import numpy as np


class SpamFilter:
    def __init__(self):
        self.p_word_given_ham = {}  # P(w | 'ham')
        self.p_word_given_spam = {}  # P(w | 'spam')

    def train(self, emails):
        ham_word_count = {}
        spam_word_count = {}
        for labeled_email in emails:
            # to iterate through every training instance (= tokenized e-mail with correct label)
            words = labeled_email[0]
            label = labeled_email[1]
            if label == 'ham':
                # this way it will go through the training instances that have the label 'ham'
                for word in words:
                    try:
                        ham_word_count[word] += 1
                    except KeyError:
                        ham_word_count[word] = 1
                        # if word is not contained in ham_word_count, we initialize it
                    if word not in spam_word_count:
                        spam_word_count[word] = 1
                        # if word never appears in spam_word_count, we make it seen nevertheless (Laplacian smoothing)
            elif label == 'spam':
                # this way it will go through the training instances that have the label 'spam'
                for word in words:
                    try:
                        spam_word_count[word] += 1
                    except KeyError:
                        spam_word_count[word] = 1
                        # if word is not contained in spam_word_count, we initialize it
                    if word not in ham_word_count:
                        ham_word_count[word] = 1
                        # if word never appears in ham_word_count, we make it seen nevertheless (Laplacian smoothing)
        for key in ham_word_count:
            # it iterates through every key (= word) present in ham_word_count
            self.p_word_given_ham[key] = ham_word_count[key] / (ham_word_count[key] + spam_word_count[key])
            # this formula computes the probability that the word appears in a ham e-mail
        for key in spam_word_count:
            # it iterates through every key (= word) present in spam_word_count
            self.p_word_given_spam[key] = spam_word_count[key] / (ham_word_count[key] + spam_word_count[key])
            # this formula computes the probability that the word appears in a spam e-mail

    def classify(self, email):
        probs = []  # to store the spam scores of every word
        probs_one_minus = []  # to store the counter spam probability of every word
        for word in email:
            try:
                p_spam_given_word = self.p_word_given_spam[word] / (self.p_word_given_ham[word] +
                                                                    self.p_word_given_spam[word])
                # computes the probability of spam given the word
                probs.append(p_spam_given_word)
                probs_one_minus.append(1-p_spam_given_word)
            except KeyError:
                pass
                # KeyError appears if the word was not contained in the training database; we ignore the word
        multiplied_prob = np.prod(probs) / (np.prod(probs) + np.prod(probs_one_minus))
        # this formula computes the overall probability that the input e-mail is spam
        if multiplied_prob > 0.5:
            return multiplied_prob, 'spam'
            # over the threshold of 0.5 (50% probability), the e-mail is classified as spam
        elif multiplied_prob < 0.5:
            return multiplied_prob, 'ham'
            # under the threshold of 0.5 (50% probability), the e-mail is classified as ham
        else:
            return 0.51, 'spam'
            # in cases such as multiplied_prob == nan (not a number), the e-mail is classified as spam by default
