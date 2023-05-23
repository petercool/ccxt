import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-


from ccxt.test.base import test_borrow_rate  # noqa E402


def test_fetch_borrow_rate(exchange, skipped_properties, code):
    method = 'fetchBorrowRate'
    borrow_rate = None
    try:
        borrow_rate = exchange.fetch_borrow_rate(code)
    except Exception as ex:
        message = str(ex)
        # for exchanges, atm, we don't have the correct lists of currencies, which currency is borrowable and which not. So, because of our predetermined list of test-currencies, some of them might not be borrowable, and thus throws exception. However, we shouldn't break tests for that specific exceptions, and skip those occasions.
        if message.find('could not find the borrow rate for currency code') < 0:
            raise Error(message)
        # console.log (method + '() : ' + code + ' is not borrowable for this exchange. Skipping the test method.');
        return
    test_borrow_rate(exchange, skipped_properties, method, borrow_rate, code)
