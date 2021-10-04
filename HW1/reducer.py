#!/usr/bin/python
import sys


def main() -> None:
    # input comes from STDIN
    mj = None
    cj = None
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        try:
            ck, mk = map(float, line.split(' '))
        except ValueError:
            continue
        # parse the input we got from mapper.py
        if mj is None or cj is None:
            mj, cj = mk, ck
        else:
            mi = (cj * mj + ck * mk) / (cj + ck)
            ci = ck + cj
            print(f"{ci} {mi}")
            mj = mi
            cj = ci


if __name__ == "__main__":
    main()

