# Name: ...
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    practice_graph.add_edge("C", "F")
    practice_graph.add_edge("F", "D")
    practice_graph.add_edge("D", "C")
    practice_graph.add_edge("D", "B")
    practice_graph.add_edge("D", "E")

    return practice_graph


# def draw_practice_graph(graph):
#     """Draw practice_graph to the screen.
#     """
#     nx.draw_networkx(graph)
#     plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()

    rj.add_edge("Nurse", "Juliet")
    rj.add_edge("Juliet", "Tybalt")
    rj.add_edges_from([("Juliet", "Capulet"), ("Tybalt", "Capulet")])
    rj.add_edges_from([("Juliet", "Friar Laurence"), ("Juliet", "Romeo"),
                       ("Romeo", "Friar Laurence")])
    rj.add_edges_from([("Romeo", "Benvolio"), ("Romeo", "Montague"),
                       ("Benvolio", "Montague")])
    rj.add_edges_from([("Capulet", "Paris"), ("Paris", "Escalus"),
                       ("Capulet", "Escalus")])
    rj.add_edges_from([("Paris", "Mercutio"), ("Escalus", "Mercutio")])
    rj.add_edges_from([("Mercutio", "Romeo"), ("Escalus", "Montague")])

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    assert user in graph.nodes()

    result = set()
    people = graph.nodes()
    for person1 in people:
        for person2 in people:
            # the () around the whole condition are necessary to
            # break the condition over multiple lines
            if (graph.has_edge(person1, person2) and
                graph.has_edge(person2, user) and
                not graph.has_edge(person1, user) and
                    person1 != user):
                result.add(person1)
    return result


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    if user1 not in graph or user2 not in graph:
        return set()
    
    friends1 = set(graph[user1])
    friends2 = set(graph[user2])
    
    return friends1.intersection(friends2)


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    if user not in graph:
        return {}

    user_friends = set(graph[user])
    common_friends_map = {}

    for person in graph:
        if person == user or person in user_friends:
            continue

        person_friends = set(graph[person])
        common_friends = person_friends.intersection(user_friends)

        if len(common_friends) > 0:
            common_friends_map[person] = len(common_friends)

    return common_friends_map


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    def sort_key(k):
        return (-map_with_number_vals[k], k)

    sorted_keys = sorted(map_with_number_vals.keys(), key=sort_key)

    return sorted_keys


def rec_number_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """



###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    pass


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    pass


###
#  Problem 5
###

def get_facebook_graph():
    """Builds and returns the facebook graph
    """

    # (Your Problem 5 code goes here.)
    pass


def main():
    # practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_practice_graph(practice_graph)

    # rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

    # (Your Problem 4 code goes here.)

    ###
    #  Problem 5
    ###

    # (Your Problem 5 code goes here. Make sure to call get_facebook_graph.)

    # assert len(facebook.nodes()) == 63731
    # assert len(facebook.edges()) == 817090

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    # (Your Problem 6 code goes here.)

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    # (Your Problem 7 code goes here.)

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    # (Your Problem 8 code goes here.)


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
