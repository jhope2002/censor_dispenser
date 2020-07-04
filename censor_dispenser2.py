# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

phrases_to_censor = ['learning algorithms', "she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself", "Helena", "out of control"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

punctuation = ['.', ',', '!', ":", ";", "\""]

def censor_email(email_to_censor, phrases=None, words=None):

    def create_censor_bar(phrase):
        censor_bar_list = ['X' for character in phrase]        
        if phrase[-2] in punctuation:
            censor_bar_list[-2:] = phrase[-2:]
        else:
            censor_bar_list[-1] = phrase[-1]
        censor_bar = ''.join(censor_bar_list)        
        return censor_bar    

    def find_possible(word_list=None):
        if word_list:
            possible_words = []
            for word in word_list:            
                possible_words.append(word + " ")
                word_upper = word[0].upper() + word[1:]
                possible_words.append(word_upper + " ")
                for character in punctuation:
                    possible_words.append(word + character + " ")
                    possible_words.append(word + character)  
                    possible_words.append(word_upper + character + " ")
                    possible_words.append(word_upper + character)             
            possible_words.sort(key = len, reverse = True)    
            return possible_words
        else:
            return None

    censored_email = email_to_censor
    split_email = email_to_censor.split()  
    #print(split_email)
    possible_phrases = find_possible(phrases)    
    possible_words = find_possible(words)   
    #print(possible_words)
        
    if possible_phrases:      
        for phrase in possible_phrases:        
            if phrase in censored_email:                            
                censor_bar = create_censor_bar(phrase)
                censored_email = censored_email.replace(phrase, censor_bar)

    if possible_words:        
        counter = 0        
        for word in possible_words:
            if word in censored_email:
                counter += 1
                #print("Negative word found!  >> " + word)
                #print("Counter is now >> " + str(counter))
                if counter > 2:
                    censor_bar = create_censor_bar(word)
                    censored_email = censored_email.replace(word, censor_bar)       
    
    return censored_email
    

#email_one_censored = censor_email(email_one, phrases=phrases_to_censor)
#print(eamil_one)
#print(email_one_censored)

#email_two_censored = censor_email(email_two, phrases=phrases_to_censor)
#print(email_two)
#print(email_two_censored)

#email_three_censored = censor_email(email_three, phrases=phrases_to_censor, words=negative_words)
#print(email_three)
#print(email_three_censored)






