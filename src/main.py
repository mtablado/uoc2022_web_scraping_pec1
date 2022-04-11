from web_download import selenium_download
from scrap import scrap

FILENAME = "dataset.csv"

def create_csv_file(filename):
    # Overwrite to the specified file.
    # Create it if it does not exist.
    header_line = "time;place;depth;magnitude"
    file = open("../csv/" + filename, "w")
    file.write(header_line)
    file.write("\n")


def append_csv(filename, data):
    # Overwrite to the specified file.
    # Create it if it does not exist.
    file = open("../csv/" + filename, "a")

    # Dump all the data with CSV format
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (j == len(data[i])-1):
                file.write(data[i][j])
            else:
                file.write(data[i][j] + ";")
        file.write("\n")

def main():
    create_csv_file(FILENAME)
    data = []
    pages = 20
    for page in range(1, pages):
        html = selenium_download(page)
        subset = scrap(html)
        print(len(subset))
        print(subset)
        append_csv(FILENAME, subset)
        data.append(subset)

if __name__ == "__main__":
    main()