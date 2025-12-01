# Load necessary libraries
library(rvest)
library(dplyr)

# Wikipedia page URL
url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

# Read the HTML page
page <- read_html(url)

# Find the first table under "CSV example: cars"
cars_table <- page %>%
  html_node("table.wikitable") %>%
  html_table(fill = TRUE)

# Save to CSV locally
write.csv(cars_table, "cars.csv", row.names = FALSE)

print("CSV saved successfully!")
