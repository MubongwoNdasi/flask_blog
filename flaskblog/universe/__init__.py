from spacy.matcher import PhraseMatcher
from spacy import displacy
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokens import Span
import string


# from flaskblog.universe.utils import CleanDoc
from flaskblog.universe.data_dictionary import data_dictionary, pipeline_dict, pipes, TABLE_NAMES, DATE_RANGES


# load the spacy object
nlp = spacy.load("en_core_web_sm")

# removing all existing pipe names


def clear_pipes():
    for pipe in nlp.pipe_names:
        nlp.remove_pipe(pipe)


class CleanDoc:
    # Function to remove duplicates from list object
    def remove_dup(self, list_obj):
        results = []
        for word in list_obj:
            if word not in results:
                results.append(word)
        return results

    # Stop words dictionary
    def stop_dic(self):
        stop_list = list(STOP_WORDS)

        stop_list_remove = []
        data_dic = data_dictionary()
        for a, b in data_dic.items():
            stop_list_remove += b

        new_list = []

        for word in stop_list_remove:
            reg = word.split()
            new_list += reg

        new_list = self.remove_dup(new_list)

        for word in new_list:
            try:
                stop_list.remove(word)
            except ValueError:
                pass
        return stop_list

    # Function that cleans up the spacy doc object

    def clean_doc(self, doc):
        new_sent = []
        stop_words = self.stop_dic()

        # Tokenization
        for word in doc:
            new_sent.append(word.text)
        new_sent = " ".join(i for i in new_sent)

        # remove punctuations
        punctuation = string.punctuation
        new_sent = new_sent.lower()

        new_str = ""
        for x in new_sent:
            if x not in punctuation:
                new_str += x

        # remove stop words
        new_str = new_str.split()

        for i in new_str:
            if i in stop_words:
                new_str.remove(i)

        # remove repeated words
        new_str = self.remove_dup(new_str)
        new_str = " ".join(i for i in new_str)

        new_sent = nlp(new_str)

        # lemmatization
        lemma = []
        for word in new_sent:
            if word.pos_ != 'PRON':
                lemma.append(word.lemma_)
        new_str = " ".join(i for i in lemma)

        # clean doc
        new_doc = nlp(new_str)

        return new_doc


# this is the matcher class

class EntityMatcher(object):
    # name = "entity_matcher"

    def __init__(self, nlp, terms, label):
        patterns = [nlp.make_doc(text) for text in terms]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(label, None, *patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            span = Span(doc, start, end, label=match_id)
            doc.ents = list(doc.ents) + [span]
        return doc

# define our matcher objects and create pipeline


def matcher_obj():
    clear_pipes()
    for key, pipe in enumerate(pipes()):
        data = data_dictionary()
        data = data.get(pipe)
        pipe_name = pipeline_dict()
        pipe_name = pipe_name.get(pipe)
        matcher = EntityMatcher(nlp, data, pipe_name)
        nlp.add_pipe(matcher, name=pipe_name)


matcher_obj()


# outputs the various entities
def get_query_params(doc):
    clean_obj = CleanDoc()
    doc = clean_obj.clean_doc(doc)
    params = {'table_name': '', 'date_range': ''}
    table_name = TABLE_NAMES()
    date_range_list = DATE_RANGES()
    error = 0

    for word in doc.ents:
        for i in table_name:
            if word.label_ == i:
                params['table_name'] = word.label_
                error += 1

            else:
                pass

        for j in date_range_list:
            if word.label_ == j:
                params['date_range'] = word.label_

    if error != 0:
        return params

    elif error == 0:
        error = {'table_name': 'Error', 'result': "Invalid query"}
        return error
    else:
        pass
