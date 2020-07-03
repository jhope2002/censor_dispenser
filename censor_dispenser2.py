# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

phrases_to_censor = ['learning algorithms']

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

punctuation = ['.', '!', ":", ";", "\""]

def censor_email(email_to_censor, phrases=None, terms=None):

    def create_censor_bar(phrase):
        censor_bar_list = ['X' for character in phrase]        
        if phrase[-2] in punctuation:
            censor_bar_list[-2:] = phrase[-2:]
        else:
            censor_bar_list[-1] = phrase[-1]
        censor_bar = ''.join(censor_bar_list)        
        return censor_bar    

    def find_possible(word_list):
        possible_words = []
        for word in word_list:            
            possible_words.append(word + " ")
            possible_words.append(word[0].upper() + word[1:] + " ")
            for character in punctuation:
                possible_words.append(word + character + " ")               
        possible_words.sort(key = len, reverse = True)    
        return possible_words

    censored_email = email_to_censor     
    possible_phrases = find_possible(phrases)
    for phrase in possible_phrases:
        print(phrase)      
    possible_terms = find_possible(terms)         
    for term in possible_terms:
        print(term)
    
    if possible_phrases:      
        for phrase in possible_phrases:        
            if phrase in censored_email:                            
                censor_bar = create_censor_bar(phrase)
                censored_email = censored_email.replace(phrase, censor_bar)

    if possible_terms:
        for term in possible_terms:
            if term in censored_email:                
                censor_bar = create_censor_bar(term)
                censored_email = censored_email.replace(term, censor_bar)           

    return censored_email
    

#email_one_censored = censor_email(email_one, phrases=phrases_to_censor)
#print(email_one_censored)

email_two_censored = censor_email(email_two, phrases=phrases_to_censor, terms=proprietary_terms)
print(email_two)
print(email_two_censored)





