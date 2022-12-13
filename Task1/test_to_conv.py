import unittest


class MyTestCase(unittest.TestCase):
    prog_data = "# title BIGTITLE\n# author memyselfandi\n# description some code description"
    title = 'Test'
    description = 'Code things'
    source_code = "print('hello world')"

    def test_prepare_md_titles(self):
        expected = ('BIGTITLE', 'Code things')
        self.assertEqual(md.prepare_md_titles(self.prog_data), expected)

    def test_prepare_md_format(self):
        test = md.prepare_md_format(self.title, self.description, self.source_code)
        expected = ('+ [Test](#test-prog)\n',
                    "## Test\nCode things\n    \n```python\nprint('hello world')\n```")
        self.assertEquals(test, expected)


if __name__ == '__main__':
    unittest.main()
