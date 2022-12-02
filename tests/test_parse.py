"""unit tests for get_images.parse_html()"""

from get_images import parse_html


def test_single_link():
    html = """
    <html><body><img src="/test.png"></body></html>
    """
    assert parse_html(html) == ["/test.png"]

def test_multi_links():
    html = """
    <html><body><img src="http://example.com/test1.png"><img src="http://example.com/test2.png"></body></html>
    """
    assert set(parse_html(html)) == {"http://example.com/test1.png", "http://example.com/test2.png"}

def test_mixed_formats():
    html = """
    <html><body><img src="http://example.com/test1.png"><img src="http://example.com/test1.gif"></body></html>
    """
    assert parse_html(html) == ["http://example.com/test1.png"]

def test_multi_links_same_src():
    html = """
    <html><body><img src="http://example.com/test1.png"><img src="http://example.com/test1.png"></body></html>
    """
    assert parse_html(html) == ["http://example.com/test1.png"]

def test_http_params():
    html = """
    <html><body><img src="/test.png?size=big"></body></html>
    """
    assert parse_html(html) == ["/test.png?size=big"]

def test_empty_ref():
    html = """
    <html><body><img src=""></body></html>
    """
    assert parse_html(html) == []

def test_wrong_tag():
    html = """
    <html><body><embed type="image/png" src="test.png"</embed></body></html>
    """
    assert parse_html(html) == []

def test_commented_out_tag():
    html = """
    <html><body><!--<img src="test.png"</img>--></body></html>
    """
    assert parse_html(html) == []
