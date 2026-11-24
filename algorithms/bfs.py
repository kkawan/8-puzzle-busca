from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        frontier = deque([initial])
        visited = {initial.tiles}
        result = SearchResult(None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            current = frontier.popleft()
            if current.is_goal:
                result.solution = current
                result.depth = current.cost - initial.cost
                return result

            result.nodes_expanded += 1
            for child in current.neighbors():
                if child.tiles not in visited:
                    visited.add(child.tiles)
                    frontier.append(child)
                    result.nodes_generated += 1

            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
