#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    #they were lying! this does not work with replace! or at leat not well 
    #DUE TO CASE SENSITIVITY

    #needs to be private (for some reason)
    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

        self.__keywords.sort(key = len, reverse = True)


    def filter(self, msg):

        #need to make it a temp since you would be chaning words which arent profane
        #by making them lowercase which is not ideal
        msg_temp = msg.lower()

        #loop through each keyword and for each one create a clean version
        for keyword in self.__keywords:

            keyword = keyword.lower()
            clean = ''
            ind = 0

            #create clean version of profane word
            for i in range(len(keyword)):
                if ind == len(self.__template): ind = 0

                clean += self.__template[ind]
                ind += 1
            
            #as long as there is still a profane word in the message
            #you must change the msg and temp message so the while loop can be broken
            #and so you actually also get the "cleaned" message
            while keyword in msg_temp:

                index = msg_temp.find(keyword)

                msg_temp = "".join([msg_temp[:index], clean, msg_temp[index + len(keyword):]])
                msg = "".join([msg[:index], clean, msg[index + len(keyword):]])

            
        return msg      


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi Mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
