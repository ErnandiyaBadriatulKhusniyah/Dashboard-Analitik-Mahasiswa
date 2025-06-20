def hitung_ipk(transkrip_list):
    total_sks = sum(t.sks for t in transkrip_list)
    total_mutu = sum(t.mutu for t in transkrip_list)
    ipk = total_mutu / total_sks if total_sks > 0 else 0
    return round(ipk, 2), round(total_sks, 2), round(total_mutu, 2)
