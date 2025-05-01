
import socket
import requests

def scan_network(subnet):
    results = []
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        try:
            s = socket.create_connection((ip, 80), timeout=0.5)
            results.append(f"[+] Port 80 open on {ip}")
            s.close()
        except:
            results.append(f"[-] {ip} not reachable on port 80")
    return results

def search_cve(keyword):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=5"
    headers = {
        "apiKey": "YOUR_API_KEY"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        data = r.json()
        if "vulnerabilities" not in data:
            return {"error": "No vulnerabilities found or bad API key."}
        result = []
        for item in data["vulnerabilities"]:
            cve_id = item["cve"]["id"]
            desc = item["cve"]["descriptions"][0]["value"]
            refs = item["cve"].get("references", [])
            solution = refs[0]["url"] if refs else "No solution available"
            result.append((cve_id, desc, solution))
        return {"results": result}
    except Exception as e:
        return {"error": str(e)}
