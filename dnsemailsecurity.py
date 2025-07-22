import dns.query
import dns.message
import socket

def query_cname_udp(server_name, port, domain):
    try:
        server_ip = socket.gethostbyname(server_name)
        query = dns.message.make_query(domain, dns.rdatatype.CNAME)
        response = dns.query.udp(query, server_ip, port=port, timeout=5)
        if response.answer:
            for answer in response.answer:
                if answer.rdtype == dns.rdatatype.CNAME:
                    for item in answer.items:
                        print(item.target.to_text())
    except Exception as e:
        print(f"errore CNAME UDP: {e}")

if __name__ == "__main__":
    server = "emailsec.challs.olicyber.it"
    port = 10502
    domain = "_netblocks.mail.dns-email.localhost"
    query_cname_udp(server, port, domain)







''' tentativi prima di trovare la flag '''
#def query_record(server_name, port, domain, rdatatype, use_tcp=False):
#    try:
#        server_ip = socket.gethostbyname(server_name)
#        query = dns.message.make_query(domain, rdatatype)
#        if use_tcp:
#            response = dns.query.tcp(query, server_ip, port=port, timeout=5)
#        else:
#            response = dns.query.udp(query, server_ip, port=port, timeout=5)
#
#        if response.answer:
#            print(f"Risposta {rdatatype} {'TCP' if use_tcp else 'UDP'} per {domain}:")
#            for answer in response.answer:
#                print(answer)
#        else:
#            print(f"Nessuna risposta {rdatatype} {'TCP' if use_tcp else 'UDP'} per {domain}.")
#    except Exception as e:
#        print(f"Errore {rdatatype} {'TCP' if use_tcp else 'UDP'} per {domain}: {e}")

#if __name__ == "__main__":
#    server = "emailsec.challs.olicyber.it"
#    port = 10502
#    domains = [
#        "dns-email.localhost",
#        "_spf.dns-email.localhost",
#        "_dmarc.dns-email.localhost",
#        "_spf.mail.dns-email.localhost",
#        "_netblocks.mail.dns-email.localhost",
#        "flag.dns-email.localhost",
#        "secret.dns-email.localhost",
#        "ctf.dns-email.localhost"
#    ]
#    record_types = ['TXT', 'MX', 'A']

#    for d in domains:
#        for rtype in record_types:
#            query_record(server, port, d, rtype, use_tcp=False)
#            query_record(server, port, d, rtype, use_tcp=True)