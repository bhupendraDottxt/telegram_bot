

def sample_responses(input_text):

    user_message = str(input_text).lower()

    if user_message == "#help":
        m="""Please use following commands to get the info:
        /syllabus
        /contacts
        /schedule
        /classlink
        /ebooks
        /test"""
        return m
    #return input_text
    return ""
