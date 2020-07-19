from convNet import model as conv
Net = conv()
Net.oneHotEncode()
Net.setupData()
Net.setupModel()
def trainOrTest(ifTrain):
    if ifTrain:
        Net.compileAndTrain(200)
    else:
        print(Net.predict('bottle.jpg', test=True))
        print(Net.decodeOneHot())
        print("[0.18498555 0.18216586 0.13744305 0.2682292  0.2455441  0.07737438]")
trainOrTest(True)