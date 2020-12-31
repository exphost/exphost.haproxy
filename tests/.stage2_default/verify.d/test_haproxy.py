def test_haproxy(host):
    apps = {}
    for i in range(4):
        hostname = host.check_output("curl localhost:7777/hostname.php")
        apps[hostname] = apps.get(hostname, 0) + 1
    assert apps.get("app-0") > 0
    assert apps.get("app-1") > 0
