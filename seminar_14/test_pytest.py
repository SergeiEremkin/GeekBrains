import string
import pytest


def remove_chars(text: str) -> str:
    alpha = string.ascii_letters + ' '
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


def test_remove_chars_no_change():
    assert remove_chars('dddddd dddd') == 'dddddd dddd'


def test_remove_chars_lower():
    assert remove_chars('AAA AA') == 'aaa aa'


def test_remove_chars_remove_chars():
    assert remove_chars('a,a,n: v.v;') == 'aan vv'


def test_remove_chars_remove_rus_alpha():
    assert remove_chars('БВАОПоаоваов') == ''


def test_remove_chars_remove_all():
    assert remove_chars('WWW,3322,ГГ:') == 'www'


if __name__ == '__main__':
    pytest.main(['-v'])
