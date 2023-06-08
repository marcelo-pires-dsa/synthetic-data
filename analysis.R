install.packages("tidyverse")

library(tidyverse)

real_data <- read.csv("./dataset/raw/customer_support_tickets_processed.csv")
synthetic_data <- read.csv("./dataset/synthetic/synthetic-customer_support_tickets.csv")

View(data)
View(synthetic_data)
