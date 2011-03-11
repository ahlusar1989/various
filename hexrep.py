def main(filename, old, new):
    file = open(filename, 'rb')
    buf = file.read().replace(old, new)
    file.close()
    file = open(filename, 'wb')
    file.write(buf)
    file.close()
        
if __name__ == '__main__':
    import sys
    try:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception, e:
        print '%s:%s' %(e.__class__.__name__, e)
        raise SystemExit, """
    Usage: [python] hexrep.py filename replacethat withthis
    """