# pip install emojis

def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(gname):

            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun
    return innerFun

tmlGrt = outerFun("Vankam")
tmGtLion = tmlGrt("lion")
tmGtLion("Surya")






"""
engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")


egSnArw = engGrt("------>")
egDblArw = engGrt("=====>>")
tmSnArw = tmlGrt("------>")
tmDblArw = tmlGrt("======>>")


egSnArw("Sachin")
egDblArw("Sehwag")

tmSnArw('Ashwin')
tmDblArw('Natraj')
"""