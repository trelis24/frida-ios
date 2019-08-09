import frida, sys

script = ''
bundle = ''

f = open(script, "r")
s = f.read()

device = frida.get_usb_device(1000)
pid = device.spawn([bundle])
session = device.attach(pid)
script = session.create_script(s)
script.load()
device.resume(pid)
sys.stdin.read()