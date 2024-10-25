
"""
Student information for this assignment:

Replace <Saisrikar Kichili> with your name.
On my/our honor, <Saisrikar Kichili> and <Anika Koppula>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: srk2749
UT EID 2: ark3398
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"

class LinkedList:
    """class defining LinkedList"""
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, exp):
        """function defining how to insert term"""
        if coeff == 0:
            return
        new_node = Node(coeff, exp)
        if self.head is None or exp > self.head.exp:
            new_node.next = self.head
            self.head = new_node
            return
        present = self.head
        past = None
        while present and present.exp >= exp:
            if present.exp == exp:
                present.coeff += coeff
                if present.coeff == 0:
                    if past is None:
                        self.head = present.next
                    else:
                        past.next = present.next
                return
            past = present
            present = present.next
        new_node.next = present
        if past:
            past.next = new_node

    def add(self, p):
        """function defining how to add"""
        final = LinkedList()
        present = self.head
        while present:
            final.insert_term(present.coeff, present.exp)
            present = present.next
        present = p.head
        while present:
            final.insert_term(present.coeff, present.exp)
            present = present.next
        return final

    def mult(self, p):
        """function defining how to multiply"""
        final = LinkedList()
        present = self.head
        while present:
            now = p.head
            while now:
                coeff = present.coeff * now.coeff
                exp = present.exp + now.exp
                final.insert_term(coeff, exp)
                now = now.next
            present = present.next
        return final

    def __str__(self):
        if self.head is None:
            return ""
        represent = []
        present = self.head
        while present:
            represent.append(str(present))
            present = present.next
        return " + ".join(represent)


def main():
    """function defining how to make the outputs"""
    everything = []
    while True:
        each = input().strip()
        if each == "":
            break
        everything.append(each)
    a = int(everything[0])
    b = LinkedList()
    for i in range(1, a + 1):
        lists = everything[i].split()
        coeff = int(lists[0])
        exp = int(lists[1])
        b.insert_term(coeff, exp)
    c = 0
    if a + 1 < len(everything):
        c = int(everything[a+1])
    d = LinkedList()
    for i in range(a + 2, a + 2 + c):
        if i < len(everything):
            lists = everything[i].split()
            coeff = int(lists[0])
            exp = int(lists[1])
            d.insert_term(coeff, exp)
    sum_polynomial = b.add(d)
    product_polynomial = b.mult(d)
    print(sum_polynomial)
    print(product_polynomial)

if __name__ == "__main__":
    main()
