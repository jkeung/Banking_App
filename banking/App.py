#!/usr/bin/env python
from __future__ import absolute_import
from banking.Menu import Menu

def main():
    """Engine to run bank app.
    Args:
        None
    """

    app = Menu()
    app.run()

if __name__ == "__main__":
    main()
