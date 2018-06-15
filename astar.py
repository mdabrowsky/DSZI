import sys
from abc import ABCMeta, abstractmethod


class AStar:
    @abstractmethod
    def heuristic_cost_estimate(self, start, goal):
        raise NotImplementedException

    @abstractmethod
    def distance_between(self, n1, n2):
        raise NotImplementedException

    @abstractmethod
    def neighbors(self, node):
        raise NotImplementedException

    def _yield_path(self, came_from, last):
        yield last
        current = came_from[last]
        while True:
            yield current
            if current in came_from:
                current = came_from[current]
            else:
                break

    def _reconstruct_path(self, came_from, last):
        return list(reversed([p for p in self._yield_path(came_from, last)]))

    def astar(self, start, goal):
        closedset = set([])
        openset = set([start])
        came_from = {}

        g_score = {}
        g_score[start] = 0

        f_score = {}
        f_score[start] = self.heuristic_cost_estimate(start, goal)

        while len(openset) > 0:
            current = min(f_score, key=f_score.get)
            if current == goal:
                return self._reconstruct_path(came_from, goal)
            openset.discard(current)
            del f_score[current]
            closedset.add(current)

            for neighbor in self.neighbors(current):
                if neighbor in closedset:
                    continue
                tentative_g_score = g_score[current] + self.distance_between(current, neighbor)
                if (neighbor not in openset) or (tentative_g_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic_cost_estimate(neighbor, goal)
                    openset.add(neighbor)
        return None


__all__ = ['AStar']
