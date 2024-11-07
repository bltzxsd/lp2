class Process:
    def __init__(
        self,
        pid: int,
        burst_time: int,
        priority: int,
    ):
        self.pid = pid
        self.prio = priority
        self.bt = burst_time

        # manually set
        self.arv = 0
        self.tat = 0
        self.wt = 0

    def __repr__(self):
        return f"Process(pid={self.pid}, bt={self.bt}, wt={self.wt})"


class PriorityScheduler:
    def __init__(self, processes) -> None:
        total_wait = 0
        for i, p in enumerate(processes):
            p.arv = i + 1

        for p in processes:
            p.wt = total_wait
            p.tat = p.wt + p.bt
            total_wait += p.bt

        self.proc = sorted(processes, key=lambda x: -x.prio)

    def avg_wait(self) -> float:
        total_wait = sum(p.wt for p in self.proc)
        return round(total_wait / len(self.proc), 4)
    
    def avg_turnaround(self) -> float:
        total_tat = sum(p.tat for p in self.proc)
        return round(total_tat / len(self.proc), 4)
    
    def __repr__(self) -> str:
        print("Process\t| Burst\t| Priority\t| Arrival\t| Wait\t| Turnaround")
        ret = ""
        for p in self.proc:
            ret += f"{p.pid}\t| {p.bt}\t| {p.prio}\t\t| {p.arv}\t\t| {p.wt}\t| {p.tat}\n"

        return ret
    
if __name__ == "__main__":
    p1 = Process(1, 3, 3)
    p2 = Process(2, 5, 4)
    p3 = Process(3, 1, 1)
    p4 = Process(4, 7, 7)
    p5 = Process(5, 4, 8)

    processes = [p1, p2, p3, p4, p5]

    scheduler = PriorityScheduler(processes)

    print(*processes, sep='\n')

    print(scheduler)

    print(f"Average waiting time: {scheduler.avg_wait()}")
    print(f"Average turnaround time: {scheduler.avg_turnaround()}")