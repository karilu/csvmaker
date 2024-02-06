import csv

source = "epistolary.txt"
destination = "epistolary.csv"

sourceFile = open(source, "r")
destinationFile = open(destination, "w", newline='')
csvwriter = csv.writer(destinationFile)
rows = []
for item in sourceFile:
    if item != "" and item != "\n":
        date = "n/a"
        s  = item.find('[') + 1
        e = item.find(']')
        if (s > 0 and e > 0):
            date = item[s:e]
            item = item[:s-1] + item[e + 1:]
        row  = item.strip().split(" by ")
        row.insert(0, date)
        if len(row) > 1:
            rows.append(row)

csvwriter.writerow(["date","title", "author", "ignore"])
csvwriter.writerows(rows);

sourceFile.close()
destinationFile.close()