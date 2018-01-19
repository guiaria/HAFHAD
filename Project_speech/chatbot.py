# Sentences we'll respond with if the user greeted us
COMMAND_KEYWORDS = ("ทำ","เปิด","ปิด","ตรวจ","เช็ค")


#GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_command(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in COMMAND_KEYWORDS:
            return command_respond(sentence)
        elif word.lower() in QUESTION_KEYWORDS:
            return question_respond(sentence)

def command_respond(sentence):
    for word in sentence.words:
        if "ไฟ" in word :
            """ เช็คว่าคำสั่งประเภทไหน"""
    pass

def question_respond(sentence):
    """ เอาคำถามไปกูเกิ้ล"""
    pass



