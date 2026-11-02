import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(
        description="DSA Problem Runner"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument(
        "problem",
        help="Problem module, e.g. arrays.two_sum"
    )

    args = parser.parse_args()

    if args.command == "run":
        module_name = f"dsa.problems.{args.problem}"

        try:
            module = importlib.import_module(module_name)
            module.main()
        except ModuleNotFoundError as e:
            parser.error(f"Problem not found: {args.problem}")
        except AttributeError:
            parser.error(f"Problem {args.problem} does not implement main()")


# Needed for executing two_sum.py directly with below command
# python src/dsa/problems/arrays/two_sum.py
if __name__ == "__main__":
    main()