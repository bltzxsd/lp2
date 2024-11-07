from typing import List


class Process:
    def __init__(
        self,
        pid: int,
        burst_time: int,
    ):
        self.pid = pid
        self.bt = burst_time
        self.tat = 0
        self.wt = 0

    def __repr__(self):
        return f"Process(pid={self.pid}, bt={self.bt}, wt={self.wt}), tat={self.tat}"


class FcfsScheduler:
    def __init__(self, processes: List[Process]) -> None:
        self.proc = processes
        total_wait = 0
        for p in self.proc:
            p.wt = total_wait
            p.tat = p.wt + p.bt
            total_wait += p.bt

    def avg_wait(self) -> float:
        total_wait = sum(p.wt for p in self.proc)
        return round(total_wait / len(self.proc), 4)

    def avg_turnaround(self) -> float:
        total_tat = sum(p.tat for p in self.proc)
        return round(total_tat / len(self.proc), 4)

    def __repr__(self) -> str:
        print("Process\t| Burst\t| Wait\t| Turnaround")
        ret = ""
        for p in self.proc:
            ret += f"{p.pid}\t| {p.bt} \t| {p.wt}\t| {p.tat}\n"

        return ret


if __name__ == "__main__":
    p1 = Process(1, 10)
    p2 = Process(2, 5)
    p3 = Process(3, 8)

    processes = [p1, p2, p3]

    scheduler = FcfsScheduler([p1, p2, p3])

    print(*processes, sep='\n')

    print(scheduler)
    print(f"Average waiting time: {scheduler.avg_wait()}")
    print(f"Average turnaround time: {scheduler.avg_turnaround()}")
