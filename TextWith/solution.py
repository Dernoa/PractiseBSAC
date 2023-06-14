testText = [
  'Given$a$text$file$of$many$lines',
  'where$fields$within$a$line$',
  'are$delineated$by$a$single$"dollar"$character',
  'write$a$program',
  'that$aligns$each$column$of$fields',
  'by$ensuring$that$words$in$each$',
  'column$are$separated$by$at$least$one$space.',
  'Further,$allow$for$each$word$in$a$column$to$be$either$left$',
  'justified,$right$justified',
  'or$center$justified$within$its$column.'
]

a = 0
max = 0

for i in range(0,10):
    a=0
    for k in range(0,len(testText[i])):
        a += 1
        if testText[i][k] == "$":
            if max < a:
                max = a
            a = 0
    testText[i] = testText[i].replace("$"," ")

for i in range(0,10):
    testText[i] = testText[i].replace(" "," " * max)
    print(testText[i])
