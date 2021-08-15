import re

def memeified(message):
    """
    Returns True for strings that have been meme-ified, or contain a capital letter followed
    by a lowercase letter followed by another capital letter. Returns False for non-meme-ified strings.

    >>> memeified("PyThon dOeSn'T sUpPort TaIl reCuRsiOn.")
    True
    >>> memeified("The above statement is false! Python doesn't support TCO")
    False
    >>> memeified("LoL this is fun")
    True
    >>> memeified("lOl this is fun")
    False
    >>> memeified("I WrIte My ScHeMe wItH StYlE - (CoNs '61 (cOnS 'A NiL))")
    True
    >>> memeified("I take my scheme very seriously and only use lowercase")
    False
    """
    return bool(re.search(r"[A-Z][a-z][A-Z]", message))



def greetings(message):
    """
    Returns whether a string is a greeting. Greetings begin with either Hi, Hello, or
    Hey (either capitalized or lowercase), and/or end with Bye (either capitalized or lowercase) optionally followed by
    an exclamation point or period.

    >>> greetings("Hi! Let's talk about our favorite submissions to the Scheme Art Contest")
    True
    >>> greetings("Hey I just figured out that when I type the Konami Code into cs61a.org, something fun happens")
    True
    >>> greetings("I'm going to watch the sun set from the top of the Campanile! Bye!")
    True
    >>> greetings("Bye Bye Birdie is one of my favorite musicals.")
    False
    >>> greetings("High in the hills of Berkeley lived a legendary creature. His name was Oski")
    False
    >>> greetings('Hi!')
    True
    >>> greetings("bye")
    True
    """
    return bool(re.search(r"(^([Hh](i|ey|ello))\b)|(([Bb]ye[!\.]?)$)", message))



def email_validator(email, domains):
    """
    >>> email_validator("oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@gmail.com", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@berkeley.com", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeley.edu", ["yahoo.com"])
    False
    >>> email_validator("xX123_iii_OSKI_iii_123Xx@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeleysedu", ["berkeley.edu", "gmail.com"])
    False
    """
    pattern = r"^\w+@[a-z0-9]+\.[a-z]{3}"
    for domain in domains[:]:
        if domain not in email:
            domains.remove(domain)
    if not domains:
        return False
    return bool(re.search(pattern, email))


