from .indicator import parse_indicators_file, parse_indicators_url


class TextFactory:

    def __init__(self, args):
        self.args = args

    def run_command(self):
        fang = False if self.args.defang else True
        if self.args.url:
            parse_indicators_url(self.args.url, fang)

        elif self.args.filename:
            f = self.args.filename
            text = f.read()
            parse_indicators_file(text, fang)
