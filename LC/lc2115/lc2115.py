class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        s = set(supplies)
        flag = True
        L = set(recipes[:])
        while flag and recipes:
            flag = False
            nxt1, nxt2 = [], []
            for i, r in enumerate(recipes):
                if all([item in s for item in ingredients[i]]):
                    s.add(r)
                    flag = True
                else:
                    nxt1.append(r)
                    nxt2.append(ingredients[i])
            recipes = nxt1
            ingredients = nxt2
        return list(s.intersection(L))