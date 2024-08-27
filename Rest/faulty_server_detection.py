class Solution:
    def countFaults(self, n: int, logs: str):
        # n servers
        # logs: <id> <error/success> (size m)
        res = 0
        status = {}
        for s in logs:
            parts = s.split(" ", 1)
            server = parts[0]
            msg = parts[1].strip()
            print(server)
            print(msg.strip())
            if msg == "error":
                status[server] = 1 + status.get(server, 0)
            else:
                status[server] = 0
            
            if status[server] == 3:
                res += 1 
                status[server] = 0
        return res