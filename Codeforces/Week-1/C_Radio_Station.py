n, m = map(int, input().split())
commands = {}
for i in range(n):
    command = input().split()
    commands[command[1]] = command[0]

# print(commands)
configuration = []
for i in range(m):
    command_ip = input()
    name, ip = command_ip.split()
    # print(ip[:-1])
    # print(commands.keys())
    # print(str(ip[:-1]) in commands.keys())
    if ip[:-1] in commands.keys():
        configuration.append("".join(command_ip)+" #"+commands[ip[:-1]])
    # print(configuration)
for i in configuration:
    print(i)