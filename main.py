with open("./forrasfajl.txt", "r", encoding="utf-8") as forrasfajl, \
    open("./forrasfajl_copy.txt", 'w', encoding='utf-8') as celfajl:
        
        for line in forrasfajl:
            data = line.strip().split(";")
            date = data[0]
            language = data[1]

            print(date, language, file=celfajl)