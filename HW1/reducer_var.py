#!/usr/bin/python
import sys


def main() -> None:
    # input comes from STDIN
    mj = None
    cj = None
    vj = None
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        try:
            ck, mk, vk = map(float, line.split(' '))
        except ValueError:
            continue
        # parse the input we got from mapper.py
        if mj is None or cj is None:
            mj, cj, vj = mk, ck, vk
        else:
            mi = (cj * mj + ck * mk) / (cj + ck)
            vi = ((cj * vj + ck * vk) / (cj + ck)) + cj * ck * ((mj - mk) / (cj + ck)) ** 2
            ci = ck + cj
            print(f"{ci} {mi} {vi}")
            mj = mi
            cj = ci
            vj = vi


if __name__ == "__main__":
    main()

