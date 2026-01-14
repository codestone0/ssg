import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("<a>", "forgotten bones", [], {'href':'http://www.dec.com','target':'_self'})
        self.assertEqual(node.props_to_html(), ' href="http://www.dec.com" target="_self"')

        

if __name__ == "__main__":
    unittest.main()