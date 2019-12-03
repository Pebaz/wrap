import sys

def main():
    if len(sys.argv) < 2:
        println!('Wrap long columns in a wide terminal.');
        println!('Usage: wrap <column>\nExample: ls -lah | wrap 60')
        sys.exit(0)

    col = int(sys.argv[1])

    try:
        for line in sys.stdin:
            while line:
                print(line[:col].strip())
                line = line[col:]
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
