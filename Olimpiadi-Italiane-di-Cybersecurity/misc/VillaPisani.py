import socket
import dns.resolver

res = dns.resolver.Resolver()
res.nameservers = [socket.gethostbyname("pisani.challs.olicyber.it")]
res.port = 10500
res.timeout = 5
res.lifetime = 5
visited = set()

def PriviPisani(name):
    if name in visited:
        return False
    visited.add(name)
    try:
        answers = res.resolve(name, "TXT")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        answers = []

    for rdata in answers:
        txt = b"".join(rdata.strings).decode('utf-8', errors='ignore')
        if "flag" in txt:
            print("Flag:", txt)
            return True
        else:
            print(f"{name} TXT → {txt}")

    for direction in ("up", "down", "left", "right"):
        target = f"{direction}.{name}"
        print(f"Arrovellandomi verso {target}")
        try:
            cname_ans = res.resolve(target, "CNAME")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
            continue

        for rdata in cname_ans:
            next_name = str(rdata.target).rstrip('.')
            if PriviPisani(next_name):
                return True

    return False

if __name__ == "__main__":
    start = "00000000-0000-4000-0000-000000000000.maze.localhost"
    if not PriviPisani(start):
        print("Unlucky")