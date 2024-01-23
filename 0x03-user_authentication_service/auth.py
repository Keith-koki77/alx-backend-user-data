#!/usr/bin/env python3
"""
Script for auth
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    hash password that uses bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
