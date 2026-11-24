import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def __init__(self, heuristic=None):
        self.custom_heuristic = heuristic

    def heuristic(self, state: State) -> int:
        if self.custom_heuristic is not None:
            return self.custom_heuristic(state)

        distance = 0
        for index, tile in enumerate(state.tiles):
            if tile != 0:
                row = index // 3
                col = index % 3
                goal_row = (tile - 1) // 3
                goal_col = (tile - 1) % 3
                distance += abs(row - goal_row) + abs(col - goal_col)
        return distance

    def search(self, initial: State) -> SearchResult:
        # Se a prioridade empatar, State compara os custos dos caminhos.
        frontier = [(initial.cost + self.heuristic(initial), initial)]
        best_cost = {initial.tiles: initial.cost}
        result = SearchResult(None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            _, current = heapq.heappop(frontier)
            if current.cost > best_cost[current.tiles]:
                continue

            if current.is_goal:
                result.solution = current
                result.depth = current.cost - initial.cost
                return result

            result.nodes_expanded += 1
            for child in current.neighbors():
                if child.cost < best_cost.get(child.tiles, float("inf")):
                    best_cost[child.tiles] = child.cost
                    priority = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (priority, child))
                    result.nodes_generated += 1

            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
