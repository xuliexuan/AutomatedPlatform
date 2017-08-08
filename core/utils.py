#!/usr/bin/env python
# -*- coding:utf-8 -*-

def to_mg(value):
    """
    Convert a given value in mmol/L to mg/dL rounded to nearest integer.
    """
    try:
        return int(round((float(value) * 18.018), 0))
    except ValueError:
        # We're catching ValueError here as some browsers like Firefox won't
        # validate the input for us. We're returning the value entered as this
        # will be passed in to the Django validator which will return the
        # validation error message.
        return value