#!/usr/bin/env python3
"""Authentication module for API"""
from flask import request
import re
from typing import List, TypeVar


class Auth:
    '''auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path requires authentication"""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Gets authorization header field from request"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets current user from request"""
        return None


    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None

        SESSION_NAME = os.getenv("SESSION_NAME")

        cookie = request.cookies.get(SESSION_NAME)

        return cookie
