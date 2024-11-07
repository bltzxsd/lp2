from collections import deque
from typing import List


class Process:
    def __init__(self, pid: int, burst_time: int) -> None:
        self.pid = pid
        self.bt = burst_time
        self.rem = burst_time
        self.wt = 0
        self.tat = 0

    def __repr__(self):
        return f"Process(pid={self.pid}, bt={self.bt}, wt={self.wt}, tat={self.tat})"


class RoundRobinScheduler:
    def __init__(self, processes: List[Process], quantum: int) -> None:
        ready_queue = deque(processes)
        current_time = 0

        while ready_queue:
            process = ready_queue.popleft()
            if process.rem > quantum:
                process.rem -= quantum
                current_time += quantum
                ready_queue.append(process)
            else:
                current_time += process.rem
                process.tat = current_time
                process.wt = current_time - process.bt
                process.rem = 0

        self.proc = processes
        pass

    def avg_wait(self) -> float:
        total_wait = sum(p.wt for p in self.proc)
        return round(total_wait / len(self.proc), 4)

    def avg_turnaround(self) -> float:
        total_tat = sum(p.tat for p in self.proc)
        return round(total_tat / len(self.proc), 4)

    def __repr__(self) -> str:
        print("Process\t| Burst\t| Waiting Time\t| Turnaround Time")
        ret = ""
        for p in self.proc:
            ret += f"{p.pid}\t| {p.bt}\t| {p.wt}\t\t| {p.tat}\n"
        return ret


if __name__ == "__main__":
    p1 = Process(1, 10)
    p2 = Process(2, 5)
    p3 = Process(3, 8)

    quantum = 2
    processes = [p1, p2, p3]

    scheduler = RoundRobinScheduler(processes, quantum)

    print(*sorted(processes, key=lambda x: x.tat), sep="\n")

    print(scheduler)

    print(f"Average waiting time: {scheduler.avg_wait()}")
    print(f"Average turnaround time: {scheduler.avg_turnaround()}")
