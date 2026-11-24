from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        frontier = [initial]
        best_depth = {}
        result = SearchResult(None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            current = frontier.pop()
            depth = current.cost - initial.cost
            if depth >= best_depth.get(current.tiles, self.depth_limit + 1):
                continue
            best_depth[current.tiles] = depth

            if current.is_goal:
                result.solution = current
                result.depth = depth
                return result

            if depth < self.depth_limit:
                result.nodes_expanded += 1
                for child in reversed(current.neighbors()):
                    if depth + 1 < best_depth.get(child.tiles, self.depth_limit + 1):
                        frontier.append(child)
                        result.nodes_generated += 1

                result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
