tp, fp, fn, tn = [int(x) for x in input().split()]

total = tp+fp+fn+tn
accuracy = round((tp+tn)/total, 4)
precision = round(tp/(tp+fp), 4)
recall = round(tp/(tp+fn), 4)
f1_score = round((2* precision * recall)/(precision + recall), 4)

print(accuracy)
print(precision)
print(recall)
print(f1_score)
