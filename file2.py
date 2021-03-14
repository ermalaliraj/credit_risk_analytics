install.packages("pROC")
library(pROC)
# Remove all missing values
hmeq.omit <- na.omit(hmeq)
# Convert JOB and REASON to factor
hmeq.omit$JOB <- as.factor(hmeq.omit$JOB)
hmeq.omit$REASON <- as.factor(hmeq.omit$REASON)

hmeq.full <- glm(BAD ~ ., data=hmeq.omit, family=binomial(link="logit"))
prob <- predict(hmeq.full, type=c("response"))
hmeq.omit$prob <- prob
g <- roc(BAD ~ prob, data = hmeq.omit)
plot(g)
auc(g)