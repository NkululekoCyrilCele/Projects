import numpy as np
import pandas as pd


class Boundaries:
    def __init__(self, dataset, column):
        self.dataset = dataset
        self.column = column

    def method1(self):
        self.column = "total_rooms"
        des = self.dataset[self.column].describe()
        desPairs = {"count": 0, "mean": 1, "std": 2,
                    "min": 3, "25": 4, "50": 5, "75": 6, "max": 7}
        Q1 = des[desPairs['25']]
        Q3 = des[desPairs['75']]
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return f"The upper boundary is {upper}, and the lower boundary is {lower}."

    def method2(self):
        self.column = "total_bedrooms"
        des = self.dataset[self.column].describe()
        desPairs = {"count": 0, "mean": 1, "std": 2,
                    "min": 3, "25": 4, "50": 5, "75": 6, "max": 7}
        Q1 = des[desPairs['25']]
        Q3 = des[desPairs['75']]
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return f"The upper boundary is {upper}, and the lower boundary is {lower}."

    def method3(self):
        self.column = "population"
        des = self.dataset[self.column].describe()
        desPairs = {"count": 0, "mean": 1, "std": 2,
                    "min": 3, "25": 4, "50": 5, "75": 6, "max": 7}
        Q1 = des[desPairs['25']]
        Q3 = des[desPairs['75']]
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return f"The upper boundary is {upper}, and the lower boundary is {lower}."

    def method4(self):
        self.column = "households"
        des = self.dataset[self.column].describe()
        desPairs = {"count": 0, "mean": 1, "std": 2,
                    "min": 3, "25": 4, "50": 5, "75": 6, "max": 7}
        Q1 = des[desPairs['25']]
        Q3 = des[desPairs['75']]
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return f"The upper boundary is {upper}, and the lower boundary is {lower}."

    def method5(self):
        self.column = "median_income"
        des = self.dataset[self.column].describe()
        desPairs = {"count": 0, "mean": 1, "std": 2,
                    "min": 3, "25": 4, "50": 5, "75": 6, "max": 7}
        Q1 = des[desPairs['25']]
        Q3 = des[desPairs['75']]
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return f"The upper boundary is {upper}, and the lower boundary is {lower}."

    def method6(self):
        self.column = "median_house_value"
        des = self.dataset[self.column].describe()
        desPairs = {"count": 0, "mean": 1, "std": 2,
                    "min": 3, "25": 4, "50": 5, "75": 6, "max": 7}
        Q1 = des[desPairs['25']]
        Q3 = des[desPairs['75']]
        IQR = Q3 - Q1
        lower = Q1 - (1.5 * IQR)
        upper = Q3 + (1.5 * IQR)
        return f"The upper boundary is {upper}, and the lower boundary is {lower}."
