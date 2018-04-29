#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 29, 2018, 12:25 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


#
# 建造者模式

# 相关模式：思路和模板方法模式很像，模板方法是封装算法流程，对某些细节，提供接口由子类修改，建造者模式更为高层一点，将所有细节都交由子类实现。
# 建造者模式：将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示。
# 基本思想
# 某类产品的构建由很多复杂组件组成；
# 这些组件中的某些细节不同，构建出的产品表象会略有不同；
# 通过一个指挥者按照产品的创建步骤来一步步执行产品的创建；
# 当需要创建不同的产品时，只需要派生一个具体的建造者，重写相应的组件构建方法即可。

def printInfo(info):
    print(info)


# the Base of builders
class PersonBuilder():
    def BuildHead(self):
        pass

    def BuildBody(self):
        pass

    def BuildArm(self):
        pass

    def BuildLeg(self):
        pass


# Fatty
class PersonFatBuilder(PersonBuilder):
    type = 'Fatty'

    def BuildHead(self):
        printInfo("Building %s's head..." % self.type)

    def BuildBody(self):
        printInfo("Building %s's body..." % self.type)

    def BuildArm(self):
        printInfo("Building %s's arms..." % self.type)

    def BuildLeg(self):
        printInfo("Building %s's legs..." % self.type)


# Thin
class PersonThinBuilder(PersonBuilder):
    type = 'Thin'

    def BuildHead(self):
        printInfo("Building %s's head..." % self.type)

    def BuildBody(self):
        printInfo("Building %s's body..." % self.type)

    def BuildArm(self):
        printInfo("Building %s's arms..." % self.type)

    def BuildLeg(self):
        printInfo("Building %s's legs..." % self.type)


# 指挥者
class PersonDirector():
    pb = None

    def __init__(self, pb):
        self.pb = pb

    def CreatePereson(self):
        self.pb.BuildHead()
        self.pb.BuildBody()
        self.pb.BuildArm()
        self.pb.BuildLeg()


if __name__ == '__main__':
    pb = PersonThinBuilder()
    pd = PersonDirector(pb)
    pd.CreatePereson()

    pb = PersonFatBuilder()
    pd = PersonDirector(pb)
    pd.CreatePereson()
