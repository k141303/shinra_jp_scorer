import argparse

from scoring import get_score

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shinra scoring program')
    parser.add_argument('answer', help='Answer path')
    parser.add_argument('result', help='System result path')
    parser.add_argument('--html', help='Html folder path')
    parser.add_argument('--text', help='Plane text folder path')
    parser.add_argument('--target', help='Scoring target id path')
    parser.add_argument('--error', help='Error log output path')
    parser.add_argument('--score', help='Score output path')


    args = parser.parse_args()

    get_score(args.answer, args.result, target = args.target, html_path = args.html, plain_path = args.text, error_path = args.error, score_path = args.score)
