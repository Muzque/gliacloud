def find_number(limit):
    r_list = list()
    for n in range(1, limit):
        if n%3 == 0:
            r_list.append(n)
        elif n%5 == 0:
            r_list.append(n)
    return sum(r_list)


def main():
    a = find_number(100)
    print(a)


if __name__ == "__main__":
    main()
