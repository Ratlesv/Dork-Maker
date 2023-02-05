# read the keyword and classes from the text files
with open("keyword.txt", "r") as keyword_file:
    keywords = keyword_file.read().strip().split("\n")

with open("classes.txt", "r") as classes_file:
    classes = classes_file.read().strip().split("\n")

# generate the Google search queries for each class and keyword
queries = []
for keyword in keywords:
    for class_name in classes:
        query = f'"{keyword}" inurl:".php?{class_name}="'
        queries.append(query)

# write the queries to a text file, one query per line
with open("queries.txt", "w") as queries_file:
    for query in queries:
        queries_file.write(query + "\n")

