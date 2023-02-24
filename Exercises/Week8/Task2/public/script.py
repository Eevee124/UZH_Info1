#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    #getter methods created to access the private attributes from our classes constructor
    #needed because the exercise dictates it...

    def get_authors(self):
        authors = []
        for author in self.__authors:
            authors.append(author)
        return sorted(authors)
    
    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year
    
    #the following three methods don't use the getter methods
    #since get_authors passes an ordered list and this can differ if you compare strings with one another

    def __str__(self):
        repr =  f"Publication({str(self.__authors)}, \"{self.get_title()}\", {self.get_year()})"

        return repr.replace("'", "\"")

    def __repr__(self):
        repr = f"Publication({str(self.__authors)}, \"{self.get_title()}\", {self.get_year()})"
        return repr.replace("'", "\"")

    def __hash__(self):
        return hash((tuple(self.__authors), self.get_title(), self.get_year()))

    #the rest of these comparisons first check if the compared to is an isntance of publication
    #then they get compared with one another using the getter methods

    #==
    def __eq__(self, other):
        if isinstance(other, Publication):
            return self.get_authors() == other.get_authors() and self.get_title() == other.get_title() and self.get_year() == other.get_year()
        
        else: return NotImplemented
    
    #!=
    def __ne__(self, other):
        if isinstance(other, Publication):
            return not (self.get_authors() == other.get_authors() and self.get_title() == other.get_title() and self.get_year() == other.get_year())
        
        else: return NotImplemented

    #<
    def __lt__(self, other):
        if isinstance(other, Publication):
            if self.get_authors() == other.get_authors():
                if self.get_title() == other.get_title():
                    return self.get_year() < other.get_year()

                else: return self.get_title() < other.get_title()
            else: return self.get_authors() < other.get_authors()
        
        else: return NotImplemented

    #<=
    def __le__(self, other):
        if isinstance(other, Publication):
            if self.get_authors() == other.get_authors():
                if self.get_title() == other.get_title():
                    return self.get_year() <= other.get_year()

                else: return self.get_title() <= other.get_title()
            else: return self.get_authors() <= other.get_authors()
        
        else: return NotImplemented
    #>
    def __gt__(self, other):
        if isinstance(other, Publication):
            if self.get_authors() == other.get_authors():
                if self.get_title() == other.get_title():
                    return self.get_year() > other.get_year()

                else: return self.get_title() > other.get_title()
            else: return self.get_authors() > other.get_authors()
        
        else: return NotImplemented

    #>=
    def __ge__(self, other):
        if isinstance(other, Publication):
            if self.get_authors() == other.get_authors():
                if self.get_title() == other.get_title():
                    return self.get_year() >= other.get_year()

                else: return self.get_title() >= other.get_title()
            else: return self.get_authors() >= other.get_authors()
        
        else: return NotImplemented






    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False
    print(hash(p1) == hash(p2)) #True
    print(hash(p1) == hash(p3)) #False

    sales = {
        p1: 273,
        p2: 398,
    }

    print(sales.values())
    print(p1 > p2) #False
    print(p2 < p3) #True
    print(p1 <= p3) #True
