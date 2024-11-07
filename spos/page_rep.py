from collections import deque
from typing import List


class ReplacementAlgorithm:
    def __init__(self, nframes: int) -> None:
        self._faults = 0
        self.nframes = nframes
        self.queue = deque()
        self.pageset = set()

    def replace(self, pages: List[int]) -> None:
        for page in pages:
            print(f"\nAccessing page: {page}")

            if page not in self.pageset:
                print(f"Page fault! {page} not in memory.")
                if len(self.pageset) == self.nframes:
                    removed_page = self.queue.popleft()
                    self.pageset.remove(removed_page)
                    print(f"Removing oldest page: {removed_page}")

                self.pageset.add(page)
                self.queue.append(page)
                self._faults += 1
            else:
                print(f"Page {page} is already in memory.")

            print(f"Current memory pageset: {self.pageset}")
            print(f"Queue order (FIFO): {list(self.queue)}")

    def faults(self) -> int:
        return self._faults


# Driver code
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
algo = ReplacementAlgorithm(nframes=3)
algo.replace(pages)

print(f"\nTotal Page Faults: {algo.faults()}")
print(f"Total Hits: {len(pages) - algo.faults()}")
