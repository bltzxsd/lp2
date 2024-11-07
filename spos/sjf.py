class Process:
    def __init__(self, pid: int, burst_time: int, arrival_time: int):
        self.bt = burst_time
        self.pid = pid
        self.arv = arrival_time
        self.rem = burst_time
        # manual
        self.tat = 0  # turn around time
        self.wt = 0  # waiting time

    def __repr__(self) -> str:
        return f"Process(pid={self.pid}, self.bt={self.bt}, arrival_time={self.arv})"


class SRTFScheduler:
    def __init__(self, processes) -> None:
        n = len(processes)
        completed = 0
        curr_time = 0

        while completed < n:
            min_remaining = float("inf")
            curr_proc = None

            for p in processes:
                # Check if process has arrived and is not completed
                if p.arv <= curr_time and p.rem > 0:
                    if p.rem < min_remaining:
                        min_remaining = p.rem
                        curr_proc = p

            if not curr_proc:
                curr_time += 1
                continue

            curr_proc.rem -= 1

            if curr_proc.rem == 0:
                completed += 1
                finish_time = curr_time + 1
                
                # Calculate waiting time and turnaround time
                curr_proc.wt = finish_time - curr_proc.bt - curr_proc.arv
                curr_proc.tat = finish_time - curr_proc.arv

            curr_time += 1


        self.proc = processes

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
    proceses = [Process(1, 6, 1), Process(2, 8, 1), Process(3, 7, 2), Process(4, 3, 3)]

    scheduler = SRTFScheduler(proceses)

    print(scheduler)
    print(f"Average waiting time: {scheduler.avg_wait()}")
    print(f"Average turnaround time: {scheduler.avg_turnaround()}")
