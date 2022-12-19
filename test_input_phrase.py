import requests
import pytest


class TestInputPrhase:
    def test_phrase_len(self):
        phrase = input("Enter a phrase with len = 15 or less: ")
        assert len(phrase) <= 15, f"Prhase len more than 15"