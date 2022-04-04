library(readxl)
library(lmerTest)
library("xlsx")
library(performance)
library(merTools)
library(dplyr)
dataset <- read_excel("/Users/leeli/Desktop/result/Total.xlsx")
dataset[is.na(dataset)] <- 0

# Build the model
model <- lmer(WEEKLY_GROSS ~ Current_Age + POS + Starts
              + Min + Gls + Ast + CrdY + CrdR + SoT + G_Sh
              + Pass_Att + Cmp_per + TklW + Blocks + Int + Clr
              + Dribble_Att + Dribble_Succ_per + Carries + Targ + Rec_per
              + grade_value + (1 | League_num/Club_num),
              data=dataset, REML=TRUE)

# save the performance of model
sink("/Users/leeli/Desktop/model/mixed_effect/Summary4.txt")
print(summary(model),correlation=TRUE)
model_performance(model)
sink()
# save the model
save(model, file="/Users/leeli/Desktop/model.rda")

# predict the results and calculate the 90% prediction interval
test = read_excel("/Users/leeli/Desktop/result/test.xlsx")
pred = predictInterval(merMod = model, newdata = test,
                       level = 0.90, type="linear.prediction",
                       include.resid.var = 0, seed = 10)
pred = predict(model, test)
write.xlsx(pred,"/Users/leeli/Desktop/model/mixed_effect/prediction95.xlsx")

