import time
import locale
import psutil

disks = psutil.disk_partitions()
cpuTempPath = '/sys/class/thermal/thermal_zone1/temp'
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
currentDate = time.strftime('%a %d de %b')
currentTime = time.strftime('%H:%M')

mem = int(psutil.virtual_memory().percent)
cpu_uso = int(psutil.cpu_percent(interval=1))

file = open(cpuTempPath)
cpu_temp = int(int(file.read()) / 1000)
file.close()


def color_disks(c_disk):
    if c_disk < 50:
        return "#00FF00"
    if c_disk < 60:
        return "#bfff00"
    if c_disk < 70:
        return "#ffff00"
    if c_disk < 80:
        return "#ffbf00"
    if c_disk < 90:
        return "#ff8000"
    return "#ff0000"


def color_mem(c_mem):
    if c_mem < 30:
        return "#00FF00"
    if c_mem < 45:
        return "#bfff00"
    if c_mem < 60:
        return "#ffff00"
    if c_mem < 75:
        return "#ffbf00"
    if c_mem < 90:
        return "#ff8000"
    return "#ff0000"


def color_uso(u_cpu):
    if u_cpu < 30:
        return "#00FF00"
    if u_cpu < 45:
        return "#bfff00"
    if u_cpu < 60:
        return "#ffff00"
    if u_cpu < 75:
        return "#ffbf00"
    if u_cpu < 90:
        return "#ff8000"
    return "#ff0000"


def color_temp(c_cpu):
    if c_cpu < 40:
        return "#00FF00"
    if c_cpu < 50:
        return "#bfff00"
    if c_cpu < 60:
        return "#ffff00"
    if c_cpu < 70:
        return "#ffbf00"
    if c_cpu < 80:
        return "#ff8000"
    return "#ff0000"


def icon(i_cpu):
    if i_cpu < 50:
        return "\uf2cb"
    if i_cpu < 55:
        return "\uf2ca"
    if i_cpu < 60:
        return "\uf2c9"
    if i_cpu < 65:
        return "\uf2c8"
    return "\uf2c7"


print_text = ""

for i in range(0, len(disks)):
    if disks[i].mountpoint != '/boot':
        print_text = print_text + '\uf0a0 ' + disks[i].mountpoint + ':<span color="' + color_disks(
            int(psutil.disk_usage(disks[i].mountpoint).percent)) + '">' + str(
            psutil.disk_usage(disks[i].mountpoint).percent) + '%</span> '

print(
    print_text +
    '\uf2db:<span color="{}">{}%</span> '
    '\uf0ae :<span color="{}">{}%</span> '
    '{}:<span color="{}">{:>2}ºC</span> '
    '\uf073 <span color="#BEBEBE">{}</span> '
    '\uf017 <span color="#BEBEBE">{}</span> '
    .format(color_mem(mem), mem, color_uso(cpu_uso), cpu_uso, icon(cpu_temp), color_temp(cpu_temp), cpu_temp,
            currentDate, currentTime))
