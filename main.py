import os
from corpus import read_dataset
from corpus import read_file
from nb import SpamFilter

print('This program will allow you to discover whether an e-mail or more e-mails is/are spam or ham,'
      ' and it will also return the value of the spam probability.')
print('To start classifying your e-mail(s), write a path to a training dataset which contains '
      'a group of e-mails in a directory called \'ham\' and a group of e-mails in a directory called \'spam\':\n')
path = input()
dataset = read_dataset(path)
# the read_dataset function is called; it reads the e-mails at the given path and returns the training instances
print('\nDone reading e-mails.\nNow the training process is running.')
classifier = SpamFilter()
classifier.train(dataset)
# the train method is called; it learns the statistics given by 'dataset'
print('Done training the classifier.')
print('Now the classifier can classify any input e-mail.')
dataset_outputs = []
while True:
    # this loop allows the user to use the same session to classify several e-mails and/or databases
    print('\nType: \n Email: For classifying single email \n Database: For classifying whole email database '
          '\n Exit: for exiting the program\n')
    user_input = input()
    if user_input == 'Email':
        print('\nTo classify a single e-mail, please write the path to the desired e-mail.')
        email_to_classify = input()
        tokenized_email = read_file(email_to_classify)
        # the read_file function is called and the resulting tokenized e-mail is stored in 'tokenized_email'
        email_file_name = os.path.basename(email_to_classify)
        # this allows to store the name of the e-mail file (needed for a neat output format)
        prob_spam, label = classifier.classify(tokenized_email)
        # the classify method is called; the spam score and the label are stored in two variables
        print("\n{} {} {}".format(email_file_name, prob_spam, label) + '\n')
        # the output is printed, using the format method which inserts certain values in certain placeholders
    elif user_input == 'Database':
        print('\nTo classify a whole dataset containing e-mails in .txt format, '
              'please write the path to the desired dataset. '
              'The file returned will output a list of lines, each of which contains the e-mail file name, '
              'the spam score, and the classification as ham or spam.')
        dataset_to_classify = input()
        for email in os.listdir(dataset_to_classify):
            # it iterates through every e-mail file inside 'dataset_to_classify'
            email_path = os.path.join(dataset_to_classify, email)
            # this allows to store the name of the e-mail file (needed for a neat output format)
            tokenized_email = read_file(email_path)
            # the read_file function is called and the resulting tokenized e-mail is stored in 'tokenized_email'
            prob_spam, label = classifier.classify(tokenized_email)
            # the classify method is called; the spam score and the label are stored in two variables
            output = "{} {} {}".format(email_path, prob_spam, label)
            # the output is stored, using the format method which inserts certain values in certain placeholders
            dataset_outputs.append(output)
            # the output of every e-mail is appended inside 'dataset_outputs'
        with open('spam_filter_output_file.txt', 'a+') as f:
            # it opens a .txt file 'spam_filter_output_file.txt', which will store all the outputs of the database
            for string in dataset_outputs:
                # it iterates through every line of 'dataset_outputs'
                f.write(string)
                f.write('\n')
                # it writes the line inside the .txt file and goes to the following line
            print('You can now see the output file on your computer by opening the file named '
                  '\"spam_filter_output_file.txt\". '
                  'Note that if you wish to classify another dataset, the output will be displayed in the same '
                  'file \"spam_filter_output_file.txt\", after the last line of the previous output.')
    elif user_input == 'Exit':
        break
        # if the user types 'Exit', the loop breaks
    else:
        print('Invalid input. Please type either \"E-mail\", \"Database\", or \"Exit\".')
        # if the user types something other than 'Email', 'Database' or 'Exit', the program asks to try again
print('\nThank you for using Spam Classifier.')
# it ends the session
