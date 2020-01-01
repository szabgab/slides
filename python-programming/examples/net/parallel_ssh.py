from pssh import ParallelSSHClient
hosts = ['myhost1', 'myhost2']
client = ParallelSSHClient(hosts)
output = client.run_command('ls -ltrh /tmp/', sudo=True)
