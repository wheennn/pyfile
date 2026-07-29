# pyfile — v0.1
# Est. 17.07.26
# by wheen

# ---- Config ----

import os, platform, keyboard, time, sys
hotkeys_reg = False
if len(sys.argv) == 2:
 pos, dir, obj, txt_objects = 0, sys.argv[1], "", []
else:
 raise TypeError("missing 1 required positional argument: 'dir'")

# ---- Core ----

# OS-managed console commands dispatcher
class OSCommands:

 def __init__(self):
  self.osname = platform.system()
  self.cmd = ["cls", None] if platform.system() == "Windows" else ["clear", "open"] if platform.system() == "Darwin" else ["clear", "xdg-open"] if platform.system() == "Linux" else []
  self.root_dir = "Local Disk (C:)" if platform.system() == "Windows" else "Root Directory (/)"
  self.dir = dir

 def clear_screen(self):
  os.system(self.cmd[0])

 def open_file(self):

  if self.osname == "Windows":
   os.startfile(self.dir)

  else:
   os.system(f"{self.cmd[1]} '{self.dir}'")

# Initializator and displayer of directories
def main(e: str):
 global pos, dir, obj, txt_objects, opes, hotkeys_reg

 if sys.argv[1] in ("-current", "-c") and e == "on_startup":
  dir = os.getcwd()

 opes = OSCommands()
 opes.clear_screen()

 if not hotkeys_reg:
  for i in ["up", "down", "enter", "q"]:
   keyboard.add_hotkey(hotkey=i, callback=key_on_press, args=(i,), suppress=True)
  hotkeys_reg = True

 listdir, txt_objects = os.listdir(dir), os.listdir(dir)

 for i in range(len(listdir)):
  obj = listdir[i]
  txt_objects[i] = ui_string_design(textpos=1 if i != len(listdir) - 1 else 2)

 pos, obj = len(listdir) - 1, listdir[len(listdir) - 1]
 txt_objects[len(txt_objects) - 1] += " <"

 render(e="main")

# Keyboard wait loop
def wait_keyboard():
 keyboard.wait()

# Handler of key press events
def key_on_press(key: str):
 global pos, dir, obj, txt_objects
 opos, txt_objects = key_action(key=key)
 if key in ("up", "down"):
  render(e="key_on_press", opos=opos)
 time.sleep(0.025)

# Processor of key actions
def key_action(key: str) -> tuple[int, list[str]]:
 global pos, dir, obj, opes
 listdir, opos = os.listdir(dir), pos

 if key in ("up", "down"):
  val = pos - 1 if key == "up" and pos > 0 else pos + 1 if key == "down" and pos < len(listdir) - 1 else pos
  opos = pos

  txt_objects[pos] = txt_objects[pos].replace(" <", "")
  txt_objects[val] += " <" if " <" not in txt_objects[val] else ""

  obj = listdir[val]
  pos = val

 elif key == "q":
  dir = os.path.dirname(dir)
  main(e="key_action")

 elif key == "enter":
  ndir = os.path.join(dir, obj)
  try:
   listdir = os.listdir(ndir)
   if listdir is not None:
    odir = dir
    try:
     opes.dir, dir = ndir, ndir
     main(e="key_action")
    except PermissionError:
     opes.dir, dir = odir, odir
     pass

  except FileNotFoundError, NotADirectoryError:
   odir = dir
   try:
    opes.dir = ndir
    opes.open_file()
   except PermissionError:
    opes.dir, dir = odir, odir
    pass

 return opos, txt_objects

# ---- TUI ----

# Builder of UI line string
def ui_string_design(textpos: int) -> str:
 pre = "┣" if textpos == 1 else "┗" if textpos == 2 else ""
 dsh = "━" if textpos == 0 else "━━"
 return f"{pre}{dsh} {obj}"

# Renderer of current directory view
def render(e: str, opos: int = 0):

 method = 2 if e == "main" else 2 if len(txt_objects) > os.get_terminal_size().lines else 1

 # Default version (render entire folder)
 if method == 2:

  print("\033[2J\033[H", end="", flush=True)
  print(f"┏━ {os.path.basename(dir) if os.path.basename(dir) else opes.root_dir}", flush=True)

  for i in range(len(txt_objects)):
   print(txt_objects[i], flush=True)

 # Optimized version (render only lines which user interacted with)
 elif method == 1:
  for i in [pos, opos]:
   print(f"\033[{i + 2};1H\033[2K{txt_objects[i]}\033[{len(txt_objects) + 1};1H", end="", flush=True)

main(e="on_startup")
wait_keyboard()