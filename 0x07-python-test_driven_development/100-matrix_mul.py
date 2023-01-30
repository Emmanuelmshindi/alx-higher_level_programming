#!/usr/bin/python3
""" Defines a matrix multiplication function """

def matrix_mul(m_a, m_b):
    """ Multiply two matrices.

    Args:
        m_a: first matrix
        m_b: second matrix
    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        ValueError: if m_a or m_b is empty (it means: = [] or = [[]])
        TypeError: if one element list of lists is not an integer or a float
        TypeError: if m_a or m_b is not a rectangle 
        ValueError: If m_a and m_b can’t be multiplied
    """
    if m_a == [] or m_a == [[]]
        raise ValueError
