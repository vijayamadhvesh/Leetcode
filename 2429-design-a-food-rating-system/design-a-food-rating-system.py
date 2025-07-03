from collections import defaultdict
class FoodRatings(object):

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_rating = {}              # food -> rating
        self.food_to_cuisine = {}             # food -> cuisine
        self.cuisine_to_heap = defaultdict(list)  # cuisine -> max-heap of (-rating, food)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_rating[f] = r
            self.food_to_cuisine[f] = c
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))  # Lazy push

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]

        # Lazy removal: clean outdated entries
        while True:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)