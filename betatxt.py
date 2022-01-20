import colors, os
red = colors.color.fg.red
red2 = colors.color.fg.red+colors.color.bold
reset = colors.color.reset
blue = colors.color.fg.lightcyan
green = colors.color.fg.lightgreen
purple = colors.color.fg.purple
strike = colors.color.strikethrough
def show(tf):
  os.system('clear')
  if tf == True:
      print("%sDISCLAIMER!%s\n%s----------------------------------------------------------%s\nThis program is still in %sbeta testing%s.\nPlease %sdo not%s think of this as a %sfinished project%s." % (red2, reset, purple+strike, reset, blue, reset, red, reset, green, reset))