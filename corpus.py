import os
# to interact with operating system


def tokenize(text):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in text:
        if ele in punc:
            text = text.replace(ele, "")
        # to edit the text avoiding punctuation signs
    text_lower = text.lower()
    # to turn all the text in lowercase
    return text_lower.split()
    # to return the text as a list of tokens


def read_file(path):
    file_in_path = open(path, 'r', errors='replace')
    # to open and read the file at the given path avoiding a possible UnicodeDecodeError
    tokenized_email = []
    for line in file_in_path:
        lines_as_lists = line.split()
        # to create a list of strings for every line in file
        if lines_as_lists[0] != 'Subject:':
            lines_as_lists = tokenize(line)
            # to tokenize all the lines in the file avoiding the subject line
            tokenized_email.extend(lines_as_lists)
            # to obtain a list containing all tokens in the file (avoiding subject line)
    return tokenized_email


def read_dataset(path):
    top_directory = path
    ham_directory = top_directory + '/ham'
    # ham directory path
    spam_directory = top_directory + '/spam'
    # spam directory path
    training_instances = []
    for email in os.listdir(ham_directory):
        email_path = os.path.join(ham_directory, email)
        # to store the path to the e-mail file
        tokenized_email = read_file(email_path)
        # to read the e-mail and return the tokenized version
        classification_tuple = tuple((tokenized_email, 'ham'))
        # to store a tuple consisting of the tokenized e-mail and the label 'ham'
        training_instances.append(classification_tuple)
        # to append every classification tuple to the list 'training_instances'
    for email in os.listdir(spam_directory):
        email_path = os.path.join(spam_directory, email)
        # to store the path to the e-mail file
        tokenized_email = read_file(email_path)
        # to read the e-mail and return the tokenized version
        classification_tuple = tuple((tokenized_email, 'spam'))
        # to store a tuple consisting of the tokenized e-mail and the label 'spam'
        training_instances.append(classification_tuple)
        # to append every classification tuple to the list 'training_instances'
    return training_instances
