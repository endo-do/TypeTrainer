import csv
from collections import defaultdict

input_file = r'ressources\unigram_freq.csv'
output_file = r'ressources\all_words.csv'

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, \
         open(output_file, 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        next(reader)
        next(reader)

        writer.writerow(['word'])

        for row in reader:
            if len(row[0]) > 2 and len(row[0]) < 9:
                writer.writerow([row[0]])

    print(f"'{input_file}' succesfully cleaned and saved as '{output_file}'")

def get_entry_count(csv_file):
    with open(csv_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        entry_count = sum(1 for row in reader) - 1
    print(f"{entry_count} entries in '{csv_file}'")

def average_word_length(csv_file):
    total_length = 0
    total_words = 0

    with open(csv_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            word = row[0].strip()
            total_length += len(word)
            total_words += 1

    if total_words == 0:
        print(f"No words in '{csv_file}'") 
    else:
        print(f"Avarge word length in '{csv_file}': {round(total_length / total_words)}")

def split_csv(input_csv):
    word_dict = defaultdict(list)

    with open(input_csv, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            word = row[0].strip()
            word_length = len(word)
            word_dict[word_length].append(word)

    for length, words in word_dict.items():
        output_csv = f'ressources\words_{length}.csv'
        with open(output_csv, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for word in words:
                writer.writerow([word])

    print(f"'{input_csv}' split into multiple files based on word length.")


def get_entry_counts():
    for i in range(3, 9):
        path = f"ressources\words_{i}.csv"
        get_entry_count(path)