# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        supplies = Counter(supplies)
        graph = defaultdict(list)
        income = defaultdict(int)
        q = deque()
        ans = []

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                if ingredient in recipes:
                    graph[ingredient].append((i, recipes[i]))
                    income[recipes[i]] += 1

        for i in range(len(recipes)):
            if not income[recipes[i]]:
                q.append((i, recipes[i]))


        while q:
            i, recipe = q.popleft()
            flag = True

            for ingredient in ingredients[i]:
                if not supplies[ingredient]:
                    flag = False
                    break

            if flag:
                supplies[recipe] = 1
                ans.append(recipe)

                for index, other_recipe in graph[recipe]:
                    income[other_recipe] -= 1
                    if income[other_recipe] <= 0:
                        q.append((index, other_recipe))

        return ans