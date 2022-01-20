# adds custom color library and dependancies for clear and delay
import colors, time, os
# color variables
font = colors.color.fg
style = colors.color
bg = colors.color.bg
# line number
line = 0
# dev mode (boolean only)
devmode = False
# command prefix
prefix = font.lightgreen+"jax.os"+font.pink+" > "+font.lightcyan
# ascii art
class ascii:
  start = open("ascii/start.txt", "r").read()
# extra commands
class extras:
  def delay(delay):
    time.sleep(delay)
  def clear():
    os.system('clear')
  def error(command):
    return ("%sError!\nCommand: %s\nError occurred at line %s.\nUse help or cmds for the command list." % (font.red, command, str(line)))
# os commands
class commands:
  def help(command):
    helplist = "Commands:"
    cmdlist = ["help", "clear"]
    if command == "":
      for i in range(len(cmdlist)):
        helplist += "\n%s"%cmdlist[i]
      return style.reset+helplist
    elif command == "cmds" or command == "commands" or command == "help":
      return (style.reset+"help\nAliases:\ncmds, commands, help\nUsage:\nhelp [command-name]")
    elif command == "clear" or command == "cls" or command == "clearscreen":
      return (style.reset+"cls\nAliases:\nclear, cls, clearscreen\nUsage:\ncls")
  def cls():
    extras.clear()
    print(font.blue+ascii.start)
    line = 0
  def colortest():
    print(style.bold+"Bold\n"+style.reset+style.strikethrough+"Strikethrough\n"+style.reset+style.underline+"Underline\n")
    print(font.red+"Red\n"+font.orange+"Orange"+font.yellow+"Yellow\n"+font.green+"Green\n"+font.cyan+"Cyan\n"+font.blue+"Blue\n"+font.purple+"Purple\n"+font.pink+"Pink\n"+font.black+bg.white+"Black\n"+style.reset+font.white+"White\n"+font.grey+"Grey\n"+font.lightblue+"Light Blue\n"+font.lightcyan+"Light Cyan\n"+font.lightgreen+"Light Green\n"+font.lightred+"Light Red\n\n"+style.reset)
    print("Loading...")
# main function
def run():
  global line
  extras.delay(3)
  extras.clear()
  commands.colortest()
  extras.delay(1)
  extras.clear()
  print(font.blue+ascii.start)
  # main loop
  while True:
    prefixedit = font.pink+"line"+str(line+1)+style.reset+"|"+prefix
    rawcmd = input(prefixedit)
    cmd = str(rawcmd.split(' ')[0])
    args = rawcmd.split(' ')
    line = line+1
    if devmode == True:
      print(rawcmd)
      print(cmd)
      print(args)
    if cmd == "cmds" or cmd == "help" or cmd == "commands":
      if len(args) == 1:
        print(commands.help(""))
      else:
        print(commands.help(str(args[1])))
    elif cmd == "clear" or cmd == "cls" or cmd == "clearscreen":
      commands.cls()
    else:
      print(extras.error(cmd))