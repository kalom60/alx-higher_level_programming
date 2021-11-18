#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    name = dir(hidden_4)
    for stings in name:
        if not stings.startswith('__'):
            print('{:s}'.format(stings))
