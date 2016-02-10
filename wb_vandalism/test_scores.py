"""
Tests a model by generating a set of scores and outputting probabilities.

Usage:
    test_scores <model-file>
                [--verbose]
                [--debug]

Options:
    -h --help     Prints this documentation
    <model-file>  The path to a model file to load.
"""
import logging
import sys

import docopt
from revscoring import ScorerModel

import mysqltsv

logger = logging.getLogger(__name__)


def main():
    args = docopt.docopt(__doc__)

    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )
    logger.setLevel(logging.DEBUG if args['--debug'] else logging.INFO)

    model = ScorerModel.load(open(args['<model-file>'], 'rb'))

    types = [int] + list(feature_types(model.features)) + \
            [lambda v: v == "True"]
    input_values = mysqltsv.Reader(sys.stdin, headers=False, types=types)
    input_values = (list(iv) for iv in input_values)

    rev_feature_labels = ((iv[0], iv[1:-1], iv[-1]) for iv in input_values)

    verbose = args['--verbose']

    run(model, rev_feature_labels, verbose)


def feature_types(features):
    for feature in features:
        if feature.returns == bool:
            yield lambda v:v == "True"
        else:
            yield feature.returns


def run(model, rev_feature_labels, verbose):

    output = mysqltsv.Writer(sys.stdout, headers=["rev_id", "score"])

    for rev_id, feature_values, label in rev_feature_labels:
        score = model.score(feature_values)
        true_proba = score['probability'][True]

        output.write([rev_id, true_proba])

if __name__ == "__main__":
    main()
