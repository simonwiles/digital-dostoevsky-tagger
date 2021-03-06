import re


def markup_proper_names(text, names, tag):

    re_proper_names = re.compile(
        rf"\b(?:{'|'.join(sorted(names, key=len, reverse=True))})\b"
    )
    text = re_proper_names.sub(rf"<{tag}>\g<0></{tag}>", text)

    return text
