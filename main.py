from pprint import pprint

def main():
    data = list()
    with open("ICE.txt", 'r') as ICE:
        for line in ICE.readlines():
            line_data = line.split("   ")
            line_data.pop(0)
            line_data[12] = line_data[12][:-1]
            data.append(line_data)
    for ii in data:
        print(ii)



if __name__ == '__main__':
    main()
