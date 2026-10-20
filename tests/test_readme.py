"""Guard the examples in README.rst.

Two issues filed against this package were caused by examples in the README
that do not parse: ``create_flat_referral.send(sender=User, request, user)``
is a SyntaxError, because Python does not allow positional arguments after a
keyword argument. Users copied it and hit the same error.
"""

import ast
import re

from django.test import SimpleTestCase

README = 'README.rst'

CODE_BLOCK = re.compile(
    r'\.\. code-block:: python\n\n((?:(?:    .*)?\n)+)'
)


class TestReadmeExamples(SimpleTestCase):

    def test_python_blocks_parse(self):
        with open(README) as f:
            readme = f.read()

        blocks = CODE_BLOCK.findall(readme)
        self.assertTrue(blocks, 'no python code blocks found in the README')

        for index, block in enumerate(blocks, 1):
            code = '\n'.join(line[4:] for line in block.split('\n'))
            with self.subTest(block=index):
                ast.parse(code)

    def test_signal_examples_use_keyword_arguments(self):
        """``sender`` is a keyword argument, so the rest must be too."""
        with open(README) as f:
            readme = f.read()

        for match in re.finditer(r'\.send\(([^)]*)\)', readme):
            arguments = match.group(1)
            self.assertNotIn(
                ', request,',
                arguments,
                'positional arguments after a keyword argument: .send({})'.format(
                    arguments
                )
            )
