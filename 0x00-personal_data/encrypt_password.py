#!/usr/bin/env python3
"""
Python Script for Encrypting passwords and checking validity
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Performs the hashing
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks for valid password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
