library(tidyverse)
library(dplyr)
library(magrittr)



dataset <- read.csv("dataset/raw/customer_support_tickets.csv")

glimpse(dataset)

#Renomear as variáveis. caixa baixa (lower case) e trocar pontos por underline
dataset <- dataset %>%
  rename(`ticket_id`=1,
         `customer_name`=2,
         `customer_email`=3,
         `customer_age`=4,
         `customer_gender`=5,
         `product_purchased`=6,
         `date_of_puschase`=7,
         `ticket_type`=8,
         `ticket_subject`=9,
         `ticket_description`=10,
         `ticket_status`=11,
         `resolution`=12,
         `ticket_priority`=13,
         `ticket_channel`=14,
         `first_response_time`=15,
         `time_to_resolution`=16,
         `customer_satisfaction_rating`=17)
      
write_csv(dataset, file="dataset/raw/customer_support_tickets_processed.csv")