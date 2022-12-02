from get_images import UrlWithAuth
import pytest
import re

def test_auth_scope():
        auth_scope = re.sub(r'/([^/]*)$', '/', "http://example.com/a/b/image.png")
        assert auth_scope == "http://example.com/a/b/"

@pytest.mark.parametrize(
    ('src', 'result_url', 'result_userpass'),
    (
        # URLs inside the authentication scope (according to https://datatracker.ietf.org/doc/html/rfc7617)
        ("image.png", "http://example.com/a/b/image.png", "user:passwd"),
        ("c/image.png", "http://example.com/a/b/c/image.png", "user:passwd"),
        # URLs outside the authentication scope 
        ("https://example.com/a/b/image.png", "https://example.com/a/b/image.png", ""),
        ("../image.png", "http://example.com/a/image.png", ""),
        ("/image.png", "http://example.com/image.png", ""),
        ("http://example.com/image.png", "http://example.com/image.png", ""),
        ("http://other.example.com/image.png", "http://other.example.com/image.png", "")
    )
)
def test_construct_url(src, result_url, result_userpass):
    url = UrlWithAuth(url="http://example.com/a/b/c.html?param1=val1&param2=val2#ancor", userpass="user:passwd")
    assert url.construct_url(src).url == result_url
    assert url.construct_url(src).userpass == result_userpass

def test_url_no_auth():
    url = UrlWithAuth(url="http://example.com/index.html")
    assert url.request.headers.get('Authorization') is None

def test_url_with_auth():
    url = UrlWithAuth(url="http://example.com/index.html", userpass="user:passwd")
    assert url.request.headers.get('Authorization') == "Basic dXNlcjpwYXNzd2Q="
