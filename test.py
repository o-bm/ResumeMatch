# Example data for the table
data = [
    ["Job", "Similarity"],
    ["pilot resume", 0.95],
    ["file2", 0.89],
    ["file3", 0.78]
]

# Calculate the maximum width for each column
column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

# Print the table
for row in data:
    row_formatted = [str(item).ljust(width) for item, width in zip(row, column_widths)]
    print(' | '.join(row_formatted))

print('\n')