from dataclasses import dataclass
from typing import List, Tuple
import spacy

nlp = spacy.load("en_core_web_sm")


# mocking a simpler version of detector output
@dataclass
class AbleistLanguage:
    text: str
    start: int
    end: int


def highlight(text: str, terms_list: List[Tuple[int, int]]) -> str:
    """Return a string with highlighted phrases enclosed in <em> </em> tags.
    Parameters
    ----------
    text : str
        document
    terms_list : List[tuple[int, int]]
        list of phrases to highlight, where each element represents a phrase's spacy
        start and end token positions in the document; list must be sorted in ascending
        order of start index
    Returns
    -------
    str
        string with highlighted phrases enclosed in <em> tags
    """
    doc = nlp(text)
    result = ""
    previous_end = 0  # store end of last span
    for term_start, term_end in terms_list:
        word = doc[term_start:term_end].text
        word_id = word.replace(" ", "")
        # get the span before the first highlighted term
        if term_start > 0:
            # might need to be smarter about the whitespace padding;
            # i.e. if the original text has \n, should use that instead of space
            result += f"{doc[previous_end:term_start].text} "
        # get all highlighted terms
        
        # result += f"<em>{doc[term_start:term_end].text}</em>"
        result += f"<mark style=\"background: #FFBE2E!important\" onclick=\"myFunction('{word_id}')\">{word}</mark>"
        # if the current highlighted term is in the middle of the doc, right pad with a space
        if term_end < len(doc):
            result += " "
        previous_end = term_end
    # append remaining text at end of doc
    if len(doc) > previous_end:
        result += doc[previous_end:].text
    return result