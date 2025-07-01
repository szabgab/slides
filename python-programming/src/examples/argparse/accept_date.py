import argparse
import datetime

def vali_date(text: str) -> datetime.datetime:
    #return datetime.datetime.strptime(text, "%Y-%m-%d")
    try:
        return datetime.datetime.strptime(text, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"This {text!r} is not a valid date.")

parser = argparse.ArgumentParser()
parser.add_argument(
        "--date",
        help = "Date in format YYYY-MM-DD",
        required = True,
        type = vali_date
)

args = parser.parse_args()
print(args.date)
